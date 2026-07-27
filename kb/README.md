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

Un serveur MCP (`kb/scripts/mcp_server.py`) expose quatre outils à Claude Code :

- `kb_query(query, k, types, mmr_lambda)` — recherche hybride sur le corpus indexé (Jekyll + PDF).
- `kb_list_sources()` — inventaire de la KB vectorielle.
- `kb_reddit_search(pattern, subs, kinds, min_len, min_score, ...)` — grep regex sur les dumps Reddit (voir section suivante).
- `kb_reddit_sources()` — inventaire des dumps Reddit téléchargés.

Il est enregistré dans `.mcp.json` à la racine du dépôt. Au premier lancement de Claude Code dans ce dossier, Claude te demandera l'autorisation d'activer le serveur — accepte pour que l'outil soit disponible en conversation. Les outils ne se rechargent pas à chaud : si tu modifies le serveur, quitte et relance la session Claude Code.

Test manuel du serveur (facultatif, communique en JSON-RPC sur stdin) :

```bash
kb/.venv/bin/python kb/scripts/mcp_server.py
# Ctrl+C pour quitter
```

## Corpus Reddit (`kb/reddit/`)

### Pourquoi ce corpus existe

La littérature académique dit peu sur le vécu clinique de la carence, du surdosage, du symptôme qui bouge quand on prend telle substance. Reddit héberge, à défaut de mieux, un laboratoire d'auto-expérimentation à grande échelle : des dizaines de milliers de personnes racontent, souvent avec précision, ce qui a marché et ce qui n'a pas marché sur elles.

Ce corpus n'est pas une preuve. C'est du **témoignage** et de la **piste**. Sa valeur pour ce projet :

- **Sourcer une anecdote clinique** pour une pièce éditoriale (« des personnes rapportent que… »).
- **Repérer des patterns convergents** — quand vingt témoignages disent la même chose sur le potassium et les arythmies, ça pointe vers quelque chose que le sérique ne voit pas.
- **Cartographier ce qui manque au diagnostic** — les personnes qui écrivent « mon médecin a dit que c'était normal alors que j'étais dans cet état » sont exactement le corpus que le site conceptualise.

À manier avec la posture épistémique du dépôt (voir `CLAUDE.md`) : le témoignage anecdotique n'est pas subordonné à la revue par les pairs, il l'informe. Il n'est pas non plus une conclusion en soi.

### Ce qui est disponible

- 67 subreddits, ~3.3 GB compressés, téléchargés en juillet 2026 via l'API Arctic Shift.
- Posts pour tous, **commentaires** pour 4 subs seulement (`B12_Deficiency`, `CFS`, `MTHFR`, plus un). Les threads complets ne sont donc pas là pour la majorité.
- Le corpus n'est pas dans la KB vectorielle. Pas d'embeddings, pas de recherche sémantique. Uniquement du matching regex sur le texte brut.
- Coût : **zéro**. Aucun appel API en interrogation.

Pour l'inventaire à jour : demande à Claude « fais un `kb_reddit_sources` » ou lance `kb/.venv/bin/python kb/scripts/reddit_search.py --help`.

### Comment m'en servir en session Claude Code

Tu n'as pas besoin de connaître l'API du tool. Tu demandes en langage naturel, Claude appelle l'outil pour toi. Exemples de formulations qui marchent :

| Ce que tu tapes | Ce que Claude appelle |
|-----------------|-----------------------|
| « Cherche dans Reddit les témoignages de palpitations sous magnésium, dans les subs Magnesium et Supplements » | `kb_reddit_search("palpitat", subs=["Magnesium","Supplements"], min_len=400)` |
| « Trouve les meilleurs posts de r/MTHFR sur le methylfolate » | `kb_reddit_search("methylfolate", subs=["MTHFR"], sort_by="score", min_score=10)` |
| « Cherche dans les subs thyroïde les gens à qui on a dit que leur TSH était normale » | `kb_reddit_search("TSH.*normal", subs=["Hypothyroidism","Hashimotos","StopTheThyroidMadness"], min_len=500)` |
| « Quels subs sont téléchargés ? » | `kb_reddit_sources()` |

Trois consignes qui rendent les résultats bons :

1. **Toujours nommer les subs** quand tu peux. Un scan sans `subs` traverse 3 GB et prend plusieurs minutes.
2. **Filtrer sur `min_len` et `min_score`** pour éliminer les one-liners et les posts sans engagement. Défauts : 200 chars, score 0. Monter à 400/5 change tout.
3. **Écrire une regex assez précise** pour ne pas ramener 500 résultats. `\bK2\b` est mieux que `K2`. `palpitat` capte palpitations/palpitating/palpitate.

### Corpus dense vs corpus large

Subs à haute densité physiologique (recommandés pour la plupart des recherches) :

`MTHFR`, `B12_Deficiency`, `Magnesium`, `VitaminD`, `Iron`, `Zinc`, `Selenium`, `Copper`, `Iodine`, `Choline`, `Boron`, `methylation`, `omega3`, `Hypothyroidism`, `Hashimotos`, `Hyperthyroidism`, `thyroidhealth`, `StopTheThyroidMadness`, `AdrenalFatigue`, `PCOS`, `Menopause`, `PMDD`, `HypothalamicAmenorrhea`, `Testosterone`, `POTS`, `dysautonomia`, `Fibromyalgia`, `CFS`, `MCAS`, `Histamine`, `HistamineIntolerance`, `RestlessLegs`, `Migraine`, `ehlersdanlos`, `Nootropics`, `StackAdvice`, `Peptides`, `Biohackers`, `Supplements`, `SelfHacking`, `QuantifiedSelf`, `DrWillPowers`, `PSSD`, `Anemic`, `AskDocs`, `FamilyMedicine`, `DiagnoseMe`, `medicine`, `FamilyMedicine`.

Subs à densité diffuse (à éviter sauf recherche spécifique) : `depression`, `Anxiety`, `ADHD`, `keto`, `Fitness`, `bodybuilding`, `tinnitus`, `insomnia`, `medical_advice`. Ils ont beaucoup de volume mais peu de spécificité nutritionnelle.

### Ce que ce corpus ne fait PAS

- Pas de recherche sémantique. Si tu cherches « perte de muscle chez la femme âgée obèse », le tool ne comprendra rien. Il faut passer des termes concrets (« sarcopenic obesity », « lost muscle mass », etc.).
- Pas de threads. Sauf pour les 4 subs qui ont des comments, tu vois les posts isolés.
- Pas de dédoublonnage entre subs. Les cross-posts apparaissent plusieurs fois.
- Non incrémental. Le dernier téléchargement date du 21 juillet 2026. Pour actualiser un sub :

```bash
kb/.venv/bin/python kb/scripts/reddit_download.py <sub> --resume
```

### CLI de secours (identique à l'outil MCP)

```bash
kb/.venv/bin/python kb/scripts/reddit_search.py "palpitat" --subs Magnesium,Supplements --min-len 400 --min-score 5 --sort-by score --limit 10
```

### Chantier dormant : ingestion vectorielle

`kb/scripts/ingest_reddit.py` sait chunker + embedder les dumps Reddit vers la KB SQLite. Coût estimé : $1 (filtres stricts) à $30 (passe intégrale) en voyage-3. Reporté tant que le grep suffit.

## État actuel

**v1.3** — hybride dense + BM25, rerank par authority_score, MMR, exposition MCP, ingestion PDF avec sidecar YAML.

**À venir** :
- Reranker cross-encoder (Voyage rerank ou modèle local) pour affiner le top-K.
- Extraction PDF layout-aware pour la littérature multi-colonnes complexe (actuellement `pdfplumber` gère raisonnablement le texte simple).
