# Vérification : magnésium (fiche `_rights/magnesium.md` + DYK sérum + recopies)

Méthode allégée du 2026-11-18 : trois catégories. Erreur dure = corrigée et poussée directement. Portée = proposition, Perig tranche. Style = hors chantier (règles déjà en mémoire). Matériau détaillé de la passe précédente : branche `origin/audit/references-2026-11` (`_audit/references/`).

Sources primaires contrôlées par notices PubMed (E-utilities) / EuropePMC, 2026-11-18.

## 1. Erreurs dures corrigées

| Erreur | Correction | Source vérifiée | Commit |
|---|---|---|---|
| MaGNet 2022 dans *Advances in Nutrition* | *Eur J Nutr* 61(7):3697–3706 | PMID 35689124 | c1e35dc |
| Citation « profoundly deficient » attribuée à MaGNet | Schwalfenberg & Genuis, *Scientifica* 2017:4179326 ; fragment marqué […] | PMC5637834 | c1e35dc |
| « 10 % » daté de 2010, « incidentally » | Whang & Ryder, *JAMA* 1990 ; dosage systématique vs demande, 48/487 | PMID 2342219 | c1e35dc |
| « Half of ICU patients » | Ryzen 1986 : 104 patients USIC, 53 % mMg bas vs 7,7 % sMg bas | PMID 3953355 | c1e35dc |
| Hypertendus « normal or even elevated » | sérum normal (Seelig CB 1990, ≠ Mildred Seelig) | PMID 1695392 | c1e35dc |
| Timeline « 2.4 billion deficient » | « with inadequate intake » | Zhang & Zhao 2025 | c1e35dc |
| Recopie dans `the-hunger-we-dont-see.md` (« MaGNet clinical review ») | Schwalfenberg & Genuis | idem | c1e35dc |
| « 3,571 » protéines | **3 751** (Piovesan 2012) | PMID 23095498 | voir log |
| « 77 % » mort subite attribué aux *apports* | 77 % = Mg **plasmatique** (RR 0,23) ; apports 37 % (RR 0,63), Nurses' Health Study | PMID 21106914 | voir log |
| Méta-analyse >500 000, RR 0,64 | Qu 2013 : 532 979, RR 0,77 sérum / 0,85 apports ; le 0,64 appartient à une autre méta-analyse | PMID 23520480 | voir log |
| Senate Document 264 = « rapport au Sénat » | réimpression d'un article de Rex Beach (*Cosmopolitan*) sur Charles Northen, présentée par le sénateur Fletcher | Monthly Catalog UNT | voir log |

Confirmé tel quel : diabète −15 % par +100 mg/j (Larsson & Wolk 2007, RR 0,85) ; seuil 0,85 mmol/L (recommandation des auteurs) ; 88,6 % (revue clinique, à remonter au primaire).

## 2. Portée : P1–P6 acceptées par Perig le 2026-11-18, appliquées

P5 : citation « All enzymatic reactions involving ATP… » introuvable (EuropePMC, phrase exacte) → convertie en énoncé non cité. P6 : Liebscher & Liebscher 2004 (PMID 15637222) et Costello et al. 2016 (*Adv Nutr*, PMC5105038) vérifiés ; Costello 2016 est probablement l'origine de la confusion « Advances in Nutrition ».

- **P1 — titre DYK « misses more than 99% of it ».** 99 % = compartiment non mesuré, pas taux de faux négatifs. Le titre est défendable (« of it » = du magnésium), mais lu vite il sonne comme une sensibilité. Variante : *« The standard magnesium test measures less than 1% of the body's magnesium »*.
- **P2 — « The recommendation nobody has adopted » / « No major laboratory has updated ».** Le recueil MaGNet lui-même trouve 2 seuils sur 43 déjà à 0,85. Variante plus cinglante et vraie : *« In MaGNet's own survey, 41 of 43 institutional cut-offs were still below 0.85 mmol/L. »*
- **P3 — « a necessary activator for 200 additional enzymes ».** La revue source (Souza 2023) dit « may act as an activator ». Variante : « and may activate 200 more ».
- **P4 — 78 millions / 2,3 milliards d'années.** Chiffres de Wolfenden (OMP décarboxylase, uroporphyrinogène décarboxylase) : exacts, mais ces deux enzymes n'ont justement pas besoin de métal. La phrase suivante (« magnesium is the key… ») laisse croire l'inverse. Variante : garder l'image, ajouter « including the kinases and polymerases that copy DNA, which cannot work without Mg-ATP ».
- **P5 — « This form, and only this form » / citation « All enzymatic reactions involving ATP ».** Absolu défendable pour les kinases, pas pour toute réaction énergétique ; citation à attribuer (actuellement sans auteur).
- **P6 — « challenged by the MaGNet network for a decade / over a decade »** (`behind-every-test-an-industry.md`, `what-the-label-cannot-say.md`). MaGNet publie la recommandation en 2022 ; la proposition 0,85 elle-même remonte à Liebscher & Liebscher (2004) et Elin. Reformuler en « for two decades, from Liebscher and Elin to MaGNet » après vérification de ces deux sources.

## 3. Lot 3 (2026-11-18, appliqué sans aller-retour)

| Point | Verdict | Action |
|---|---|---|
| 88,6 % des diabétiques | une seule étude, n = 210 (cité par Schwalfenberg & Genuis) | portée bornée |
| UK 24/21/38/70 % | Thomas 2007, *Nutr Health* (comparaison McCance & Widdowson) ; chiffres non relus dans le texte intégral | attribution ajoutée |
| Raffinage 82/83/99 % | Marier 1986 ; résumé seulement, chiffres non relus | attribution ajoutée |
| Taub Center « 83–253 M NIS/an » | 83–188 M en 2025, 110–253 M en 2040 ; Sadeh et al. 2024 | horizons séparés |
| « $86 billion » | Paul Mason, cité par Life Extension 2005 ; pas de modèle publié | attribué |
| Citation Durlach « About 20% » | Durlach 2004, *J Am Coll Nutr* (PMID 15637217) | réf. 42 ajoutée |
| Durlach 1925–2017 | confirmé (Rayssiguier, *Magnes Res* 2017;30(4)) | — |
| Scénario Dean | paraphrase présentée en bloc | marqué « paraphrased » |

## 4. Reste ouvert

- « 20 to 40% » de baisse liée aux NPK (réf. commerciales 17, 19) : source primaire non trouvée.
- Préface Seelig (réf. 5, mgwater.com redirige) ; vidéo Rosanoff (réf. 25).
- Tableau des associations par système ; tests alternatifs.
- Réf. 26 = doublon probable de 24.
