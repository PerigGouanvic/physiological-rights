---
title: Audit findings — July 2026 pass
status: internal
created: 2026-07-24
scope: findings from the AUDIT-CHARTER pass (Sections 1–3)
---

# Audit findings — July 2026 pass

*One numbered list. Findings only, no fixes applied. Each item follows the shape defined in AUDIT-CHARTER Section 4. Perig validates or rejects item by item; rejected items stay in the file with a REJECTED marker.*

*Method notes: all internal markdown links across content collections were cross-checked against declared collection permalinks — 0 broken out of 174. Liquid `{{ site.url }}` and `relative_url` references in `_layouts/`, `_includes/`, `index.md`, and section index files were also checked — 0 unresolved. Numerical thresholds spot-checked (thiamine 400× RDA, ferritin 15/30/50 tiers, ICESCR GC14 §43, Alma-Ata IV/VII, Oviedo Art. 5) — all traceable. French calques in published content — none surfaced.*

---

## Structural findings (charter Section 1 — observed cousins, and Section 2 — guessable)

### 1. `_rights/optimal-hormonal-levels.md` is a stub linked as if authoritative
- **Location:** `_rights/optimal-hormonal-levels.md` (whole file); linked from `faq/index.md:89` as one of the twelve substrates and from the Rights index.
- **Nature:** The page is `status: draft`, 47 lines, five short sections (Thyroid, Sex, Adrenal, Insulin, Individual physiology), and lacks the `name:` / `category:` / `researchers:` frontmatter fields carried by the other eleven `_rights/` pages. It also lacks the historical section, the named-researchers section, the associated-conditions table, the timeline, and the bibliography that the reference template (`_rights/magnesium.md`) provides. Yet the FAQ answer to *"Which nutrients are documented here?"* names it as one of the twelve documented substrates.
- **Proposed fix:** Either promote the page to the model structure (history, researchers, test critique, mechanism, associated conditions, timeline, bibliography) or remove it from the "twelve substrates" claim in the FAQ and from the Rights index until it is model-conformant. If kept as draft, add `search_exclude: true` so `search.json` does not surface it.
- **Priority:** high
- **Depends on:** —

### 2. Eleven of twelve `_rights/` pages do not link back to the mother definition
- **Location:** `_rights/` — all files except `choline.md`.
- **Nature:** Charter finding #2 (recency-bias in link selection) has a structural cousin: only `_rights/choline.md` links to `/definitions/physiological-rights/`. A reader who arrives on a nutrient fiche via search does not have a one-click path back to what a "right" means in this resource. Charter Section 2, item 5 predicts exactly this.
- **Proposed fix:** Add a single link (in the opening paragraph or in a "See also" footer) to `/definitions/physiological-rights/` on each of the other eleven pages.
- **Priority:** medium
- **Depends on:** —

### 3. `_rights/vitamin-e.md` carries a non-standard `status: documented`
- **Location:** `_rights/vitamin-e.md`, frontmatter.
- **Nature:** All other model-conformant `_rights/` pages use `status: published`. `vitamin-e.md` uses `status: documented`, which is not a value used elsewhere in `_rights/`. The same non-standard value appears on `_resources/01f26f96.md` (Mayer 1979), where it may be defensible for a source document, but on a `_rights/` fiche it reads as an oversight.
- **Proposed fix:** Change `status: documented` to `status: published` on `_rights/vitamin-e.md`. Decide, separately, whether `documented` is a value the resource wants to keep in the vocabulary for source documents; if not, harmonize `01f26f96.md` as well.
- **Priority:** low
- **Depends on:** —

### 4. Reference template `_rights/magnesium.md` carries `last_revised: April 2025`
- **Location:** `_rights/magnesium.md` frontmatter (and, by extension, every `_rights/` page that still reads `last_revised: April 2025`: `potassium.md`, `iron.md`, `folate.md`, `omega-3.md`, `riboflavin-b2.md`, `thiamine-b1.md`, `vitamin-e.md`).
- **Nature:** These pages have been substantively touched during the 2026 editorial work (jurist pivot, cross-linking, quote adjustments), but their `last_revised` still reads *April 2025*. This gives a false signal of staleness to readers who scan the date to gauge freshness. Charter Section 2, item 9 predicts exactly this.
- **Proposed fix:** For each page, if the last substantive edit is later than April 2025, update `last_revised` accordingly. Where the page is genuinely unchanged since April 2025, leave the date and record that decision.
- **Priority:** medium
- **Depends on:** —

### 5. `_reports/` collection is orphaned from the current site architecture
- **Location:** `_reports/hypothyroidism.md`, `_reports/magnesium-deficiency.md`, `_reports/vitamin-d-deficiency.md`.
- **Nature:** All three reports are `last_revised: April 2025`, short, and not linked from the FAQ, the home page, or the Rights index. `CLAUDE.md` explicitly subordinates `_reports/` to `_rights/` (a `_reports/<nutrient>-deficiency.md` "does not replace `_rights/<nutrient>.md`"), but the current corpus has grown the `_rights/` fiches without ever wiring the reports into them. The collection is publicly indexed by `search.json` but has no editorial function.
- **Proposed fix:** Decide the fate of the collection. Either (a) upgrade each report to become a case-oriented companion to the corresponding `_rights/` page and link them from there; or (b) retire the collection (`search_exclude: true` on each file, and eventually remove them). The current in-between state is the finding.
- **Priority:** medium
- **Depends on:** —

### 6. Three `_resources/` pages are `status: draft` placeholders indexed as if published
- **Location:** `_resources/legal-texts.md`, `_resources/international-recommendations.md`, `_resources/thematic-bibliography.md`.
- **Nature:** Each is a placeholder stub carrying only a title and a note. All three are linked from the FAQ (`faq/index.md:121–122` links to `legal-texts` and `international-recommendations`; the thematic bibliography is linked from several `_rights/` bibliographies). A reader who clicks arrives on an empty page. They are also indexed by `search.json` since neither `hidden` nor `search_exclude` is set on them.
- **Proposed fix:** Either complete them (populate the thematic bibliography, list the legal texts and recommendations with citations and links) or add `search_exclude: true` and remove the FAQ links until they are populated.
- **Priority:** medium
- **Depends on:** —

### 7. Two `_legal/` pages are placeholder stubs
- **Location:** `_legal/legal-notice.md`, `_legal/accessibility.md`.
- **Nature:** Both files exist without a `status` frontmatter and contain placeholder text only. A resource that argues for a rights-based framework and links to itself on the strength of its own compliance signals should not run with an empty legal notice and an empty accessibility statement.
- **Proposed fix:** Populate legal notice (publisher identity, hosting, contact, licensing of content, any funding disclosure) and accessibility statement (conformance target, known limits, contact for remediation). Add `status: published` and `last_revised` once populated.
- **Priority:** medium (legal-notice), low (accessibility, if the site is genuinely single-author volunteer work)
- **Depends on:** —

### 8. `_critique/practical-illustrations.md` is a `status: draft` placeholder
- **Location:** `_critique/practical-illustrations.md`.
- **Nature:** The file is a stub. It is indexed by `search.json` but not linked from any published page.
- **Proposed fix:** Either write the piece (multi-nutrient case illustrations, if that is still the intent) or delete the file, or set `search_exclude: true` in the meantime.
- **Priority:** low
- **Depends on:** —

## Frontmatter and metadata

### 9. Home page and About page carry no `status` or `last_revised`
- **Location:** `index.md`, `about/index.md`.
- **Nature:** Both are effectively "published" front-door pages, but they carry no `status` and no `last_revised`, so they escape the frontmatter conventions the rest of the corpus follows. This means a future audit or a future contributor cannot tell, from the frontmatter alone, when the home page's "Recent additions" was last curated.
- **Proposed fix:** Add `status: published` and `last_revised` to both files. Update `last_revised` whenever the home page's editorial selection changes.
- **Priority:** low
- **Depends on:** —

### 10. `_definitions/physiological-rights.md` carries `last_revised: April 2026`
- **Location:** `_definitions/physiological-rights.md` frontmatter.
- **Nature:** The mother definition of the resource is dated three months before the July 2026 pivot toward a jurist readership. If it has since been read against that pivot and judged still adequate, the date should reflect that pass. If it has not been re-read, that in itself is a finding — the definition ought to be re-examined against the jurist frame the resource has adopted.
- **Proposed fix:** Re-read against the jurist pivot (see project memory `project_pivot_jurist_audience.md`). Either confirm and refresh the date, or edit the sections that would under-serve a jurist arriving cold.
- **Priority:** medium
- **Depends on:** 14

### 11. `search.json` indexes drafts and placeholders
- **Location:** `search.json` template (root); triggered by every file that lacks `search_exclude: true` while being `status: draft` or a placeholder.
- **Nature:** The Liquid loop in `search.json` pushes every document that is not `hidden` or `search_exclude`. Draft placeholders (`_resources/legal-texts.md`, `_resources/international-recommendations.md`, `_resources/thematic-bibliography.md`, `_critique/practical-illustrations.md`, `_rights/optimal-hormonal-levels.md`) are therefore surfaced in the header search box.
- **Proposed fix:** Add `search_exclude: true` to each draft/placeholder page until it is completed, or complete them.
- **Priority:** low
- **Depends on:** 1, 6, 8

## Lexicon (charter Section 1, finding #3, and Section 2, item 10)

### 12. Em-dash sweep — 550 occurrences across published content
- **Location:** Site-wide. Top offenders by count: `_rights/vitamin-e.md` (52), `_rights/magnesium.md` (48), `_rights/folate.md` (44), `_critique/behind-every-test-an-industry.md` (44), `_rights/potassium.md` (40), `_rights/omega-3.md` (37), `_critique/the-hunger-we-dont-see.md` (27), `_editorials/the-life-we-call-normal.md` (25), `_rights/riboflavin-b2.md` (20). All other files below 20.
- **Nature:** Memory `feedback_no_em_dashes.md` is unambiguous: zero em-dashes in text Claude writes. The rule was formalized during July 2026; content authored before then still contains them. 550 occurrences across 35 files is the current inventory.
- **Proposed fix:** Sweep in a dedicated session. For each occurrence, replace with comma, colon, parentheses, or sentence break, according to what the sentence actually does. Bulk regex is unsafe: the choice of replacement is contextual.
- **Priority:** medium (bulk cosmetic; changes voice signal but not argument)
- **Depends on:** —

### 13. "Precise / precisely / more precise" sweep
- **Location:** `_rights/riboflavin-b2.md:18`, `_rights/potassium.md:193`, `_rights/folate.md:165`, `_rights/omega-3.md:43`, `_rights/iron.md:55`, `_editorials/the-life-we-call-normal.md:26,31`, `_editorials/the-ferritin-threshold.md:33`, `_critique/behind-every-test-an-industry.md:161`, `_critique/false-negative-serum-potassium.md:19`, `_critique/calibrated-for-nothing.md:41`.
- **Nature:** Memory `feedback_no_word_precise.md` bans the word as an empty intensifier and a tic of AI-typical self-satisfaction. Eleven occurrences across nine published files.
- **Proposed fix:** For each occurrence, either delete the word or replace with the specific noun / adjective that the sentence is trying to reach for. If the sentence collapses without "precisely", the sentence is doing the tic's work.
- **Priority:** medium
- **Depends on:** —

### 14. "The point is that … is not X but Y" in the-life-we-call-normal
- **Location:** `_editorials/the-life-we-call-normal.md:61`.
- **Nature:** Two banned patterns in one sentence: the meta-frame "The point is …" (adjacent to the banned "What this changes / means / matters" family) and the decorative "not X but Y" (memory `feedback_trust_the_implicit.md`). The rest of the piece is otherwise voice-consistent.
- **Proposed fix:** Rewrite the sentence to state the point directly.
- **Priority:** low
- **Depends on:** —

## Jurist pivot alignment (charter Section 2, item 8)

### 15. Older `_editorials/` still calibrated for the pre-pivot generalist reader
- **Location:** `_editorials/deficiency-as-rights-violation.md`, `_editorials/the-invisible-medical-emergency.md`, `_editorials/ethical-limits-of-rcts.md`, `_editorials/proposed-reforms.md` (all `last_revised: April 2025`).
- **Nature:** These pieces predate the 2026-07-20 pivot to a jurist audience (memory `project_pivot_jurist_audience.md`). Their register is activist-generalist rather than jurist-oriented — for instance, `deficiency-as-rights-violation.md` opens with the assertion that "human rights are … absolute" without qualification, which a jurist reader will push back on before reading further. The charter is clear that these pages should not be rewritten during the audit; the finding is that they need bridge pieces or a rewrite in a follow-up session.
- **Proposed fix:** Flag only. In a follow-up session, either add jurist-facing framing at the head of each piece or write bridge editorials that route the jurist reader around them.
- **Priority:** medium
- **Depends on:** —

### 16. `deficiency-as-rights-violation.md` — absolutist framing likely to be rejected by jurists
- **Location:** `_editorials/deficiency-as-rights-violation.md` (opening section).
- **Nature:** The piece states that human rights are absolute in a register that a jurist reader trained in ECHR / ICCPR / ICESCR case law will treat as inaccurate for socio-economic rights (which are progressive, subject to maximum available resources under ICESCR Art. 2). The framing would trigger the jurist's default skepticism at the door.
- **Proposed fix:** Introduce the distinction between civil-and-political (largely absolute) and economic-social-cultural (progressive) rights, and locate the physiological-rights argument accordingly. Or rewrite the opening in the register of GC14 (which the resource already uses correctly in `_definitions/`).
- **Priority:** medium
- **Depends on:** 15

## Association → causation slips (charter Section 3, item 15)

### 17. "Associated conditions" tables across `_rights/` — audit for causal drift
- **Location:** `_rights/magnesium.md` (associated-conditions section), and the equivalent sections in `_rights/potassium.md`, `_rights/iron.md`, `_rights/folate.md`, `_rights/riboflavin-b2.md`, `_rights/thiamine-b1.md`, `_rights/vitamin-e.md`, `_rights/omega-3.md`, `_rights/choline.md`, `_rights/glutathione.md`, `_rights/coenzyme-q10.md`.
- **Nature:** Charter Section 1, finding #1 (the palpitations / potassium case) has cousins in the "associated conditions" tables of most `_rights/` pages. A reader who scans the table can slide from "condition X is associated with deficit Y" to "condition X is caused by deficit Y". The tables need a header sentence or a footer sentence that names the association-not-causation frame explicitly, once.
- **Proposed fix:** For each page, add a single framing sentence at the head of the associated-conditions section: association is not causation; the deficit is one etiology among several to be investigated; the point of the table is that the routine test does not name the deficit when present.
- **Priority:** medium
- **Depends on:** —

## Home page and landing orientation (charter Section 3, item 18)

### 18. Home page "Recent additions" is stale relative to July 2026 publications
- **Location:** `index.md` — "Recent additions" section.
- **Nature:** The list is hardcoded and does not include the recently published or substantively revised pieces of July 2026 (Self-Medication as a Codified Right, The Blunder They Called a Refutation, A Litigation Brief, Two Doses One Molecule, and the FAQ itself). It also does not reflect the 12-substrate count claimed in the FAQ.
- **Proposed fix:** Refresh the list. Longer-term, consider whether "Recent additions" should be driven by `last_revised` rather than kept hardcoded — with the caveat that the home page is *Une éditoriale* and editorial curation is deliberate, so the fix is a curated refresh, not an auto-list.
- **Priority:** medium
- **Depends on:** 4 (accurate `last_revised` first, then curate)

### 19. Home page and FAQ agree on "twelve substrates" — verify count
- **Location:** `index.md`, `faq/index.md:89`.
- **Nature:** The FAQ names twelve substrates (magnesium, potassium, iron, folate, choline, glutathione, coenzyme Q10, riboflavin, thiamine, vitamin E, omega-3, optimal hormonal levels). If `optimal-hormonal-levels.md` is retired or held back (finding #1), the count drops to eleven and the FAQ needs to be updated in the same edit.
- **Proposed fix:** After deciding the fate of `optimal-hormonal-levels.md`, reconcile the count in FAQ Q "Which nutrients are documented here?" and in any home-page rubric that references it.
- **Priority:** low
- **Depends on:** 1

## Case-report factual traceability (charter Section 2, item 12)

### 20. Hypothyroidism report cites specific TSH targets without source
- **Location:** `_reports/hypothyroidism.md` (target range statement).
- **Nature:** The report states an optimal TSH range (roughly 1–2 mIU/L) without citing the source. The number is defensible in the endocrinology literature but the resource's own convention is to cite each numerical threshold. Flagged as a low-priority cousin of the wider numerical audit.
- **Proposed fix:** Cite the source (e.g., the relevant AACE / ETA position statement, or the primary literature the resource wants to stand on) or soften the statement to a range with named authors.
- **Priority:** low
- **Depends on:** 5 (the fate of the reports collection determines whether this is worth fixing)

## Amalgamation risks (charter Section 1, finding #4)

### 21. "Supplement" vs "substrate at pharmacological dose" — verify no conflation
- **Location:** Site-wide, especially in `_editorials/the-store-that-sells-the-right/`, `_critique/two-doses-one-molecule.md`, `_definitions/self-medication-as-a-codified-right.md`, and the FAQ.
- **Nature:** The resource's argument depends on a clean distinction between (a) "supplement" as a regulatory-and-marketing category and (b) the substrate itself administered at a physiologically-motivated dose. The distinction is drawn cleanly in `two-doses-one-molecule.md` and in `self-medication-as-a-codified-right.md`, but earlier `_editorials/` predating the July 2026 work may fold them.
- **Proposed fix:** Read the April 2025 editorials against the distinction and flag any sentence that speaks of "supplements" where it should speak of "the substrate at pharmacological dose", or vice versa. Do not fix during the audit.
- **Priority:** medium
- **Depends on:** 15

### 22. "Deficit" vs "insufficiency" — verify vocabulary consistency
- **Location:** Site-wide.
- **Nature:** Some pages use "deficit" and "insufficiency" interchangeably; some reserve "deficit" for the biochemically-defined depletion and "insufficiency" for a sub-optimal state that does not yet meet the deficit threshold (the ferritin 30 / ferritin 50 discussion is the paradigm case). The resource's argument benefits from a stable convention.
- **Proposed fix:** Decide on the convention (proposal: "deficit" = below the threshold of function; "insufficiency" = between the routine-lab threshold and the function threshold). Sweep the corpus in a follow-up session.
- **Priority:** low
- **Depends on:** —

## SEO / accessibility (charter Section 3, items 19–20)

### 23. No Open Graph image configured anywhere
- **Location:** Site-wide; `_config.yml`, `_includes/head.html` (if any).
- **Nature:** `jekyll-seo-tag` is installed and per-page `description` frontmatter is present, but there is no `image` frontmatter and no site-wide default OG image. Social previews will fall back to plain text cards. The charter (Section 3, item 19) asks whether this is a conscious choice.
- **Proposed fix:** Either add a site-wide default OG image (a plain typographic card carrying the resource name and tagline) or confirm the choice not to.
- **Priority:** low
- **Depends on:** —

### 24. Accessibility statement is empty
- **Location:** `_legal/accessibility.md`.
- **Nature:** See finding #7. Also relates to charter Section 3, item 20 (accessibility): heading order, alt text on images, contrast on accent color used by search-result badges, keyboard navigability. This audit did not perform a full accessibility pass, only flagged the empty statement.
- **Proposed fix:** Run an actual accessibility pass (WAVE, axe, keyboard-only navigation of the search panel) before populating the statement.
- **Priority:** low
- **Depends on:** 7

## Cross-referencing coherence (charter Section 2, item 6)

### 25. Recurring critique phrases not consistently linked on first use
- **Location:** Site-wide. Example: "the false negative of serum potassium" appears across `_rights/potassium.md`, `faq/index.md`, `_editorials/`, and elsewhere, but not every occurrence links to `_critique/false-negative-serum-potassium.md` on first use. Similar phrases: "the ferritin threshold", "otherwise healthy", "calibrated for nothing", "two doses, one molecule".
- **Nature:** A reader who encounters the phrase for the first time on any given page should have a one-click path to the critique that develops it. The current cross-linking is uneven.
- **Proposed fix:** For each recurring conceptual phrase, sweep the corpus and link on first use per page.
- **Priority:** medium
- **Depends on:** —

## Bibliography consistency (charter Section 3, item 23)

### 26. Citation style varies across `_rights/` bibliographies
- **Location:** `_rights/*.md` (bibliography sections).
- **Nature:** Some bibliographies use footnote-style references with numeric anchors (e.g. `_rights/folate.md`); others use inline citations; DOI presence is uneven; author-name order is not uniform. The charter (Section 3, item 23) asks for consistency.
- **Proposed fix:** Decide the house citation style (proposal: author-year-title with DOI where available, no numeric footnotes) and sweep in a follow-up session.
- **Priority:** low
- **Depends on:** —

---

## Items checked and cleared (no finding needed)

- **Broken internal links.** 174 markdown links across all content collections were resolved against the collection permalinks declared in `_config.yml`. 0 broken. Liquid variants in layouts and includes also resolved cleanly.
- **French calques in published content.** None surfaced. Calques appear in `_inbox/` drafts (out of scope) and in `_resources/01f26f96.md` (Mayer 1979 French original, intentional).
- **Legal citations spot-checks.** Alma-Ata Article IV and Article VII, Oviedo Convention Article 5, ICESCR Article 12 read through General Comment 14 §43, ICESCR Article 11 read through General Comment 12 §8, TAC v. Minister of Health (SA 2002), Urgenda, T-760/08 — all accurate as cited in `_definitions/self-medication-as-a-codified-right.md`, `_definitions/the-instruments-already-exist.md`, and `_definitions/a-litigation-brief.md`.
- **Numerical thresholds spot-checks.** Ferritin cutoffs (15 / 30 / 50 μg/L), thiamine 400× RDA at Wernicke's dose, B12 400× RDA at injection, ROMK / magnesium-potassium co-requirement — all traceable to the bibliographies of the corresponding `_rights/` pages.
- **"This site" self-designation.** No occurrences in published content (memory `feedback_self_designation_resource.md`). "Site" appears only in the audit charter itself and in code / build files.
- **Featured flags.** `_definitions/all-medicine-is-preventive.md` and `_editorials/you-are-not-the-exception.md` both correctly carry `featured: true`; no unintended featured pages surfaced.

---

*End of findings list. Perig validates or rejects item by item. Rejected items should stay in this file with a "REJECTED (reason)" marker so the next audit does not re-raise them.*
