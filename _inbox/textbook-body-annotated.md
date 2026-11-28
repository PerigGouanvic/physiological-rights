# The Textbook Body, annotated

*Brouillon de projet, 28 nov. 2026 (Claude web, avec Perig). Prolonge l'éditorial `_editorials/the-textbook-body.md`.*

## L'idée

Ne rien réécrire : **annoter**. Reprendre les schémas et les passages fondamentaux des manuels de biologie, de physiologie et de médecine, et leur ajouter une couche qui dit ce que chaque flèche présuppose : quel cofacteur, quel nutriment, quelle composition de membrane, et quelle part de la population en manque. Chaque annotation renvoie à la fiche correspondante de `_rights/` et à ses sources.

L'éditorial le dit déjà : « Every arrow on every diagram is a cofactor somebody had to eat. The diagram does not say so. » L'édition annotée le dirait, flèche par flèche.

## Pourquoi c'est faisable

- Les manuels existent : il n'y a rien à écrire, seulement à annoter.
- Le système de références du site s'y prête : `{% include cite.html id="..." ex="..." %}`, des fiches qui glissent depuis le bas sur téléphone et sont aussi longues que nécessaire.
- Le travail de moine (relever chaque présupposé, le relier aux fiches et aux sources) peut être confié à un assistant, sous la direction de Perig.

## Premiers schémas candidats

1. **L'ATP** : la forme biologiquement active est le complexe Mg-ATP ; voir `_rights/magnesium.md`.
2. **La pompe sodium-potassium** : environ un quart de la dépense énergétique au repos ; magnésium et potassium ; elle conditionne l'excitabilité et la libération des neurotransmetteurs.
3. **La membrane** : représentée comme une ligne ; sa composition (choline, oméga-3, vitamine E) n'apparaît pas.
4. **Le cycle de Krebs et la chaîne respiratoire** : cofacteurs directs (thiamine, riboflavine, niacine, acide pantothénique, acide lipoïque, magnésium, centres fer-soufre) et cofacteurs indirects qui créent l'environnement des réactions ; fréquence des carences en thiamine et en fer.
5. **La synapse** : précurseurs, cofacteurs de synthèse des neurotransmetteurs, environnement ionique.

## Question à trancher : quel manuel annoter ?

- **Droit d'auteur.** Annoter publiquement un manuel commercial suppose d'en reproduire des schémas ou des passages, ce qui pose un problème de droits. Une piste, de mémoire et à vérifier : le manuel *Anatomy and Physiology* d'OpenStax est publié sous licence Creative Commons Attribution, ce qui permettrait de reproduire et d'annoter librement, avec attribution.
- Alternative : citer brièvement les manuels commerciaux et redessiner des schémas génériques.

## Forme possible sur le site

- Une nouvelle collection (par exemple `_annotated/`), une page par schéma ou par chapitre.
- Chaque page : le schéma, puis les annotations numérotées, chacune avec ses citations et un lien vers la fiche `_rights/`.
- Lien depuis l'éditorial *The Textbook Body*.

## Cadre théorique

Voir `revolution/notes/2026-11-28-pedagogie-inverse.md` (la pédagogie « par les bases » comme source de dissociation durable ; Fleck sur la science des manuels, Kuhn sur la réécriture de l'histoire par les manuels).
