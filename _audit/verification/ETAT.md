# État du chantier de vérification (mis à jour 2026-11-19, 3h50)

## Fait (sources en pop-up, corrections appliquées et poussées)
- `_did-you-know/magnesium-serum-test-misses-99-percent.md` (pilote)
- `_rights/magnesium.md` (40 marqueurs) — dossier `magnesium.md`
- `_rights/potassium.md` (38 marqueurs)
- `_rights/omega-3.md` (67 marqueurs) — table d'appariement `omega-3-matches.md`
- `_editorials/the-textbook-body.md` : arithmétique vérifiée, oméga-3 mis à jour (Powers 2026)

## Outils
- `scripts/fetch_source.py <sid> pmid:|pmc:|doi:|url:|pdf:` → `kb/sources/texts/` (gitignoré). Cloudflare : passer par `url:https://web.archive.org/web/2025id_/<url>`.
- `scripts/make_source.py _audit/source-specs/<sid>.json` → `_sources/<sid>.md` (extraits mécaniques ; options anchor/until/from/to/marks).
- `scripts/check_refs.py <page>` (listes numérotées) ; `scripts/auto_cite.py <page> --fetch` (notes kramdown `[^n]`, table d'appariement à relire).
- Test : build Docker `jekyll/jekyll:4.2.2` avec `.local-build.yml`, captures `~/prbuild/tools/shot3.js`.

- `_rights/choline.md` (18), `_rights/vitamin-e.md` (65) — 2026-11-19 matin
- *The Textbook Body* : les sept puces ouvrent leur source. Reste : le fer (« ferritine < 30 chez un tiers des femmes réglées ») — Weyand 2023 (JAMA) n'est accessible qu'en PDF verrouillé ; vitamine D < 75 nmol/L standardisé introuvable (Ginde 2009 non standardisé, Herrick 2019 seuils IOM).

## Suite, dans l'ordre
2. Autres `_rights/` : folate, thiamine-b1, riboflavin-b2, vitamin-c, iron, insulin, coenzyme-q10, glutathione, muscle-mass, optimal-hormonal-levels.
3. Recopies : `_critique/the-hunger-we-dont-see.md`, `behind-every-test-an-industry.md`, `what-the-label-cannot-say.md` (Liebscher 2004, Costello 2016 déjà en fiches).
4. Puis `_did-you-know/`, `_critique/`, `_editorials/`, `_definitions/`.
