---
name: revision-dialoguee
description: Révision dialoguée d'un texte du site (éditoriaux d'abord), fragment par fragment, en anglais et en français, entre le texte, Perig et Claude. À utiliser quand Perig veut réviser une page de physiological-rights.org ou en produire la version française.
---

# Révision dialoguée (dialogue à trois : le texte, Perig, Claude)

## But

Retirer d'un texte rédigé par une IA à partir des idées de Perig les tics de l'IA, et y faire revenir sa voix, en anglais comme en français. Le français est publié sur le site, il ne sert pas seulement d'outil. On fait en filigrane de la stylistique comparée du français et de l'anglais, et l'enrichissement peut aller dans les deux sens.

## Avant de commencer

1. Lire `notes/revision/guide-revision.md` (le guide de révision, en particulier la partie II et la règle 10 sur la longueur des phrases).
2. Lire `notes/revision/decisions-style.md` : ce que Perig a déjà tranché vaut pour tous les textes, ne pas le redemander.
3. S'il existe un journal pour la page dans `notes/revision/journal/`, le lire et reprendre au dernier fragment traité.
4. Le fond n'est pas dans le périmètre, sauf si Perig l'ouvre. Une autre révision du fond est en cours.

## Déroulement, pour chaque fragment

Perig travaille sur téléphone, en dictée. Les fragments font environ un demi-écran de téléphone (2 à 4 phrases), recopiés directement dans la conversation, jamais dans un document à côté.

1. Recopier le fragment anglais tel qu'il est sur le site, en citation.
2. Perig répond, au choix : une réécriture anglaise, une version française dite comme il la dirait, un doute (« ça arrive comme un cheveu sur la soupe »), ou les deux langues. Rester souple : il pense bilingue, et passer au français peut être difficile par moments.
3. Claude répond en commentaires numérotés et courts :
   - ce que la proposition de Perig règle, en nommant la règle du guide quand c'est utile ;
   - ce qui reste à trancher, avec une ou deux formulations concrètes ;
   - quand il y a du français, ce que le français fait mieux (liens implicites, enchaînement, précision) et ce que l'anglais peut en absorber : la phrase cumulative oui, l'emboîtement de subordonnées non, les comma splices jamais ; et ce que l'anglais peut apporter au français.
4. Puis recopier le fragment suivant, sans attendre de confirmation, sauf si une décision bloque la suite.

## Règles de conduite

- Ne pas relever les erreurs qui ressemblent à de la dictée (mot proche, homophone, accord manquant), sauf si elles changent le sens.
- Ne pas confirmer de version finale tant que Perig ne le demande pas. Les propositions restent provisoires.
- Quand Perig doute d'un passage, chercher pourquoi le passage désoriente (registre, point de vue, deux idées fondues en une, explication de trop) avant de proposer une coupe.
- Signaler les conséquences d'une coupe sur les fragments suivants (une phrase qui dépend de celle qu'on coupe).
- Appliquer le guide à ses propres propositions : pas de panneaux, pas de chute vendue, pas de point-virgule ni de tiret long, phrase longue construite vers la droite.
- Ne jamais modifier le texte publié sans validation explicite.

## Tenue des fichiers (tout reste dans le dépôt)

- `notes/revision/journal/<page>.md` : pour chaque fragment, le texte d'origine, les propositions de Perig, la version retenue provisoirement, les points ouverts. Mettre à jour en fin de séance.
- `notes/revision/decisions-style.md` : ajouter une décision seulement quand Perig la tranche pour l'ensemble des textes.
- À la fin d'une page : produire la version anglaise finale et la version française, que Perig valide avant publication.

## Contexte et longueur

Une conversation par page, pour ne pas surcharger le contexte. La continuité passe par le journal et le fichier de décisions, pas par l'historique des conversations.
