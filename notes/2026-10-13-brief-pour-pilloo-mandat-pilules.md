# Brief pour Pilloo — mandat premier d'aide à la prise de pilules

**Date** : 2026-10-13
**Émetteur** : agent physiological-rights
**Destinataire** : agent pilloo (conversation à 3 avec Perig)
**Portée** : ce que physiological-rights apporte au mandat opérationnel de base de Pilloo, pas la fonctionnalité micro ni l'écosystème de nuages ni la renaissance conceptuelle.

---

## 1. L'usager concret

Perig n'est pas un profil naïf. Il travaille dans un cadre orthomoléculaire, lecteur de la recherche primaire depuis longtemps, posture épistémique étayée dans `~/projects/physiological-rights/CLAUDE.md`.

Ligne de base supplémentation complète : [`user_supplementation_baseline.md`](~/perig-travail/.claude/projects/-home-perig-projects-physiological-rights/memory/user_supplementation_baseline.md) (inventaire 2026-10-13). À lire *avant* toute suggestion. Ce qu'il prend régulièrement :

- Socle antioxydant / minéral : ascorbate K potion sirotée (~3-4 g K/jour quand pas oublié), acide ascorbique poudre, Mg, NAC, sélénium, CoQ10 ubiquinol, oméga-3, D3, K2 MK-7.
- B et méthylation : méthylcobalamine sublinguale, 5-MTHF, Thiamega, Benfotiamine, TMG.
- Mitochondrie : créatine, NMN, ALA.
- Choline (foie, cerveau, parasympathique) + reste CDP-choline.
- Immunité / tabac / AA : whey (précurseur GSH), collagène (glycine), AA essentiels, leucine, arginine.
- Herbes : Cold FX, Ginkgo, curcuma, fenugrec, SOD cantaloup.
- Autres : citrate de zinc, metamucil, GABA, fer (en réserve), psilocybine microdose.
- Médicaments : testostérone (hypogonadisme compensé, sous ordonnance), ramipril.

Trous identifiés dans le contexte tabac + fatigue (à discuter, pas à injecter d'office) : vit E mixed tocophérols/tocotrienols, quercétine, astaxanthine, B-complex méthylé, ALCAR, cuivre 2 mg, glycine en poudre pour protocole GlyNAC.

## 2. Posologie — ce qu'il faut savoir

**Doses de travail orthomoléculaires**, pas les RDA. Référence : [`feedback_no_conservative_dosages.md`](~/perig-travail/.claude/projects/-home-perig-projects-physiological-rights/memory/feedback_no_conservative_dosages.md). Ordres de grandeur : vit D 10-20k UI, zinc 30-50 mg, NAC 1800-2400 mg, vit C en dizaines de g épisodiquement.

Vit C mégadose = savoir installé depuis 2003, pas pratique exploratoire. Ne pas expliquer la bowel tolerance comme s'il la découvrait.

## 3. Registre partagé — points d'articulation avec ton mandat

Physiological-rights pose les compléments comme des **droits**, pas des prescriptions. Pilloo porte la même logique côté geste : rappeler sans chantage, pharmacie-bien-être pas pharmacie-médicament, oubli absorbé sans reproche. Les deux cadres se répondent.

Articulations opérationnelles pour la conversation à 3 :

- **Fréquence et contexte de prise**. Perig a des molécules à logique variée : certaines quotidiennes stables (D3, K2, Mg), certaines à distribuer dans la journée (K-ascorbate sirotée), certaines épisodiques à la demande (vit C mégadose selon inflammation), certaines à cycler (fer en réserve). Un seul rythme ne couvre pas tout.
- **Interactions temporelles**. Fer et calcium s'opposent à l'absorption, les liposolubles veulent du gras, le zinc à jeun ou pas selon tolérance, méthylcobalamine sublinguale pas en même temps que boisson chaude. Pilloo peut porter ces micro-indications sans devenir pilulier médical.
- **Oublis et manques**. La potion K est le fil rouge connu : les jours d'oubli, le trou s'ouvre. Pilloo peut rendre visible ce trou spécifique sans culpabiliser.
- **Co-prises avec sa femme**. Contexte famille, budget contraint ([`user_budget_constraint_supplements.md`](~/perig-travail/.claude/projects/-home-perig-projects-physiological-rights/memory/user_budget_constraint_supplements.md)). Pilloo gère un usager, pas deux, mais le contexte familial pèse sur ce qui est pris.

## 4. Ce que physiological-rights NE demande PAS à Pilloo

- Pas de posologie prescriptive. Les doses de travail sont un cadre de référence, pas un ordre.
- Pas d'alerte anxiogène sur l'oubli. L'oubli est un signal, pas une faute.
- Pas de contenu éducatif généré par LLM en live sur le tama. Le corpus éducatif passe par le circuit curé (`_did-you-know/` côté physiological-rights alimente le futur corpus Pilloo).
- Pas de surveillance biographique transformée en dossier médical. La trace reste nourricière.

## 5. Questions ouvertes à travailler à 3

- **Quel sous-ensemble de la pharmacopée Perig** veut-il réellement voir rappelé par Pilloo ? Tout, ou seulement ce qu'il oublie structurellement (hypothèse K-ascorbate) ?
- **Comment Pilloo apprend-il** l'inventaire de Perig sans dupliquer la ligne de base déjà portée par physiological-rights ? Partage de fichier, saisie initiale, import ?
- **Quelle granularité temporelle** pour la K-ascorbate sirotée ? Rappel toutes les 2h, ou présence passive du tama qui signale la décroissance de la bouteille ?
- **Que fait Pilloo quand Perig prend une mégadose vit C ponctuelle** (épisode inflammatoire) ? Il l'enregistre comme événement, il ne le rappelle pas comme routine.

---

**Pointeurs utiles pour l'agent pilloo** :
- `~/projects/physiological-rights/CLAUDE.md` — posture épistémique du projet
- `~/perig-travail/.claude/projects/-home-perig-projects-physiological-rights/memory/MEMORY.md` — index des mémoires
- `~/projects/physiological-rights/_rights/` — fiches par nutriment (modèle `magnesium.md`)
- `~/projects/physiological-rights/_did-you-know/` — collection destinée à alimenter le corpus Pilloo
