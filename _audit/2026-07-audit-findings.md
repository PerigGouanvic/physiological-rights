---
title: Constats d'audit — juillet 2026
status: internal
created: 2026-07-24
last_revised: 2026-07-27
scope: constats issus de la passe AUDIT-CHARTER (Sections 1–3)
---

# Constats d'audit — juillet 2026

Une seule liste numérotée. Constats seulement, aucune correction appliquée. Chaque item suit le gabarit de AUDIT-CHARTER Section 4, adapté pour un vote rapide sur mobile.

## Comment voter

Chaque constat porte une ligne `Verdict :` avec cinq cases. Deux façons de te prononcer :

1. **Dans GitHub sur mobile.** Bouton crayon en haut à droite du fichier, coche la case, puis « Commit changes ». Les cases `- [ ]` sont cliquables sur les fichiers dont tu es propriétaire.
2. **Dans notre conversation.** Réponds-moi item par item : « 1 : OK ; 2 : Non ; 3 : À discuter parce que… ». Je reporterai les votes dans le fichier au commit suivant.

**Verdicts disponibles :**

- `[ ] OK` — à corriger dans la session de correction qui suivra.
- `[ ] Plus tard` — retenu, mais pas prioritaire ; à ressortir plus tard.
- `[ ] Non` — rejeté. J'ajouterai un marqueur `REJETÉ (raison)` pour que la prochaine passe d'audit ne relance pas.
- `[ ] À discuter` — décision suspendue, on en parle en session.
- `[ ] Déjà fait` — corrigé entre l'écriture du constat et ta lecture (rare, mais possible sur un dépôt qui bouge).

**Options secondaires à noter dans la ligne _Notes_ si utile :** « À découper » (le constat regroupe plusieurs corrections distinctes) ; « Reformuler » (l'idée est bonne mais la formulation ne convient pas) ; « Déléguer à un juriste » ou « à un clinicien » (nécessite un regard extérieur avant décision).

## Notes de méthode

Tous les liens markdown internes du corpus ont été vérifiés contre les permaliens de collections déclarés dans `_config.yml` : 0 lien cassé sur 174 vérifiés. Les références Liquid dans `_layouts/`, `_includes/`, `index.md` et les index de section ont aussi été résolues : 0 non-résolu. Seuils numériques vérifiés par échantillon (thiamine 400× RDA, paliers ferritine 15/30/50, GC14 §43, Alma-Ata IV/VII, Oviedo art. 5) : tous traçables. Calques francophones dans le contenu publié : aucun n'a émergé.

---

## Constats structurels (Charte §1 — cousins observés, et §2 — prévisibles)

### 1. `_rights/optimal-hormonal-levels.md` est un stub, référencé comme s'il faisait autorité

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_rights/optimal-hormonal-levels.md` (fichier entier) ; référencé depuis `faq/index.md:89` comme l'un des douze substrats, et depuis l'index des Rights.
- **Nature :** La page est `status: draft`, fait 47 lignes, contient cinq sections courtes (Thyroid, Sex, Adrenal, Insulin, Individual physiology), et ne porte pas les champs de frontmatter `name:` / `category:` / `researchers:` présents sur les onze autres fiches `_rights/`. Il lui manque aussi la section historique, la section chercheurs référents, le tableau des maladies associées, la timeline, et la bibliographie que fournit le gabarit de référence (`_rights/magnesium.md`). Or la FAQ, dans sa réponse à « Which nutrients are documented here? », la nomme parmi les douze substrats documentés.
- **Correction proposée :** Soit hisser la page au gabarit (historique, chercheurs, critique du test, mécanisme, maladies associées, timeline, bibliographie) ; soit la retirer de la revendication des « twelve substrates » dans la FAQ et de l'index Rights tant qu'elle n'est pas conforme. Si maintenue en draft, ajouter `search_exclude: true` pour que `search.json` ne la remonte pas.
- **Priorité :** haute
- **Dépend de :** —

_Notes :_

### 2. Onze fiches `_rights/` sur douze ne renvoient pas à la définition-mère

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_rights/` — tous les fichiers sauf `choline.md`.
- **Nature :** Le constat #2 de la charte (recency bias dans la sélection de liens) a un cousin structurel : seul `_rights/choline.md` renvoie à `/definitions/physiological-rights/`. Un lecteur qui arrive sur une fiche nutriment via la recherche n'a pas de chemin en un clic vers la définition de « droit » telle que la ressource l'entend. La charte §2, item 5 le prédit exactement.
- **Correction proposée :** Ajouter un lien unique (dans le paragraphe d'ouverture ou dans un pied « See also ») vers `/definitions/physiological-rights/` sur chacune des onze pages.
- **Priorité :** moyenne
- **Dépend de :** —

_Notes :_

### 3. `_rights/vitamin-e.md` porte un `status: documented` non standard

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_rights/vitamin-e.md`, frontmatter.
- **Nature :** Toutes les autres fiches `_rights/` conformes au gabarit utilisent `status: published`. `vitamin-e.md` utilise `status: documented`, valeur qui n'est employée nulle part ailleurs dans `_rights/`. La même valeur non standard apparaît sur `_resources/01f26f96.md` (Mayer 1979), où elle peut se défendre pour un document-source ; sur une fiche `_rights/`, elle passe pour un oubli.
- **Correction proposée :** Passer `status: documented` à `status: published` sur `_rights/vitamin-e.md`. Décider séparément si `documented` reste une valeur admise dans le vocabulaire pour les documents-source ; sinon, harmoniser aussi `01f26f96.md`.
- **Priorité :** basse
- **Dépend de :** —

_Notes :_

### 4. Le gabarit de référence `_rights/magnesium.md` porte `last_revised: April 2025`

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** frontmatter de `_rights/magnesium.md`, et par extension chaque fiche `_rights/` qui lit encore `last_revised: April 2025` : `potassium.md`, `iron.md`, `folate.md`, `omega-3.md`, `riboflavin-b2.md`, `thiamine-b1.md`, `vitamin-e.md`.
- **Nature :** Ces pages ont été touchées substantiellement pendant le travail éditorial de 2026 (pivot juriste, cross-linking, ajustements de citations), mais leur `last_revised` lit toujours *April 2025*. Signal trompeur pour le lecteur qui scanne la date pour jauger la fraîcheur. La charte §2, item 9 le prédit exactement.
- **Correction proposée :** Pour chaque page, si la dernière édition substantielle est postérieure à avril 2025, mettre à jour `last_revised`. Là où la page est réellement inchangée depuis avril 2025, garder la date et consigner la décision.
- **Priorité :** moyenne
- **Dépend de :** —

_Notes :_

### 5. La collection `_reports/` est orpheline dans l'architecture actuelle

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_reports/hypothyroidism.md`, `_reports/magnesium-deficiency.md`, `_reports/vitamin-d-deficiency.md`.
- **Nature :** Les trois rapports sont `last_revised: April 2025`, courts, et non liés depuis la FAQ, la page d'accueil ou l'index des Rights. `CLAUDE.md` subordonne explicitement `_reports/` à `_rights/` (un `_reports/<nutriment>-deficiency.md` « ne remplace pas `_rights/<nutriment>.md` »), mais le corpus actuel a fait grossir les fiches `_rights/` sans jamais câbler les rapports dedans. La collection est publiquement indexée par `search.json` mais n'a pas de fonction éditoriale.
- **Correction proposée :** Trancher le sort de la collection. Soit (a) hisser chaque rapport en compagnon cas-oriented de la fiche `_rights/` correspondante et les lier depuis là ; soit (b) retirer la collection (`search_exclude: true` sur chaque fichier, et à terme suppression). L'état intermédiaire actuel est le constat.
- **Priorité :** moyenne
- **Dépend de :** —

_Notes :_

### 6. Trois pages `_resources/` sont des stubs `status: draft` indexés comme publiés

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_resources/legal-texts.md`, `_resources/international-recommendations.md`, `_resources/thematic-bibliography.md`.
- **Nature :** Chacune est un stub avec titre et note seulement. Les trois sont liées depuis la FAQ (`faq/index.md:121–122` lie `legal-texts` et `international-recommendations` ; la bibliographie thématique est liée depuis plusieurs bibliographies `_rights/`). Un lecteur qui clique arrive sur une page vide. Elles sont aussi indexées par `search.json` puisque ni `hidden` ni `search_exclude` n'y sont posés.
- **Correction proposée :** Soit les compléter (peupler la bibliographie thématique, lister les textes légaux et recommandations avec citations et liens) ; soit ajouter `search_exclude: true` et retirer les liens FAQ tant qu'elles ne sont pas peuplées.
- **Priorité :** moyenne
- **Dépend de :** —

_Notes :_

### 7. Deux pages `_legal/` sont des stubs

Verdict : [x] OK (mention légale)  [x] Plus tard (accessibilité, voir #24)  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_legal/legal-notice.md`, `_legal/accessibility.md`.
- **Nature :** Les deux fichiers existent sans frontmatter `status` et ne contiennent qu'un texte de remplacement. Une ressource qui argumente pour un cadre fondé sur les droits et qui se présente sur la force de sa propre conformité déclarative ne devrait pas tourner avec une mention légale vide et une déclaration d'accessibilité vide.
- **Correction proposée :** Peupler la mention légale (identité de l'éditeur, hébergeur, contact, licence du contenu, transparence de financement s'il y a lieu) et la déclaration d'accessibilité (cible de conformité, limites connues, contact pour remédiation). Ajouter `status: published` et `last_revised` une fois peuplées.
- **Priorité :** moyenne (mention légale), basse (accessibilité, si la ressource reste un travail de bénévolat mono-auteur)
- **Dépend de :** —

_Notes :_ Mention légale peuplée : éditeur Perig Gouanvic en clair (à réviser plus tard s'il y a lieu), email `perig.gouanvic@gmail.com` direct (pas encore de redirection sur domaine perso), hébergeur GitHub Pages, licence CC BY-SA 4.0, déclaration d'indépendance de financement, juridiction Québec. L'accessibilité reste à peupler après la passe technique de #24.

### 8. `_critique/practical-illustrations.md` est un stub `status: draft`

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_critique/practical-illustrations.md`.
- **Nature :** Le fichier est un stub. Indexé par `search.json` mais non lié depuis aucune page publiée.
- **Correction proposée :** Soit écrire la pièce (illustrations multi-nutriments par cas, si l'intention tient toujours) ; soit supprimer le fichier ; soit poser `search_exclude: true` en attendant.
- **Priorité :** basse
- **Dépend de :** —

_Notes :_

## Frontmatter et métadonnées

### 9. Page d'accueil et page About n'ont ni `status` ni `last_revised`

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `index.md`, `about/index.md`.
- **Nature :** Les deux sont effectivement des pages « publiées » de porte d'entrée, mais elles ne portent ni `status` ni `last_revised`. Elles échappent donc aux conventions de frontmatter que suit le reste du corpus. Un audit futur ou un contributeur ne peut pas savoir, à partir du seul frontmatter, quand la sélection « Recent additions » de l'accueil a été mise à jour pour la dernière fois.
- **Correction proposée :** Ajouter `status: published` et `last_revised` aux deux fichiers. Mettre à jour `last_revised` chaque fois que la sélection éditoriale de l'accueil bouge.
- **Priorité :** basse
- **Dépend de :** —

_Notes :_

### 10. `_definitions/physiological-rights.md` porte `last_revised: April 2026`

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** frontmatter de `_definitions/physiological-rights.md`.
- **Nature :** La définition-mère de la ressource est datée de trois mois avant le pivot juriste du 20 juillet 2026. Si elle a depuis été relue à l'aune de ce pivot et jugée toujours adéquate, la date devrait refléter cette passe. Si elle n'a pas été relue, c'est en soi un constat : la définition mérite d'être réexaminée contre le cadre juriste que la ressource a adopté.
- **Correction proposée :** Relire contre le pivot juriste (voir mémoire projet `project_pivot_jurist_audience.md`). Soit confirmer et rafraîchir la date ; soit éditer les passages qui sous-serviraient un juriste arrivant à froid.
- **Priorité :** moyenne
- **Dépend de :** 14

_Notes :_

### 11. `search.json` indexe les drafts et les stubs

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** template `search.json` (racine) ; déclenché par chaque fichier qui n'a pas `search_exclude: true` tout en étant `status: draft` ou stub.
- **Nature :** La boucle Liquid dans `search.json` pousse tout document qui n'est ni `hidden` ni `search_exclude`. Les stubs et drafts (`_resources/legal-texts.md`, `_resources/international-recommendations.md`, `_resources/thematic-bibliography.md`, `_critique/practical-illustrations.md`, `_rights/optimal-hormonal-levels.md`) sont donc remontés dans la boîte de recherche du header.
- **Correction proposée :** Ajouter `search_exclude: true` à chaque page draft ou stub tant qu'elle n'est pas complétée ; ou les compléter.
- **Priorité :** basse
- **Dépend de :** 1, 6, 8

_Notes :_

## Lexique (Charte §1, constat #3, et §2, item 10)

### 12. Passe em-dash : 550 occurrences dans le contenu publié

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** transversal. Top des occurrences par fichier : `_rights/vitamin-e.md` (52), `_rights/magnesium.md` (48), `_rights/folate.md` (44), `_critique/behind-every-test-an-industry.md` (44), `_rights/potassium.md` (40), `_rights/omega-3.md` (37), `_critique/the-hunger-we-dont-see.md` (27), `_editorials/the-life-we-call-normal.md` (25), `_rights/riboflavin-b2.md` (20). Tous les autres fichiers sous 20.
- **Nature :** La mémoire `feedback_no_em_dashes.md` est sans ambiguïté : zéro em-dash dans le texte que j'écris. La règle a été formalisée pendant juillet 2026 ; le contenu antérieur en contient encore. 550 occurrences dans 35 fichiers, c'est l'inventaire actuel.
- **Correction proposée :** Passe dédiée. Pour chaque occurrence, remplacer par virgule, deux-points, parenthèses, ou coupure de phrase, selon ce que la phrase fait réellement. Un regex de remplacement en masse est risqué : le choix du remplacement dépend du contexte.
- **Priorité :** moyenne (cosmétique en volume ; change le signal de voix, pas l'argument)
- **Dépend de :** —

_Notes :_

### 13. Passe « precise / precisely / more precise »

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_rights/riboflavin-b2.md:18`, `_rights/potassium.md:193`, `_rights/folate.md:165`, `_rights/omega-3.md:43`, `_rights/iron.md:55`, `_editorials/the-life-we-call-normal.md:26,31`, `_editorials/the-ferritin-threshold.md:33`, `_critique/behind-every-test-an-industry.md:161`, `_critique/false-negative-serum-potassium.md:19`, `_critique/calibrated-for-nothing.md:41`.
- **Nature :** La mémoire `feedback_no_word_precise.md` bannit le mot comme intensificateur vide et tic d'auto-satisfaction IA. Onze occurrences dans neuf fichiers publiés.
- **Correction proposée :** Pour chaque occurrence, soit supprimer le mot, soit le remplacer par le nom ou l'adjectif spécifique que la phrase cherche. Si la phrase s'effondre sans « precisely », c'est que la phrase faisait le travail du tic.
- **Priorité :** moyenne
- **Dépend de :** —

_Notes :_

### 14. « The point is that … is not X but Y » dans the-life-we-call-normal

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_editorials/the-life-we-call-normal.md:61`.
- **Nature :** Deux patterns bannis dans la même phrase : le méta-cadrage « The point is … » (voisin de la famille bannie « What this changes / means / matters ») et le décoratif « not X but Y » (mémoire `feedback_trust_the_implicit.md`). Le reste de la pièce est par ailleurs cohérent en voix.
- **Correction proposée :** Réécrire la phrase pour énoncer le point directement.
- **Priorité :** basse
- **Dépend de :** —

_Notes :_

## Alignement pivot juriste (Charte §2, item 8)

### 15. Vieux `_editorials/` encore calibrés pour le lecteur généraliste d'avant le pivot

Verdict : [x] OK (partiel, voir Notes)  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_editorials/deficiency-as-rights-violation.md`, `_editorials/the-invisible-medical-emergency.md`, `_editorials/ethical-limits-of-rcts.md`, `_editorials/proposed-reforms.md` (tous `last_revised: April 2025`).
- **Nature :** Ces pièces précèdent le pivot du 20 juillet 2026 vers un lectorat juriste (mémoire `project_pivot_jurist_audience.md`). Leur registre est militant-généraliste plutôt que juriste-orienté ; par exemple, `deficiency-as-rights-violation.md` ouvre sur l'assertion que « human rights are … absolute » sans qualification, ce qu'un lecteur juriste va rejeter avant de continuer sa lecture. La charte est claire : ne pas récrire pendant l'audit ; le constat est qu'il faut des pièces-ponts ou une reprise en session dédiée.
- **Correction proposée :** Signalement seulement. En session ultérieure, soit ajouter un cadrage juriste en tête de chaque pièce, soit écrire des éditoriaux-ponts qui routent le lecteur juriste autour.
- **Priorité :** moyenne
- **Dépend de :** —

_Notes :_ Session 2026-07-27. Traitement en trois temps. (a) `deficiency-as-rights-violation.md` réécrit contre GC14 §43 (voir #16). (b) `proposed-reforms.md` caché (`status: draft`, `hidden: true`, `search_exclude: true`) : programme normatif sans doctrine, `a-litigation-brief.md` fait le même travail proprement. Filtres `hidden` ajoutés à `editorials/index.md` et `llms.txt`. (c) `the-invisible-medical-emergency.md` et `ethical-limits-of-rcts.md` restent à raccrocher aux instruments (GC14 §43 + Alma-Ata pour l'un ; Nuremberg + Helsinki §33 + principe de précaution TFUE art. 191 pour l'autre) ; laissés en l'état, à reprendre en session dédiée.

### 16. `deficiency-as-rights-violation.md` : cadrage absolutiste qui va se faire rejeter par un juriste

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_editorials/deficiency-as-rights-violation.md` (section d'ouverture).
- **Nature :** La pièce affirme que les droits humains sont absolus dans un registre qu'un lecteur juriste formé au droit ECHR / ICCPR / ICESCR va traiter comme inexact pour les droits socio-économiques (qui sont de réalisation progressive, sous condition de moyens maximums disponibles selon l'article 2 ICESCR). Ce cadrage active la méfiance juriste dès la porte d'entrée.
- **Correction proposée :** Introduire la distinction entre droits civils-et-politiques (largement absolus) et droits économiques-sociaux-culturels (progressifs), et situer l'argument des droits physiologiques en conséquence. Ou récrire l'ouverture dans le registre de la General Comment 14 (que la ressource utilise déjà correctement dans `_definitions/`).
- **Priorité :** moyenne
- **Dépend de :** 15

_Notes :_ Session 2026-07-27. Réécrit contre GC14 §43 (core obligations), ICESCR art. 2 (réalisation progressive nommée explicitement), obligation de moyens vs obligation de résultats. Ouverture absolutiste retirée. Cross-links ajoutés vers `calibrated-for-nothing`, `false-negative-serum-potassium`, `the-instruments-already-exist`, `a-litigation-brief`. Reformulation « refuses to provide » remplacée par « architectural blindness of the standard of care ».

## Glissements association → causation (Charte §3, item 15)

### 17. Tableaux « associated conditions » dans `_rights/` : audit du dérapage causal

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_rights/magnesium.md` (section maladies associées), et sections équivalentes de `_rights/potassium.md`, `_rights/iron.md`, `_rights/folate.md`, `_rights/riboflavin-b2.md`, `_rights/thiamine-b1.md`, `_rights/vitamin-e.md`, `_rights/omega-3.md`, `_rights/choline.md`, `_rights/glutathione.md`, `_rights/coenzyme-q10.md`.
- **Nature :** Le constat #1 de la charte (cas palpitations / potassium) a des cousins dans les tableaux « associated conditions » de la plupart des pages `_rights/`. Un lecteur qui parcourt le tableau peut glisser de « condition X est associée au déficit Y » à « condition X est causée par le déficit Y ». Les tableaux ont besoin d'une phrase de tête ou de pied qui nomme explicitement, une fois, le cadre « association ≠ causation ».
- **Correction proposée :** Pour chaque page, ajouter une phrase de cadrage en tête de la section maladies associées : l'association n'est pas la causation ; le déficit est une étiologie parmi d'autres à explorer ; le point du tableau est que le test de routine ne nomme pas le déficit quand il est présent.
- **Priorité :** moyenne
- **Dépend de :** —

_Notes :_ Phrase de cadrage ajoutée sur `magnesium.md`, `iron.md`, `potassium.md`, `folate.md`, `omega-3.md`. `muscle-mass.md` et `optimal-hormonal-levels.md` portaient déjà un cadrage équivalent (respectivement lignes 79 et 191/207). Non appliqué à `choline.md`, `glutathione.md`, `riboflavin-b2.md`, `thiamine-b1.md`, `vitamin-e.md`, `coenzyme-q10.md` : ces fiches n'ont pas de tableau discret d'associations condition ↔ nutriment, mais des sections de mécanisme (pleiotropie) ou de cas ciblé (SAMS pour Q10). Le risque de glissement causal ne se pose pas de la même façon ; à revoir si un tableau est ajouté.

## Page d'accueil et orientation à l'entrée (Charte §3, item 18)

### 18. « Recent additions » de la page d'accueil est obsolète par rapport aux publications de juillet 2026

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `index.md`, section « Recent additions ».
- **Nature :** La liste est en dur et n'inclut pas les pièces récemment publiées ou substantiellement révisées de juillet 2026 (Self-Medication as a Codified Right, The Blunder They Called a Refutation, A Litigation Brief, Two Doses One Molecule, et la FAQ elle-même). Elle ne reflète pas non plus le décompte de douze substrats revendiqué dans la FAQ.
- **Correction proposée :** Rafraîchir la liste. À plus long terme, réfléchir à savoir si « Recent additions » devrait être piloté par `last_revised` plutôt que resté en dur ; avec la réserve que la page d'accueil est *Une éditoriale* et que la sélection est délibérée, donc la correction est un rafraîchissement curaté, pas une auto-liste.
- **Priorité :** moyenne
- **Dépend de :** 4 (dates `last_revised` justes d'abord, puis curation)

_Notes :_

### 19. Page d'accueil et FAQ s'accordent sur « twelve substrates » : vérifier le compte

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `index.md`, `faq/index.md:89`.
- **Nature :** La FAQ nomme douze substrats (magnésium, potassium, fer, folate, choline, glutathion, coenzyme Q10, riboflavine, thiamine, vitamine E, oméga-3, niveaux hormonaux optimaux). Si `optimal-hormonal-levels.md` est retirée ou mise en attente (constat #1), le compte tombe à onze et la FAQ doit être mise à jour dans la même édition.
- **Correction proposée :** Après avoir tranché le sort de `optimal-hormonal-levels.md`, réconcilier le compte dans la question FAQ « Which nutrients are documented here? » et dans toute rubrique de la page d'accueil qui la référence.
- **Priorité :** basse
- **Dépend de :** 1

_Notes :_

## Traçabilité factuelle des case reports (Charte §2, item 12)

### 20. Le rapport hypothyroïdie cite des cibles TSH spécifiques sans source

Verdict : [ ] OK  [x] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_reports/hypothyroidism.md` (énoncé de la fourchette cible).
- **Nature :** Le rapport énonce une fourchette TSH optimale (à peu près 1–2 mIU/L) sans citer la source. Le chiffre est défendable dans la littérature endocrinologique, mais la convention de la ressource est de citer chaque seuil numérique. Signalé comme cousin basse priorité de l'audit numérique plus large.
- **Correction proposée :** Citer la source (par exemple la position AACE / ETA pertinente, ou la littérature primaire sur laquelle la ressource souhaite s'appuyer) ; ou adoucir l'énoncé en fourchette avec auteurs nommés.
- **Priorité :** basse
- **Dépend de :** 5 (le sort de la collection reports détermine si ça vaut la peine d'être corrigé)

_Notes :_

## Risques d'amalgame (Charte §1, constat #4)

### 21. « Supplement » vs « substrat à dose pharmacologique » : vérifier l'absence de confusion

Verdict : [ ] OK  [x] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** transversal, notamment `_editorials/the-store-that-sells-the-right/`, `_critique/two-doses-one-molecule.md`, `_definitions/self-medication-as-a-codified-right.md`, et la FAQ.
- **Nature :** L'argument de la ressource repose sur une distinction nette entre (a) « supplement » comme catégorie réglementaire-et-marketing et (b) le substrat lui-même administré à une dose physiologiquement motivée. La distinction est tirée proprement dans `two-doses-one-molecule.md` et dans `self-medication-as-a-codified-right.md`, mais les éditoriaux plus anciens (avril 2025), antérieurs au travail de juillet 2026, peuvent les confondre.
- **Correction proposée :** Relire les éditoriaux d'avril 2025 contre la distinction et signaler toute phrase qui parle de « supplements » là où elle devrait parler du « substrate at pharmacological dose », ou l'inverse. Ne pas corriger pendant l'audit.
- **Priorité :** moyenne
- **Dépend de :** 15

_Notes :_

### 22. « Deficit » vs « insufficiency » : vérifier la cohérence du vocabulaire

Verdict : [ ] OK  [x] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** transversal.
- **Nature :** Certaines pages utilisent « deficit » et « insufficiency » de manière interchangeable ; d'autres réservent « deficit » à la déplétion biochimiquement définie et « insufficiency » à un état sous-optimal qui n'atteint pas encore le seuil du déficit (la discussion ferritine 30 / ferritine 50 est le cas paradigmatique). L'argument de la ressource gagne à avoir une convention stable.
- **Correction proposée :** Décider la convention (proposition : « deficit » = sous le seuil de fonction ; « insufficiency » = entre le seuil labo de routine et le seuil de fonction). Passe corpus en session ultérieure.
- **Priorité :** basse
- **Dépend de :** —

_Notes :_

## SEO / accessibilité (Charte §3, items 19–20)

### 23. Aucune image Open Graph configurée

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** transversal ; `_config.yml`, `_includes/head.html` (s'il existe).
- **Nature :** `jekyll-seo-tag` est installé et les `description` par page sont présentes, mais il n'y a pas de frontmatter `image` ni de défaut OG au niveau du site. Les aperçus sociaux tomberont sur des cartes texte simples. La charte (§3, item 19) demande si c'est un choix conscient.
- **Correction proposée :** Soit ajouter une image OG par défaut au niveau du site (carte typographique simple portant le nom de la ressource et sa devise) ; soit confirmer le choix de ne pas en avoir.
- **Priorité :** basse
- **Dépend de :** —

_Notes :_ Carte typographique par défaut générée : `assets/og-default.png` (1200×630, Cormorant Garamond, palette du site). Devise « What physiological integrity requires. » retenue au lieu de « the right to food » parce que le corpus déborde du droit à l'alimentation stricto sensu. Câblée site-wide dans `_config.yml` via la clé `image:` que `jekyll-seo-tag` prend comme défaut ; peut être surchargée par page via le frontmatter.

### 24. La déclaration d'accessibilité est vide

Verdict : [ ] OK  [x] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_legal/accessibility.md`.
- **Nature :** Voir constat #7. Renvoie aussi à la charte §3, item 20 (accessibilité) : ordre des titres, textes alternatifs sur les images, contraste sur la couleur d'accent utilisée pour les badges de résultats de recherche, navigation clavier du panneau de recherche. Cet audit n'a pas fait de passe accessibilité complète, il n'a signalé que la déclaration vide.
- **Correction proposée :** Faire une vraie passe accessibilité (WAVE, axe, navigation au clavier uniquement du panneau de recherche) avant de peupler la déclaration.
- **Priorité :** basse
- **Dépend de :** 7

_Notes :_

## Cohérence des cross-references (Charte §2, item 6)

### 25. Phrases-concepts récurrentes non liées à leur critique-mère au premier usage

Verdict : [x] OK  [ ] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** transversal. Exemple : « the false negative of serum potassium » apparaît dans `_rights/potassium.md`, `faq/index.md`, `_editorials/`, et ailleurs, mais toutes les occurrences ne renvoient pas à `_critique/false-negative-serum-potassium.md` au premier usage. Phrases similaires : « the ferritin threshold », « otherwise healthy », « calibrated for nothing », « two doses, one molecule ».
- **Nature :** Un lecteur qui rencontre la phrase pour la première fois sur une page donnée devrait avoir un chemin en un clic vers la critique qui la développe. Le cross-linking actuel est inégal.
- **Correction proposée :** Pour chaque phrase-concept récurrente, passer le corpus et lier au premier usage par page.
- **Priorité :** moyenne
- **Dépend de :** —

_Notes :_

## Cohérence bibliographique (Charte §3, item 23)

### 26. Le style de citation varie entre les bibliographies `_rights/`

Verdict : [ ] OK  [x] Plus tard  [ ] Non  [ ] À discuter  [ ] Déjà fait

- **Lieu :** `_rights/*.md` (sections bibliographie).
- **Nature :** Certaines bibliographies utilisent des références en notes de bas de page avec ancres numériques (par exemple `_rights/folate.md`) ; d'autres utilisent des citations en ligne ; la présence de DOI est inégale ; l'ordre des noms d'auteurs n'est pas uniforme. La charte (§3, item 23) demande de la cohérence.
- **Correction proposée :** Décider le style-maison (proposition : auteur-année-titre avec DOI quand disponible, sans notes numérotées) et passer le corpus en session ultérieure.
- **Priorité :** basse
- **Dépend de :** —

_Notes :_

---

## Items vérifiés et sans constat

- **Liens internes cassés.** 174 liens markdown dans toutes les collections de contenu, résolus contre les permaliens déclarés dans `_config.yml`. 0 cassé. Les variantes Liquid dans layouts et includes se résolvent aussi proprement.
- **Calques francophones dans le contenu publié.** Aucun n'a émergé. Des calques apparaissent dans les brouillons `_inbox/` (hors périmètre) et dans `_resources/01f26f96.md` (Mayer 1979, texte français original, intentionnel).
- **Citations légales, vérifications par échantillon.** Alma-Ata articles IV et VII, Convention d'Oviedo art. 5, ICESCR art. 12 lu à travers General Comment 14 §43, ICESCR art. 11 lu à travers General Comment 12 §8, TAC v. Minister of Health (Afrique du Sud, 2002), Urgenda, T-760/08 : toutes exactes telles que citées dans `_definitions/self-medication-as-a-codified-right.md`, `_definitions/the-instruments-already-exist.md`, et `_definitions/a-litigation-brief.md`.
- **Seuils numériques, vérifications par échantillon.** Paliers ferritine (15 / 30 / 50 μg/L), thiamine 400× RDA à la dose de Wernicke, B12 400× RDA en injection, co-requis magnésium-potassium via ROMK : tous traçables dans les bibliographies des pages `_rights/` correspondantes.
- **Autodésignation « this site ».** Aucune occurrence dans le contenu publié (mémoire `feedback_self_designation_resource.md`). « Site » n'apparaît que dans la charte d'audit elle-même et dans les fichiers de code / build.
- **Flags `featured`.** `_definitions/all-medicine-is-preventive.md` et `_editorials/you-are-not-the-exception.md` portent tous deux `featured: true` correctement ; aucune page featured involontaire n'a émergé.

---

*Fin de la liste. Perig valide ou rejette item par item. Les items rejetés restent dans ce fichier avec un marqueur « REJETÉ (raison) » pour que la prochaine passe d'audit ne les relève pas à nouveau.*
