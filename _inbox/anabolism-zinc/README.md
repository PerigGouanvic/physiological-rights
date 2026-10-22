# Atelier — Pièce compagnon zinc & anabolisme

**Ouvert** : 2026-08-29 (samedi soir)
**Reprise prévue** : jeudi 2026-09-03 (retour de quota Perig)
**Destination finale** : `_critique/` (pas `_inbox/`) — publication éditoriale directe
**Statut** : matière rassemblée, plan arrêté, à écrire

---

## Origine et enchaînement de la conversation-ruche

Point de départ : Perig s'interroge sur la pertinence des efforts pour prendre des protéines en quantités « phénoménales » pour lui et sa femme, à la lumière de deux pièces récentes (`_critique/one-missing-letter.md` publiée août 2026 sur les sinks d'AA, `_critique/ai-mirror-medical-information-zinc.md` publiée août 2026 sur le silence médical autour du zinc). Diagnostic partagé : le grammage protéique brut ne peut pas atterrir si (1) une ou plusieurs lettres manquent (sinks glycine/cystéine/méthionine) et (2) la machinerie anabolique en aval est éteinte faute de zinc fonctionnel, de fer pour la conversion T4→T3, de sensibilité insulinique, etc.

Deuxième temps : Perig identifie que la pièce zinc actuelle (*AI as Mirror*) est forte sur la sémiologie du silence et l'inflammaging, mais **faible sur la démonstration clinique positive côté anabolisme**. Il rappelle que le corpus zinc grand public est saturé côté inflammation/cicatrisation (pâte d'Ihle, rhume, etc.), et veut défricher le versant strictement anabolique en profondeur.

Troisième temps : décision de compagnon publié séparément, dédié anabolisme uniquement. Deux tours de Deep Research Perplexity :
1. Rapport mécanistique (rapport 1 ci-dessous) — solide mais faible côté clinique.
2. Rapport essais cliniques humains (rapport 2 ci-dessous) — comble le trou.

Perig arrête sa session pour préserver son quota. Ce README garde la ruche jusqu'à jeudi.

---

## Matière disponible dans ce dossier

- `2026-08-29-perplexity-rapport-1-mecanismes.md` — mécanismes moléculaires (mTOR direct McClung, IGF-1, zinc fingers AR, Prasad 1996, Ai 1997, myogenèse, insuline, KLF15/KLF5, bariatrie, cachexie).
- `2026-08-29-perplexity-rapport-2-essais-cliniques.md` — essais humains (Rodondi 2009 pivot, ZENITH nul chez sufficient, hémodialyse +1,02 kg sous-groupe, cirrhose, BPCO Gouzi, ZIP14 cachexie cancer, silences documentés).
- `2026-08-29-prompt-deep-research-1.md` — prompt du premier tour, pour traçabilité méthodologique.
- `2026-08-29-prompt-deep-research-2.md` — prompt du second tour (rattrapage clinique).

Pièces publiées à articuler avec le compagnon :
- `../../_critique/ai-mirror-medical-information-zinc.md` (mère, sur laquelle greffer le compagnon)
- `../../_critique/one-missing-letter.md` (sœur sur les sinks d'AA, à référencer)
- `../../_critique/the-workup-they-do-not-order.md` (récente, sur l'asymétrie médicale du workup)

---

## Plan de la pièce compagnon (arrêté 2026-08-29)

**Titre candidat** : *Zinc When Given* (à raffiner). Alternatives : *What Happens When the Mineral Is Restored*, *The Anabolism That Waits on One Mineral*.

**Cadrage** : la pièce mère (*AI as Mirror*) démonte le silence. Ce compagnon documente ce qui se passe **quand un clinicien décide de donner du zinc à la population qui en manque**. Ni catalogue triomphaliste ni contre-catalogue défaitiste. Trois mouvements + un mouvement-silence en clôture.

### Mouvement I — Ce que le zinc fait quand on le donne à la bonne population

Piliers cliniques positifs, chacun développé avec chiffres précis :

1. **Prasad, Mantzoros, Beck, Hess, Brewer 1996, *Nutrition* 12:344-348**. Jeunes hommes en restriction zinc 20 semaines : testostérone de 39,9 → 10,6 nmol/L. Âgés 64±9 ans marginalement déficients, 30-40 mg/j 3-6 mois : testostérone de 8,3 → 16,0 nmol/L. Effet-seuil : rien chez suffisants. Retour à baseline en 12 semaines de réplétion.

2. **Rodondi et al. 2009, *JNHA* — pivot du compagnon**. 61 hospitalisés fragiles 66-105 ans, MNA 17-24. EAA-lactosérum + 30 mg zinc vs EAA-lactosérum seul, 4 semaines, double aveugle. IGF-1 : **+48,2 % vs +22,4 %** dès la 1re semaine (p<0,05). ADL : +27 % vs +18 %. Résorption osseuse abaissée. Synergie zinc×protéine sur marqueur anabolique endocrinien direct chez la population exactement pertinente pour la sarcopénie et pour la femme de Perig.

3. **Hémodialyse : méta-analyse 27 RCT sur composition corporelle**. Effet global nul, MAIS sous-groupe hémodialysés +1,02 kg vs placebo. Exemple numérique canonique de l'écrasement du signal par agrégation de populations hétérogènes.

4. **Cirrhose hépatique**. Essai zinc sulfate 50 mg/j double aveugle chez 60 cirrhotiques : amélioration masse musculaire, encéphalopathie, statut clinique. Crampes musculaires résolues chez 7/12 cirrhotiques hypozincémiques sous 220 mg zinc sulfate x2/j. BCAA + zinc synergiques chez 32 sarcopéniques cirrhotiques.

### Mouvement II — Pourquoi la physiologie l'explique (émerveillement)

5. **mTOR activé directement par le zinc**. McClung et al. USARIEM (PubMed 17848732). Phosphorylation p70S6K, GSK-3, Akt(Ser473) 6h après réplétion, indépendamment des acides aminés et de l'insuline. Le mineral est une instruction anabolique de premier ordre, pas un simple cofacteur.

6. **Zinc fingers du récepteur des androgènes**. Deux doigts coordonnés chacun par quatre cystéines. Boîte P (résidus 577-582, séquence GSCKV) touche l'ADN, boîte D dimérise le récepteur. **Sans zinc coordonné, ni liaison ADN ni dimérisation.** Toute la transcription androgénique musculaire dépend structurellement de la disponibilité du zinc au bon endroit au bon moment. Architecture partagée avec récepteurs des glucocorticoïdes, progestérone, minéralocorticoïde, vitamine D, thyroïde. Registre d'émerveillement pur.

7. **Ai, Chen, He 1997 (Wei Sheng Yan Jiu) — résultat en négatif révélateur**. Chez rat carencé zinc, la testostérone exogène **n'a aucun effet favorable** sur poids musculaire, ARN musculaire, force. En plus, **inhibe** la synthèse endogène de T. Conclusion des auteurs : le déficit anabolique n'est pas lié au niveau bas de T dans la carence zinc. Le zinc agit sur l'anabolisme par une voie indépendante de la T circulante — probablement via mTOR direct et/ou via l'occupation fonctionnelle du récepteur AR zinc-dépendante. **Message qui tranche dans une culture qui vend la T comme la clef anabolique unique.**

Angle éditorial pour ce mouvement : décrire avec émerveillement combien le zinc est structurellement inséré dans la machinerie anabolique. Les zinc fingers sont un des plus beaux motifs de la biologie moléculaire. Perig veut ce ton (voir memory `project_editorial_pivot_vitriol_wonder`).

### Mouvement III — Pourquoi la simplicité serait trompeuse (nuance anti-hagiographie)

8. **KLF15 et KLF5 : facteurs à zinc finger qui pilotent l'ATROPHIE, pas l'anabolisme**. KLF15 induit par l'immobilisation via Piezo1↓ → IL-6 → atrophie ; délétion muscle-spécifique protège (JCI 2021). KLF5 induit par dexaméthasone/microgravité → protéolyse ubiquitine ; délétion sélective atténue atrophie induite par déchargement. Certains effecteurs zinc-dépendants pilotent la dégradation musculaire selon contexte hormonal et mécanique.

9. **ZIP14 en cachexie cancéreuse métastatique : le zinc accumulé pathologiquement dans le muscle accélère l'atrophie**. Modèle murin, PubMed via PMC6015555. Chez patient cancéreux à zinc sérique bas, la supplémentation réflexe n'est pas sans risque. Contre-signal important qui empêche la lecture linéaire « plus de zinc = plus d'anabolisme ».

10. **ZENITH (108 Italiens 70-85 ans, 6 mois) et ZMA (Wilborn 42 hommes entraînés, 8 semaines) : nul chez zinc-sufficient**. Ces résultats négatifs ne réfutent pas le zinc, ils réfutent l'usage indiscriminé. La théorie du seuil-fonction les prédit.

### Mouvement IV — Ce que la médecine s'est abstenue de mesurer (silences documentés)

11. **Aucun essai MPS isotopique + zinc**. Toute la méthodologie est mature depuis Rennie/Halliday/Millward, validée D2O Wilkinson/Smith. La technique existe. La question n'a jamais été posée pour le zinc. Angle mort complet.

12. **Anabolic resistance jamais testée avec zinc comme variable**. Groupes van Loon, Phillips, Rennie, Volpi, Paddon-Jones ont caractérisé la résistance anabolique postprandiale de la personne âgée par la dose protéique, la leucine, l'exercice. Le zinc n'apparaît pas dans leurs protocoles. C'est un choix, pas un oubli.

13. **Post-bariatrie : population candidate idéale, aucun essai zinc vs placebo avec DEXA en critère primaire**. Déplétion documentée 24-74 % selon procédure, perte de masse maigre concomitante rapide et sévère. La combinaison est là, l'essai n'est pas fait. « Workup they do not order » appliqué à la masse maigre.

Ligne de clôture : le compagnon nomme ce que la pièce mère ne pouvait dire. Le zinc, quand il est donné à qui en manque, débloque des choses mesurables et rapides. Quand la question n'est pas posée, la réponse est absente par construction. Le silence de la littérature clinique sur l'anabolisme-zinc n'est pas un défaut de preuve, c'est un défaut de demande.

---

## Contraintes de style (rappel des memories)

- **Français à Perig, anglais dans le texte publié.**
- **Vitriol + émerveillement combinés** (`project_editorial_pivot_vitriol_wonder`). Ton polémique frontal ET émerveillement biologique. Lectorat élargi (juristes + éthique + population).
- **Mordre, ne pas plaindre** (`feedback_bite_dont_lament`). Cible = le dispositif, pas les personnes.
- **Zéro em-dash** (`feedback_no_em_dashes`). Virgule, deux-points, parenthèses, phrase séparée.
- **Bannir « what this changes », « the takeaway », « key insight », « precise »** (`feedback_no_ai_meta_framing`, `feedback_no_word_precise`).
- **Varier longueur de phrases**, éviter staccato (`feedback_vary_sentence_length`).
- **Faire confiance à l'implicite** (`feedback_trust_the_implicit`). Pas de « not X but Y » décoratif.
- **Logique de droits, pas d'attribution pharmacologique individuelle** (`feedback_rights_logic_not_pharmaco_attribution`).

## Positionnement dans la resource

- Frontmatter `related` doit lister au minimum : *AI as Mirror*, *One Missing Letter*, *The Workup They Do Not Order*, *Right to Optimal Hormonal Levels*, *Right to Adequate Muscle Mass*.
- Ajouter en fin de *AI as Mirror* un renvoi obligatoire vers ce compagnon quand publié.
- Statut `published` direct, commit + push (règle `feedback_publish_dont_draft`).

## À vérifier au moment d'écrire

- Ref [14] du rapport 1 (myhealthcare.com) : remonter à la source primaire Prasad 1996 pour citation.
- Ref [18] du rapport 1 (PDF japonais researchmap.jp) : validité et paternité.
- Vérifier ClinicalTrials.gov pour les deux essais zinc-insuffisance cardiaque signalés en 2020 comme complétés, résultats non trouvés (biais de publication potentiel à documenter dans le compagnon).
- Confirmer que Rodondi et al. 2009 est bien la référence : PubMed 19536417.
- Chercher si Ito et al. gériatrique japonais existe vraiment (le rapport 2 dit non, prompt 1 le mentionnait comme piste).
