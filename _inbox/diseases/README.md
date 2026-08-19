---
title: Diseases — atelier de recherche
status: en cours
created: 2026-08-19
---

# Atelier `diseases/`

Recherche préparatoire pour la future collection `_diseases/` : une fiche éditoriale par grande pathologie, structurée pour montrer les corrélats nutritionnels, les mécanismes, et le geste du diagnostic-écran (le nom qui ferme l'enquête).

## Méthode

Division du travail :
1. **Ici** : formulation des questions, sélection des pathologies, analyse critique des rapports reçus, rédaction éditoriale.
2. **Perplexity Deep Research** : couverture large, sourcing exhaustif, récupération des études et auteurs.
3. **Perig** : lance les requêtes Perplexity, dépose les rapports dans chaque sous-dossier, ajoute ses trouvailles personnelles.

Chaque sous-dossier `<pathologie>/` contient :
- `question.md` — la requête prête à copier dans Perplexity, avec les angles spécifiques à cette pathologie.
- `perplexity-report.md` — le rapport reçu (à déposer par Perig).
- `notes.md` — trouvailles personnelles de Perig, sources qu'il connaît déjà, cliniciens à ne pas oublier.
- `analysis.md` — synthèse critique produite ici après lecture du rapport.

## Pathologies dans ce batch (2026-08-19)

Sélection couvrant les grands tueurs du GBD + les champs où le diagnostic-écran est le plus scandaleux :

1. `cardiovascular-disease/` — le plus lourd du GBD, dossier nutritionnel massif
2. `depression/` — diagnostic-écran par excellence, corps absent de la conversation thérapeutique
3. `anxiety-disorders/` — chaîne cholinergique et parasympathique
4. `type-2-diabetes/` — épicentre de l'insulinorésistance, croisement avec le travail Bikman/Voluntary Famines
5. `cancer/` — générique, à raffiner en cancers spécifiques après premier rapport
6. `cognitive-decline/` — Alzheimer, MCI, démences (angle B vitamines, oméga-3, choline, insulinorésistance cérébrale)
7. `inflammatory-bowel-disease/` — prototype de l'inflammatoire chronique
8. `allergic-atopic-disease/` — asthme, dermatite atopique, rhinite, allergies alimentaires

Candidats pour un batch ultérieur : ostéoporose, MPOC, maladies auto-immunes systémiques, addictions/toxicomanies, thyroïde fonctionnelle, fatigue chronique/fibromyalgie, obésité comme pathologie en soi, autisme.

## Template maître de requête Perplexity

À injecter dans chaque `question.md`, avec la pathologie substituée et les angles spécifiques ajoutés en fin.

```
Contexte : rapport pour un projet éditorial (physiological rights) documentant les liens nutritionnels et physiologiques des grandes pathologies. Audience : cliniciens, juristes, chercheurs. Rigueur méthodologique primordiale, sources primaires préférées. Distinctions association/causalité et mécanisme établi/hypothèse doivent être explicites.

Produire un rapport exhaustif sur [PATHOLOGIE] couvrant :

1. **Fardeau épidémiologique** : GBD récent, prévalence, incidence, mortalité, DALYs, variation géographique (Occident vs. reste du monde), tendances 30 ans.

2. **Corrélats nutritionnels** : pour chaque nutriment ou molécule apparentée (vitamines, minéraux, acides aminés, acides gras, choline, taurine, créatine, CoQ10, glutathion, NAD+, PQQ, etc.) où existe une littérature, associations entre statut (déficit ou suboptimal) et risque, sévérité ou progression. Études de cohorte majeures, méta-analyses observationnelles, tailles d'effet, IC, populations, sources primaires (auteurs, journaux, DOI).

3. **Mécanismes physiologiques** : pour chaque corrélat, voie(s) mécanistique(s) contribuant à la pathologie. Niveau de preuve : cellulaire in vitro, modèle animal, humain in vivo. Distinguer établi vs. spéculatif.

4. **Interventions nutritionnelles** : RCTs et essais non randomisés de supplémentation ou modification nutritionnelle. Résultats, tailles d'effet, critique méthodologique (dose typiquement suffisante vs. sous-dosée, durée, sélection de population, cofacteurs adressés ou non). Distinguer échecs vrais vs. échecs méthodologiques.

5. **Cliniciens et chercheurs de référence** : auteurs contemporains portant la thèse nutritionnelle sur cette pathologie, institutions, laboratoires, publications-clés des 10 dernières années. Successeurs des figures historiques (nommer si figure historique récemment décédée).

6. **Chevauchements sémiologiques** : signes et symptômes de la pathologie qui recoupent des symptômes de carence nutritionnelle connue. Zones où le diagnostic pathologique et le diagnostic de carence peuvent être confondus ou coexister.

7. **Populations à risque particulier** : âge, grossesse, populations captives (EHPAD, prisons, psychiatrie institutionnelle), minorités, revenus, régimes restrictifs, contextes cliniques (post-chirurgie bariatrique, insuffisance rénale, MICI, etc.).

Consignes de style : rapport dense, structuré, sourcé. Sources primaires préférées, méta-analyses acceptables, revues narratives à identifier comme telles. Distinctions explicites association/causalité et mécanisme établi/hypothèse. Ne pas conclure prématurément sur "les preuves sont limitées" : décrire ce qui existe et où sont les zones grises. Exposer les tensions avec le consensus mainstream sans les modérer.
```

## Statut par pathologie

| Pathologie | Question rédigée | Rapport Perplexity | Analyse ici |
|---|---|---|---|
| cardiovascular-disease | ✓ | | |
| depression | ✓ | | |
| anxiety-disorders | ✓ | | |
| type-2-diabetes | ✓ | | |
| cancer | ✓ | | |
| cognitive-decline | ✓ | | |
| inflammatory-bowel-disease | ✓ | | |
| allergic-atopic-disease | ✓ | | |
