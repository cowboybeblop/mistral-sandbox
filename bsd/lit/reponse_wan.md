# Réponse de Xin Wan (reçue par l'utilisateur, fin novembre 2026)

**Texte reçu (verbatim) :**
> Yes you are right. The choice is different from and much easier than the principal series case in my ANT paper. I just meant to make sure the quotients of \chi_1/\chi_2 have conductor t_1 for h and \theta, and the \chi_{\theta,1} and \chi_{h,1} can be well chosen to be unramified (and thus there product as well). The point is to use Proposition 7.27.

## Lecture, question par question (email `email_wan.md`)

| Question | Réponse de Wan | Conséquence |
|---|---|---|
| 1. En place décomposée supercuspidale, remplacer (iv) par la condition de FW Cor. 7.28 et prendre le vecteur nouveau ? | **Oui** (« you are right », « the point is to use Proposition 7.27 »). Ce choix est « different from and much easier than the principal series case in my ANT paper » | **Le cas supercuspidal du problème A est confirmé par l'auteur** (communication privée). C'est ce que donnent FW Prop. 7.27 et Cor. 7.28 (démontrés pour tout ℓ au §9 de `probleme_A_note.md`) et la Prop. R′ avec A trivial |
| 2. Lire « conductors ℓ^{t₁} » comme cond(χ₁χ₂^{-1}) = ℓ^{t₁} ? | **Oui** : « the quotients of χ₁/χ₂ have conductor t₁ for h and θ ». De plus, χ_{θ,1} et χ_{h,1} peuvent être pris non ramifiés | Notre lecture est confirmée. L'indice 1 correspond à la composante non ramifiée, ce qui est cohérent avec « χ_{θ,𝔳} unramified » dans CLW (4) |
| 3. Lemme 8.14 / 8.17 (séries principales, Steinberg) et orientation | **Pas de réponse explicite.** Il signale seulement que le cas des séries principales de l'article ANT est différent | **Reste ouvert.** C'est le point qui touche le cas publié (premiers multiplicatifs décomposés, et tordue g_K aux premiers de D_K pour le rang 1) |

## Ce qui change
- **A, cas supercuspidal (≈ 92 % des courbes de la famille en 2, ≈ 29 % en 3) : confirmé par l'auteur.** Le statut passe de « DÉDUCTION » à « confirmé par l'auteur, communication privée ».
- **Le rang 1 dépend toujours du cas « série principale ramifiée »**, via la tordue g_K aux premiers de D_K, c'est-à-dire de la question 3. La borne de 78,6 % reste donc conditionnelle à ce point, à la Prop. R′ et au point N6.
- **Prudence d'interprétation.** « Yes you are right » répond clairement aux questions 1 et 2. On ne peut pas en déduire qu'il valide la Prop. V ou le contre-exemple au Lemme 8.14.
- **Avant de citer sa réponse** dans un document diffusé (« X. Wan, private communication »), il faut lui en demander l'autorisation.

## Projet de relance (courte, en anglais, à envoyer par l'utilisateur)

Subject: Re: Question on split supercuspidal places — thank you, and one follow-up on Lemma 8.17

Dear Professor Wan,

Thank you very much for your clear answer. It confirms the supercuspidal case completely.

May I ask one short follow-up on the principal series and Steinberg case, which matters for the twist g_K in BSTW (primes dividing D_K) and for split multiplicative primes?

Take the vectors of Lemma 8.17 (ANT version): f_{χθ} and f_{χh} as in Lemma 8.13, with t₁ < s and t₂ = t₁ + s (or t₂ = s + 1 if t₁ = 0). Then f_{χθ} ⊗ f_{χh} is a K_0(ϖ^{t₂})-eigenvector of character (χ_{f,1}ϑ)^{-1}(a)(χ_{f,2}ϑ^{-1})^{-1}(d). By invariance of Ichino's integral, I_v only sees the projection of the first vector to the inverse type. In π_f ⊗ (χ_{f,2}ϑ^{-1})^{-1} = π(χ_{f,1}χ_{f,2}^{-1}ϑ, ϑ), which has conductor 2s > t₂, that type does not occur (Casselman). So I_v = 0 for every vector of π_f, unless t₁ = 0 and s = 1.

If this is right, a choice in the spirit of Proposition 7.27 seems to work for every generic π_v. Take φ_v with Kirillov function A^{-1}·1_{O^×} and data with type A(a)A^{-1}(d) on K_{t₁}. Only the identity double coset then contributes, and I_v = Vol(K_{t₁}) is independent of the family (details in the attached note, §3–5).

Is this consistent with what you intended for the principal series case?

Also, would you allow me to mention your answer as a private communication in the note I plan to show to a few colleagues?

With many thanks again,
[your name]

*(Pièce jointe suggérée : `bsd/NEW_RESULTS_EN.pdf`.)*
