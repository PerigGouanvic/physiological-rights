# Base de connaissance (KB) — physiological-rights

Pipeline RAG local pour la recherche personnelle et l'écriture éditoriale.

Voir `CLAUDE.md` (racine du dépôt) pour le concept fondateur (droits physiologiques) et la posture épistémique qui guident l'usage de cette KB.

## Ce qu'il y a ici

| Chemin | Rôle | Versionné ? |
|--------|------|-------------|
| `scripts/` | Pipeline Python (config, chunker, ingestion, requête) | oui |
| `db/kb.sqlite` | Base SQLite (chunks + embeddings via sqlite-vec + FTS5) | non |
| `sources/` | Sources externes ingérées (PDF, articles) | non |
| `logs/` | Journaux d'ingestion | non |
| `.venv/` | Environnement Python | non |

Le contenu ingéré vient de :
- Collections Jekyll : `_definitions/`, `_reports/`, `_critique/`, `_editorials/`, `_resources/`, `_inbox/` — markdown avec frontmatter YAML.
- Sources externes : PDFs dans `kb/sources/` (littérature scientifique, briefings), avec sidecar `<nom>.meta.yaml` pour les métadonnées.

## Installation

Depuis la racine du dépôt :

```bash
python3 -m venv kb/.venv
kb/.venv/bin/pip install -r kb/scripts/requirements.txt
cp .env.example .env
# Édite .env pour y mettre VOYAGE_API_KEY
```

## Ingestion

```bash
# Ingestion incrémentale (skip les fichiers inchangés)
kb/.venv/bin/python kb/scripts/ingest.py

# Ré-ingestion complète
kb/.venv/bin/python kb/scripts/ingest.py --force

# Un seul dossier
kb/.venv/bin/python kb/scripts/ingest.py --path _reports

# Test à sec (parse + chunk, aucun appel API, aucune écriture DB)
kb/.venv/bin/python kb/scripts/ingest.py --dry-run
```

Les fichiers sont hashés — relancer sans `--force` ne coûte rien pour ce qui est déjà indexé.

## Requêter

```bash
# Recherche hybride (dense + BM25), pondérée par authority_score, MMR pour la diversité
kb/.venv/bin/python kb/scripts/query.py "cofacteurs thyroïde iode sélénium"

# Plus de résultats
kb/.venv/bin/python kb/scripts/query.py "..." --k 10

# Filtrer par type de source
kb/.venv/bin/python kb/scripts/query.py "..." --type reports,critique

# Contrôler la diversité (défaut 0.7 : plutôt relevance ; 0.5 : plus diversifié ; 1.0 : pure relevance)
kb/.venv/bin/python kb/scripts/query.py "..." --mmr-lambda 0.5

# Désactiver le MMR
kb/.venv/bin/python kb/scripts/query.py "..." --no-mmr

# JSON pour usage programmatique
kb/.venv/bin/python kb/scripts/query.py "..." --json
```

## Métadonnées côté source

**Markdown** : frontmatter YAML en tête de fichier :

```yaml
---
title: "…"
authority_score: 0.9        # défaut 1.0 — assigné par Perig, pas dérivé du prestige
source_category: mechanism  # libre — ex: case-series, orthomolecular, overview, regulatory, clinical-experience
---
```

**PDF** : sidecar `<nom>.meta.yaml` à côté du PDF (mêmes champs, plus libres) :

```yaml
title: "Potassium Intake of the U.S. Population — NHANES 2017-2018"
authors: [Hoy MK, Goldman JD, Moshfegh AJ]
year: 2022
source_category: population-data
authority_score: 1.0
url: https://www.ars.usda.gov/…
doi: 10.…
note: |
  Ce que la source apporte au corpus, en une phrase.
```

Si le sidecar est absent, l'ingestion utilise les métadonnées internes du PDF (`Title`) puis le nom de fichier comme fallback ; `authority_score` par défaut = 1.0.

L'`authority_score` multiplie le score de similarité au moment du reranking. C'est le levier principal pour promouvoir certaines sources et déclasser les autres.

L'extraction PDF (via `pdfplumber`) insère un marqueur `[page N]` à chaque saut de page, ce qui permet de retracer un extrait vers sa page d'origine.

## Serveur MCP

Un serveur MCP (`kb/scripts/mcp_server.py`) expose deux outils à Claude Code :

- `kb_query(query, k, types, mmr_lambda)` — même retrieval que le CLI.
- `kb_list_sources()` — inventaire.

Il est enregistré dans `.mcp.json` à la racine du dépôt. Au premier lancement de Claude Code dans ce dossier, Claude te demandera l'autorisation d'activer le serveur — accepte pour que l'outil soit disponible en conversation.

Test manuel du serveur (facultatif — il communique en JSON-RPC sur stdin) :

```bash
kb/.venv/bin/python kb/scripts/mcp_server.py
# Ctrl+C pour quitter
```

## État actuel

**v1.3** — hybride dense + BM25, rerank par authority_score, MMR, exposition MCP, ingestion PDF avec sidecar YAML.

**À venir** :
- Reranker cross-encoder (Voyage rerank ou modèle local) pour affiner le top-K.
- Extraction PDF layout-aware pour la littérature multi-colonnes complexe (actuellement `pdfplumber` gère raisonnablement le texte simple).
