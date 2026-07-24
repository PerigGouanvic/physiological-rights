---
title: Audit charter
status: internal
created: 2026-07-24
scope: future audit session
---

# Audit charter — physiological-rights resource

**Purpose.** Systematically pass over the site to catch the classes of error surfaced during recent editorial work (July 2026), the errors those examples let us predict, and the unknown unknowns worth surveying while the pass is happening. The output of the audit session is a numbered list, one item per finding, so that Perig can validate or reject each correction individually.

**When to run.** As a dedicated session, not folded into content work. Uses this file as its brief.

**Do not publish.** This folder is in `_config.yml`'s `exclude`. It exists to let future sessions ground themselves.

---

## Section 1 — Observed errors (already surfaced)

Errors that occurred in the recent editorial work and set the tone for the audit. Every one of them may have close cousins elsewhere in the corpus. The audit must look for those cousins, not just fix the original.

1. **Causal shortcuts.** The FAQ Q5 (potassium / palpitations) was written in a way that let the reader infer palpitations → probably potassium. Palpitations have many etiologies (thyroid, iron, primary arrhythmia, stimulants, dehydration, anxiety), and the site's actual claim is narrower: serum K is a poor proxy for intracellular K, so a normal serum test does not rule K out as *one* cause among the ones to investigate. Look across `_rights/` and `_critique/` for analogous slips: "symptom X — nutrient Y is missed by the routine test" that reads as "symptom X is caused by deficit Y".

2. **Recency bias in link selection.** When the FAQ was first drafted, the "what is a physiological right" entry linked to argumentative pieces (`all-medicine-is-preventive`, `a-litigation-brief`, `the-instruments-already-exist`) but not to the actual mother definition (`_definitions/physiological-rights.md`). The trigger was picking the freshest pages read, not the pages a reader arriving at the question actually needs. **Discipline for the audit:** before writing a link list, `ls` the relevant folder and select from the full inventory, not from working memory.

3. **AI-typical lexicon leakage.** Perig has documented rules against em-dashes, against the word "precise", against "what this changes / matters / means", against "the takeaway", against "not X but Y" as decoration. The audit should grep for these across published content and flag every occurrence with its context, so Perig can decide keep / edit / cut.

4. **Amalgamation between distinct concepts.** I conflated `/out.txt` (talk-to-site author channel) with the ADA concept (not yet incarnated) in conversation. Analogous conflations in *published* text would be more consequential (e.g., collapsing "physiological right" and "right to health"; collapsing "supplement" and "orthomolecular dose"; collapsing "deficit" and "insufficiency"). Flag them.

## Section 2 — Guessable manquements

Errors the observed ones let us predict.

5. **Definitional pages under-linked from `_rights/`.** Each `_rights/*.md` page should point back to the framework in `_definitions/` (at minimum `physiological-rights.md`), so a reader who arrives on a nutrient fiche via search understands what a "right" means here. Audit: does each of the 12 `_rights/` pages carry that link?

6. **Cross-referencing coherence.** Where a page cites a concept developed elsewhere (e.g., "the false negative of serum X" appears across pages), the citing page should link to the critique. Audit: for each recurring conceptual phrase, does every occurrence link on first use?

7. **Model conformance of `_rights/` pages.** `magnesium.md` is the reference template: history, named researchers, test critique, mechanism, associated conditions, timeline, bibliography. The other 11 substrates (potassium, iron, folate, choline, glutathione, CoQ10, riboflavin, thiamine, vitamin E, omega-3, optimal hormonal levels) should each be measured against that structure. Flag missing sections.

8. **Jurist pivot alignment.** Since the 2026-07-20 pivot toward jurists as an intended readership, most existing pages are still calibrated for a general reader. The audit should not rewrite them (bridge pieces will do that work), but it should flag pages whose framing would confuse or under-serve a jurist arriving cold — especially the `_definitions/` and `_critique/` clusters.

9. **Frontmatter consistency.** `status`, `last_revised`, `description`, `permalink` conventions across collections. Any page missing one? Any `status: draft` that is actually published? Any `last_revised` from before the last substantial edit?

10. **Em-dash and IA-lexicon sweep on content predating the rules.** The no-em-dash rule and the no-"precise" / no-"what this changes" rules were formalized during July 2026. Content authored before likely still has them. Grep-based inventory needed.

11. **French calques in the English text.** Perig writes in a francophone rhythm and often produces "chez la femme adulte" → "in the adult woman", "à même le menu" → literal English constructions. His voice must be preserved (see `feedback_correct_language_preserve_voice.md`), but calques that read as broken English should be corrected. This requires close reading, not grep.

12. **Numerical thresholds — factual audit.** Ferritin cutoffs, RDA multiples, dose numbers, ROMK claims, prevalence figures. Each numerical claim should be traceable to a source in the bibliography or in `kb/`. Flag numbers that appear without traceable support.

13. **Legal claims — factual audit.** Every citation of the Alma-Ata Declaration, the ICESCR, the Oviedo Convention, DSHEA, Regulation 1924/2006, etc. should reference the actual article or provision correctly. Flag broad handwavey citations ("the WHO recognizes...") that don't survive a check.

14. **"Resource" vs "site" self-designation.** The rule (`feedback_self_designation_resource.md`) is that editorial content refers to itself as "resource", not "site". Grep the collections for "this site" and check whether each occurrence is a legitimate reference to the Jekyll implementation or a slip.

## Section 3 — Unknown unknowns

Categories of problem to actively look for rather than to fix in a predictable way.

15. **Association → causation slips beyond the palpitations case.** Any page that lists conditions "associated with" a deficit runs the risk of implying the deficit is *the* cause. Audit the "associated conditions" tables of each `_rights/` page for this drift.

16. **Over-generalization from single studies or single cases.** Series of cases and single trials appear in the corpus (Cochrane on riboflavin/migraine, WHI on Premarin, etc.). Where the site draws general conclusions from one dataset, is the epistemic qualification present?

17. **Clinical advice buried in editorial text.** The site is emphatically not a source of individualized clinical advice, but wording that reads as "you should take X mg" can appear without safeguards. Flag paragraphs that a first-time reader could mistake for a personalized dose recommendation.

18. **Landing-page orientation.** `index.md` (Home Option A — Une éditoriale) is the front door. Does it still orient a reader who has never heard of physiological rights? Does its rubric list still match the actual state of the corpus (12 rights, N critiques, etc.)?

19. **SEO / Open Graph / social-preview metadata.** `jekyll-seo-tag` is installed. Is every published page carrying a usable `description` and `title`? Are OG images set anywhere, and if not, is that a conscious choice?

20. **Accessibility.** Heading order, alt text on images, contrast on the accent color used by search-result badges, keyboard navigability of the search panel outside the shortcuts already implemented.

21. **`search.json` performance and content.** With 12 rights + growing collections, is the client-side index still small enough to load fast on mobile? Are pages that should be excluded from search (drafts, legal boilerplate) opted out via `search_exclude`?

22. **Broken internal links.** Every link in the FAQ, in cross-references, in "Read next" sections. Are any 404?

23. **Bibliography formatting.** Consistency across `_rights/` bibliographies: citation style, DOI presence, author name order, italicization.

## Section 4 — Deliverable format

The audit session's output is a **single numbered list**, appended to a file the audit session creates (e.g. `_audit/2026-XX-audit-findings.md`). Each numbered item follows this shape:

```
### N. [Short label of the finding]
- **Location:** file path (or "site-wide") + line range if applicable
- **Nature:** what the problem is, in one or two sentences
- **Proposed fix:** what would be changed, in one or two sentences
- **Priority:** high / medium / low
- **Depends on:** other item numbers, if any
```

Perig validates or rejects item by item. Rejected items stay in the file with a "REJECTED (reason)" marker so the next audit does not re-raise them.

## Section 5 — Scope

**In scope.** All content collections (`_rights/`, `_definitions/`, `_critique/`, `_editorials/`, `_reports/`, `_resources/`, `_legal/`, `about/`, `faq/`, `index.md`), layouts and partials that render them, `search.json` content, frontmatter.

**Out of scope.** Any refactor of `assets/css/style.css` beyond flagging accessibility issues. The ADA integration chantier (see `project_ada_vs_out_txt_distinction.md`) is separate. The KB (`kb/`) is separate. New content generation is out — the audit is a pass over existing state, not a writing session.

## Section 6 — Method

- Load this charter first.
- List each target folder before writing any finding for it, so recency bias in file selection is neutralized.
- Use grep for lexical rules (em-dash, banned words, self-designation), close reading for everything else.
- Cross-check against `~/.claude/projects/-home-perig-projects-physiological-rights/memory/` before flagging anything — a finding may already be documented as a deliberate choice.
- When in doubt whether something is a bug or a voice choice of Perig's, flag it as low-priority with the ambiguity noted rather than silently pass.
- Do not fix during the audit. The output is findings only. Fixes happen in a follow-up session where Perig has validated the list.
