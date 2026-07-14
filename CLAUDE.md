# physiological-rights

## Nature du dépôt

Ce dépôt est à la fois :
- **Un site Jekyll public** consacré aux **droits physiologiques** (voir section suivante).
- **Une base de connaissance personnelle** utilisée par Perig pour sa recherche clinique et l'écriture éditoriale.

Le champ traité concerne principalement les vitamines, minéraux, nutriments conditionnellement essentiels et molécules apparentées.

## Concept fondateur : les droits physiologiques

Les droits physiologiques sont **l'opérationnalisation du droit à l'alimentation**. Le droit à l'alimentation, tel qu'il est défini dans les instruments existants, n'explicite pas ce en quoi consiste l'alimentation — il se rabat sur des catégories très générales (protéines, calories, micronutriments) sans spécificité clinique. C'est une **erreur de définition** qui produit un **« droit du pauvre et des défavorisés »** : un droit rabaissé à un plancher minimal. Cibler les moins bien lotis n'est évidemment pas mauvais en soi, mais restreindre le droit à ce seul plancher en évacue l'essentiel. Les droits physiologiques cherchent à combler ce vide en spécifiant les besoins physiologiques réels.

### Rapport à la médecine fondée sur les faits (EBM)

Une médecine fondée sur les droits physiologiques s'**oppose** à l'evidence-based medicine, **non par conflit de principe entre droits et faits**, mais parce que la nature des faits nutritionnels rend les droits physiologiques largement inévaluables selon les critères EBM. Ce n'est pas Perig qui commence cette incompatibilité : elle est structurelle. Le monde médical moderne fonctionne dans un double bind :

- **Absence de preuves** faute de financement pour la recherche sur les nutriments.
- **Absence de tests utiles et valides** pour connaître les besoins nutritionnels individuels.

## Structure

Contenu publié (versionné) :
- `_rights/` `rights/` — **fiches de droits par nutriment ou paramètre physiologique** (Mg, folate, oméga-3, B1, B2, E, niveaux hormonaux optimaux, etc.). **C'est le format central du site.** Chaque fiche est ambitieuse (200+ lignes) : historique long, chercheurs référents nommés, critique structurelle des tests, mécanismes physiologiques, tableau des maladies associées, timeline, bibliographie référencée. Modèle à imiter : `_rights/magnesium.md`.
- `_definitions/` `definitions/` — fiches de fond conceptuelles (le concept de droit physiologique, rights-based vs EBM, etc.)
- `_reports/` `reports/` — vignettes cliniques courtes, illustratives, subordonnées aux vraies fiches `_rights/` (une fiche `_reports/<nutriment>-deficiency.md` ne remplace pas `_rights/<nutriment>.md`)
- `_critique/` `critique/` — critiques argumentées transversales (ex : ambiguïtés du « régime équilibré »)
- `_editorials/` `editorials/` — éditoriaux
- `_resources/` `resources/` — ressources (bibliographie thématique, textes légaux, recommandations internationales)
- `_inbox/` — brouillons en cours de maturation
- `_legal/` — mentions légales

Toutes les collections sont déclarées dans `_config.yml` — s'y référer comme source d'autorité, la présente liste peut prendre du retard.

Non-publié (gitignoré) :
- `kb/db/`, `kb/sources/`, `kb/logs/` — infrastructure RAG : base vectorielle locale, sources ingérées (PDF, articles), journaux.
- `kb/scripts/` reste versionné : c'est le pipeline lui-même.

Le contexte clinique personnel de Perig n'est pas stocké dans le dépôt : il vit dans la mémoire persistante de Claude (`~/.claude/projects/…/memory/`). Voir la note de collaboration correspondante.

## Posture épistémique

Le projet part du constat qu'une partie du discours dominant sous-estime le rôle thérapeutique des nutriments, en les cantonnant au champ de la prévention. Perig soutient qu'une intervention nutritionnelle peut prévenir l'aggravation d'une maladie installée, voire contribuer à un rétablissement. Le corpus inclura des sources moins conventionnelles (cliniciens, séries de cas, littérature orthomoléculaire, monographies spécialisées) dont Perig juge la rigueur, indépendamment de leur prestige académique.

En travaillant sur ce dépôt :

- **Ne pas utiliser le consensus dominant comme argument-massue** pour clôturer une discussion. « The evidence is limited » n'est pas une conclusion — c'est une invitation à examiner ce qui existe.
- **Face à une tension** entre le corpus local et un "savoir par défaut", exposer la tension au lieu de trancher automatiquement par le mainstream.
- **Distinguer** « l'évidence est faible » de « le mainstream désapprouve » — ce sont deux constats différents.
- Le **scoring d'autorité** des sources dans la KB est assigné manuellement par Perig au moment de l'ingestion, pas dérivé d'une hiérarchie de journaux.
- Perig lit la recherche primaire depuis longtemps — **éviter les explications de base** en biochimie, statistiques, méthodologie.

## Priorités cliniques

Quand Perig pose une question qui concerne sa santé, il est prioritaire de :
1. Utiliser la KB (`kb/`) plutôt que de raisonner uniquement de mémoire.
2. Croiser plusieurs sources du corpus, en particulier quand une catégorie de nutriments touche à plusieurs systèmes (effets synergiques, cofacteurs, erreurs de catégorie).
3. Distinguer clairement dans la réponse : ce qui vient du corpus, ce qui vient de connaissances générales, ce qui reste conjectural.

## Utilisation de la base de connaissance

La KB est exposée à Claude Code via un **serveur MCP** déclaré dans `.mcp.json` à la racine. Deux outils sont disponibles automatiquement dans les conversations sur ce dépôt :

- **`kb_query(query, k, types, mmr_lambda)`** — recherche hybride (embeddings Voyage + BM25 sur FTS5), reranking pondéré par `authority_score`, puis MMR pour la diversité. À invoquer dès qu'une question de Perig touche à un sujet potentiellement documenté dans le corpus.
- **`kb_list_sources()`** — inventaire (chunks, fichiers, autorité) pour savoir ce qui est indexé avant de requêter.

**Consignes d'usage** :
- Face à une question clinique ou biologique, appeler `kb_query` **avant** de répondre — même si la réponse « de mémoire » semble évidente. La KB peut contenir des précisions, des séries de cas, ou des rappels d'auteurs de référence que Perig a jugés importants.
- Signaler explicitement dans la réponse ce qui vient de la KB (avec `source_path`) vs. ce qui vient de connaissances générales.
- Si un résultat semble marginal ou dominé par un seul texte long, retenter avec `mmr_lambda=0.5` pour forcer plus de diversité.
- Si Perig cherche à écrire ou raffiner un article public, croiser la KB pour trouver les fils argumentatifs déjà présents dans les autres sections (`_definitions`, `_critique`, `_editorials`).

CLI de secours (identique fonctionnellement) : `kb/.venv/bin/python kb/scripts/query.py "..."`
