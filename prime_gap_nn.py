"""Predict the next prime gap with a small MLP and compare to simple baselines.

Train on primes in [TRAIN_LO, TRAIN_HI), test on a *different, larger* range
[TEST_LO, TEST_HI) so the net cannot memorise anything.

Target: k = gap/2 (gaps are even for p > 2), capped at K (class K = "gap >= 2K").
Metric: mean negative log-likelihood (nats) on the test range. Lower is better.
  - baseline "geometric": gap ~ geometric with mean ln(p)   (Cramer model)
  - "mod only": MLP seeing only p mod small primes (no gap history)
  - "full": MLP seeing p mod small primes + last H gaps
"""
import sys, time
import numpy as np
import torch, torch.nn as nn

K = 64          # gap classes: k = gap/2 in 1..K-1, class K-1 index = tail
H = 16          # history length (gaps)
MODS = [3, 4, 5, 7, 11, 13, 17, 19, 23]
TRAIN_LO, TRAIN_HI = 10**7, 10**8 + 3 * 10**6
TEST_LO, TEST_HI = 10**9, 10**9 + 2 * 10**7
torch.manual_seed(0); np.random.seed(0)


def primes_in(lo, hi):
    """Segmented sieve with numpy."""
    base = np.arange(2, int(hi**0.5) + 2)
    sv = np.ones(len(base), bool)
    for i in range(len(base)):
        if sv[i] and base[i] ** 2 < len(base) + 2:
            sv[i + base[i]::base[i]] = False
    bp = base[sv]
    out, seg = [], 10**7
    for s in range(lo, hi, seg):
        e = min(s + seg, hi)
        a = np.ones(e - s, bool)
        for p in bp:
            if p * p >= e:
                break
            st = max(p * p, (s + p - 1) // p * p)
            a[st - s::p] = False
        out.append(np.nonzero(a)[0] + s)
    return np.concatenate(out).astype(np.int64)


def build(pr):
    gaps = np.diff(pr)                       # gaps[i] = pr[i+1]-pr[i]
    n = len(gaps) - H
    idx = np.arange(H, len(gaps))            # predict gaps[idx] from gaps[idx-H:idx]
    p = pr[idx]                              # current prime = start of the target gap
    hist = np.stack([gaps[idx - H + j] for j in range(H)], 1).astype(np.float32)
    lnp = np.log(p).astype(np.float32)
    feats_hist = hist / lnp[:, None]
    mods = np.concatenate([np.eye(m, dtype=np.float32)[p % m] for m in MODS], 1)
    scale = ((lnp - 17) / 4)[:, None]
    y = np.minimum(gaps[idx] // 2, K) - 1    # 0..K-1
    return (torch.tensor(feats_hist), torch.tensor(mods), torch.tensor(scale),
            torch.tensor(lnp), torch.tensor(y, dtype=torch.long))


def geo_nll(lnp, y):
    q = 1 - 2 / lnp
    k = (y + 1).float()
    logp = torch.log(1 - q) + (k - 1) * torch.log(q)
    tail = (K - 1) * torch.log(q)            # P(k >= K) = q^(K-1)
    return -torch.where(y == K - 1, tail, logp).mean().item()


def make_net(d_in):
    return nn.Sequential(nn.Linear(d_in, 256), nn.ReLU(), nn.Linear(256, 256), nn.ReLU(),
                         nn.Linear(256, 128), nn.ReLU(), nn.Linear(128, K))


def run(name, tr, te, use_hist, epochs=6):
    def X(d):
        parts = [d[1], d[2]] + ([d[0]] if use_hist else [])
        return torch.cat(parts, 1)
    xtr, ytr, xte, yte = X(tr), tr[4], X(te), te[4]
    net = make_net(xtr.shape[1])
    opt = torch.optim.AdamW(net.parameters(), 1e-3, weight_decay=1e-4)
    steps = epochs * (len(xtr) // 4096)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, 2e-3, total_steps=steps)
    lf = nn.CrossEntropyLoss()
    t = time.time()
    for ep in range(epochs):
        perm = torch.randperm(len(xtr))
        for i in range(0, len(perm) - 4095, 4096):
            b = perm[i:i + 4096]
            opt.zero_grad(); lf(net(xtr[b]), ytr[b]).backward(); opt.step(); sched.step()
        with torch.no_grad():
            nll = lf(net(xte), yte).item()
        print(f"  [{name}] epoch {ep+1}/{epochs}  test NLL {nll:.4f}  ({time.time()-t:.0f}s)", flush=True)
    return nll


if __name__ == "__main__":
    t = time.time()
    ptr, pte = primes_in(TRAIN_LO, TRAIN_HI), primes_in(TEST_LO, TEST_HI)
    print(f"train primes: {len(ptr):,}  test primes: {len(pte):,}  ({time.time()-t:.0f}s)")
    tr, te = build(ptr), build(pte)
    base = geo_nll(te[3], te[4])
    print(f"baseline geometric(ln p) test NLL: {base:.4f}")
    a = run("mod only", tr, te, False)
    b = run("mod + gaps", tr, te, True)
    print(f"\nSUMMARY (nats/prime, lower = better)\n  geometric baseline : {base:.4f}\n"
          f"  MLP mod only       : {a:.4f}\n  MLP mod + {H} gaps  : {b:.4f}")
