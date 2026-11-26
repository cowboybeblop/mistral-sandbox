\\ Fonction L p-adique d'une courbe elliptique (réduction bonne ordinaire en p)
\\ par sommes de Riemann de Mazur–Tate–Teitelbaum sur le symbole modulaire x^+ de E.
\\ Normalisation : mu(b + p^n Z_p) = al^-n [b/p^n]^+ - al^-(n+1) [b/p^(n-1)]^+,
\\ avec [r]^+ = mseval(M, x^+, [oo, r]) et [0]^+ = L(E,1)/Omega^+ (Omega^+ = E.omega[1]).
\\ Alors (1 - 1/al)^-2 L_p(0) = L(E,1)/Omega^+, comme dans ellpadicL de PARI.
\\ Variable : L_p(T) = int (1+T)^{log_gamma <a>} dmu, gamma = 1+p ;
\\ en s (T = gamma^s - 1), coefficient de s^r = c_r * log_p(gamma)^r + termes en c_j, j < r.

\\ Racine unité de X^2 - ap X + p dans Z_p, à la précision prec.
mtt_alpha(ap, p, prec) =
{
  my(R = polrootspadic('X^2 - ap*'X + p, p, prec));
  R = select(z -> valuation(z, p) == 0, R);
  if (#R != 1, error("p non ordinaire"));
  R[1];
}

\\ Renvoie [c_0, ..., c_K] coefficients de L_p(T) en T, approximation de niveau n.
\\ MS = msfromell(E, 1) déjà calculé (réutilisé entre p et n).
mtt_series(E, MS, p, n, K, prec) =
{
  my(M = MS[1], xs = MS[2], ap = ellap(E, p), al = mtt_alpha(ap, p, prec));
  my(P = p^n, Q = p^(n-1), g = 1 + p, A, B, mu, gj, t, b, c, s1, s2);
  \\ valeurs du symbole aux niveaux n et n-1, indexées par le représentant dans [0, p^k)
  my(symn = vector(P, i, 0), symq = vector(Q, i, 0));
  for (i = 1, P - 1, if (i % p, symn[i + 1] = mseval(M, xs, [oo, i / P])));
  for (i = 1, Q - 1, if (i % p, symq[i + 1] = mseval(M, xs, [oo, i / Q])));
  if (Q == 1, symq[1] = mseval(M, xs, [oo, 0]));
  my(teich = vector(p - 1, a, lift(teichmuller(a + O(p^n)))));
  mu = vector(Q, j, 0);
  my(ain = 1 / al, ainn = ain^n, ainn1 = ain^(n+1));
  gj = 1;
  for (j = 0, Q - 1,
    s1 = 0; s2 = 0;
    for (a = 1, p - 1,
      b = (teich[a] * gj) % P;
      s1 += symn[b + 1];
      s2 += symq[(b % Q) + 1];
    );
    mu[j + 1] = ainn * s1 - ainn1 * s2;
    gj = (gj * g) % P;
  );
  \\ c_m = sum_j mu_j binomial(j, m)
  vector(K + 1, m, sum(j = 0, Q - 1, mu[j + 1] * binomial(j, m - 1)));
}

\\ Coefficients en s de L_p(gamma^s - 1), jusqu'à s^K, à partir des c_m.
mtt_s_coeffs(c, p, prec) =
{
  my(K = #c - 1, lg = log(1 + p + O(p^prec)), T, S);
  T = exp(lg * 'S + O('S^(K + 1))) - 1;
  S = sum(m = 0, K, c[m + 1] * T^m);
  vector(K + 1, m, polcoef(S, m - 1, 'S));
}
