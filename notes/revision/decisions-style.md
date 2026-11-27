# Décisions de style (valables pour tous les textes)

Ce fichier note ce que Perig a tranché une fois pour toutes. Une décision n'y entre que lorsqu'il la valide pour l'ensemble des textes.

## Décisions prises

- Méthode : révision dialoguée fragment par fragment (voir `.claude/skills/revision-dialoguee/SKILL.md`). Le format « rapport en marge » est abandonné (27 novembre 2026).
- Longueur des phrases : règle 10 du guide (phrase longue construite vers la droite, phrase courte réservée au contraste, pas de comma splice) (27 novembre 2026).
- Le fond est hors périmètre de cette révision, une autre révision est en cours (27 novembre 2026).
- La version française des éditoriaux doit être publiée (27 novembre 2026).

## À trancher

- Contractions (it's, you're, don't) ou formes pleines.
- Nombres en chiffres (95%) ou en lettres (ninety-five percent), et espacement à l'anglaise (4,700 mg, 97.6%).
- Point de vue « you » : à partir d'où l'assumer, et comment rendre le début cohérent.
- Nombre de chutes à garder par texte.

## Chantier technique lié

- Le sélecteur de langue de `_layouts/default.html` (lignes ~193 et ~274) envoie vers Google Traduction pour FR, ES, PT, DE, IT. Quand une version française révisée existe, le lien FR doit pointer vers elle et non vers la traduction automatique. À faire par l'agent du dépôt, une fois la structure des pages françaises décidée.
