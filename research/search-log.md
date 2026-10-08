# Search log

Every automated or manual search pass that feeds the BrainLift is logged here. Times are US Central (CT).
Raw outputs per pass live in `research/deep-research/<pass>/`. Scrape working copies stay on hdx-lab in `~/code/deep-research/output/`.

## Tooling for automated passes

- **Tool:** fork of [dzhng/deep-research](https://github.com/dzhng/deep-research) (upstream `1f8f3e2`) on hdx-lab, local branch `provenance`. The provenance patch is commit `b16a237` and the query files are commit `bb09770`. The patch saves every learning with its source URL and a verbatim supporting quote, checks that quote against the scraped page, and keeps the raw page markdown.
- **Model:** `openai/gpt-5-mini` via OpenRouter. It is used for query generation, learning extraction and report writing.
- **Search/scrape, pass 1:** Firecrawl cloud search API (free plan, 1,000 credits per month, concurrency 2). Each search returned up to 5 results, and every result was scraped to markdown.
- **Search/scrape, passes 2–4:** self-hosted Firecrawl (`v2.11.486`, Docker on hdx-lab, `~/code/firecrawl`) with a self-hosted SearXNG metasearch backend. Engines used: Google CSE, DuckDuckGo, Startpage, Google Scholar, Semantic Scholar and OpenAlex. Scholarly hits often resolve through `oadoi.org` (Unpaywall) to open-access full text. It runs at no per-page cost, with concurrency 3 and 4 kept results per search (2 extra fetched to replace filtered ones). The fork at commit `603a808` adds:
  - truncation of pages over 150k characters (recorded in `pages/index.jsonl` and in `evidence.source_truncated`)
  - skipping of YouTube, social and forum domains, bulk documents (abstract books, programmes, proceedings) and bot-wall pages under 500 characters (logged in `pages/skipped.jsonl`)
  - re-fetching of PMC/PubMed pages through Europe PMC (`fetched_via` is recorded and the NCBI URL is kept)
  - the original pass brief re-sent to every query-generation and extraction call, with short search-engine-style queries required
- **Verification:** `scripts/verify-quotes.py` re-checks each `supporting_quote` against the saved page text, using whitespace- and markdown-normalized exact substring matching. A verified quote shows that the passage exists on the page. It does **not** show that the learning is a fair reading of the source or that the source is credible.

## Passes

| Pass | When (CT) | Query file | Breadth / depth | Searches | Pages scraped | Evidence records | Quotes verified | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smoke-interleaved (tool test) | 2026-10-07 8:07–8:09 PM | inline: "evidence on interleaved vs blocked practice for intermediate guitarists" | 2 / 1 | 2 | 10 | 6 | 6/6 | $0.028 OpenRouter, 35 Firecrawl credits |
| pass1-theory-integration | 2026-10-07 8:47–8:53 PM | `deep-research/pass1-theory-integration/query.md` | 3 / 2 | 9 | 42 unique (44 returned) | 27 | 20/27 | $0.19 OpenRouter, **1,005 Firecrawl credits** |
| smoke-selfhost (tool test) | 2026-10-07 9:13–9:15 PM | inline: "blocked vs interleaved practice schedules in music instrument learning: effects on retention and transfer" | 2 / 1 | 2 | 5 kept (1 skipped) | 6 | 4/6 | $0.011 OpenRouter, $0 Firecrawl |
| pass2-expertise-development | 2026-10-07 9:17–9:19 PM | `deep-research/pass2-expertise-development/query.md` | 3 / 2 | 9 | 39 returned, 2 skipped, 4 truncated | 27 | 18/27 | ~$0.13 OpenRouter, $0 Firecrawl |
| pass3-adaptive-instruction | 2026-10-07 9:20–9:22 PM | `deep-research/pass3-adaptive-instruction/query.md` | 3 / 2 | 9 | 32 returned, 6 skipped, 5 truncated | 24 | 18/24 | ~$0.15 OpenRouter, $0 Firecrawl |
| pass4-recording-assessment | 2026-10-07 9:23–9:26 PM | `deep-research/pass4-recording-assessment/query.md` | 3 / 2 | 9 | 38 returned, 4 skipped, 3 truncated | 25 | 15/25 | ~$0.15 OpenRouter, $0 Firecrawl |

Per-pass OpenRouter figures are deltas in key usage, which updates with a short lag. Passes 2–4 together cost $0.49.

Smoke-run outputs were not copied into this repo. They are on hdx-lab under `~/code/deep-research/output/smoke-*/`.

## Notes on pass1-theory-integration

- **Credit blow-out.** Firecrawl charges per PDF page. Several results were very long PDFs and pages: a 2019 SMPC abstract book (~960k characters), a DiVA thesis PDF (~875k), the 2020 Society for Music Theory programme PDF (~360k) and several dissertations. That single pass used the whole free-plan allowance and left the account at −40 credits. Passes 2–4 were stopped automatically by the batch runner's credit guard. The pre-run estimate (~160 credits per pass) was based on a smoke run with short pages and was far too low.
- **Source quality is weak for the decision at hand.** 3 of the 27 records cite YouTube and several cite marketing or course pages (Berklee Online course page, wpmusicacademy.com, teoria.com, CIM graduate entrance requirements). Many records are off-topic:
  - choir singing and speech-in-noise in older adults
  - mindfulness for conservatoire students
  - collegiate jazz-education history
  - Gordon aptitude-test validity
  - an instrument-timbre placement dissertation
  - cognitive far-transfer from childhood instrumental training

  The second-level queries drifted. For example, "chunking mindfulness neuroscience myelination" came from a dissertation found at level 1.
- **No record directly answers the core question**, which is controlled evidence that theory-in-practice transfers better than theory-first for adult guitarists. The closest leads to read in full:
  - Karpinski on holistic aural-skills pedagogy and tonic inference (MTO 2021)
  - a randomized N=73 study of Gordon learning-sequence instruction (shareok.org thesis; quote unverified, near-match)
  - a Kodály modality-sequence qualitative study (St Thomas)
  - a meta-analysis of instrumental training on cognitive outcomes (ScienceDirect S1747938X22000057; far transfer only, children)
- **Unverified quotes (7):** all near-misses rather than invented text. They came from passages stitched with "…", joined list items, or small edits, with exact verbatim runs of 50–95% of the quote. They still need manual checking before use.
- **report.md overclaims.** It states that the evidence is "strongest" for aural-first approaches and refers to "several controlled studies", which the evidence records do not support. Treat the report as an unreviewed AI synthesis and work from `evidence.jsonl` instead.

## Notes on passes 2–4 (self-hosted stack)

- **Source quality improved a lot.** Most records now cite peer-reviewed or open-access papers (Frontiers, PMC, Springer, Nature, arXiv) or theses. No YouTube page reached the model.
- **Off-topic drift remains at depth 2.** Follow-up questions widen into neighbouring fields. Examples:
  - pass 2: dance interventions in older adults, COVID-era musician careers, executive function in musicians
  - pass 3: music training and children's executive function or phonological awareness, PTSD in veterans (Guitars for Vets), speech-assessment reliability, guitar acoustics
  - pass 4: surgical-simulation AI assessment, gait classification, virtual-team ratings, audio restoration, LLM grading of text answers

  Filter these out when building the evidence table.
- **Coverage gaps.** Breadth 3 covers about 3 sub-questions per pass.
  - Pass 3 found almost nothing on fixed-versus-adaptive curricula, on how reliably learner bottlenecks can be diagnosed, or on feedback timing and amount (guidance hypothesis, self-controlled feedback).
  - Pass 2 found little on adult plateaus beyond one longitudinal improvisation study of uncertain quality (`10.5216/mh.v25.82965`).

  These need targeted manual searches.
- **Weaker source types still present:**
  - preprints (a medRxiv meta-analysis of guitarist injury prevalence; an erhu assessment study on Research Square)
  - a UC Berkeley MIDS capstone page (Fretwork)
  - Scribd lecture notes
  - ProQuest "openview" stubs, where only the title is quotable
  - a fuzzy-control "adaptive instruction" paper with simulated metrics
- **Paywalls and bot walls.** JSTOR, ScienceDirect, IEEE PDFs, some `oadoi.org` redirects and old-style `ncbi.nlm.nih.gov/pubmed/<id>` URLs returned bot walls and were skipped. The Europe PMC rescue only matches `pubmed.ncbi.nlm.nih.gov` and PMC URLs.
- **Unverified quotes (25 across passes 2–4).** Almost all are near-misses: "…"-stitched passages, OCR artefacts in old PDFs (e.g. "U" for "4"), or small edits, with exact runs of roughly 30–98% of the quote. One off-topic pass-4 record (virtual-team ratings, `doi.org/10.1007/s10111-018-0499-6`) had no matching text. Check every quote by hand before use.
- **report.md files are unreviewed AI syntheses.** Do not cite them. Work from `evidence.jsonl` and the original sources.

## Lessons for any further automated passes

- Done in `603a808`: page caps, carrying the brief into deeper levels, short queries, domain and bulk filtering, and self-hosting (no credit cost).
- Still open: run narrower single-question passes (for example "guidance hypothesis feedback frequency motor learning meta-analysis") to fill the coverage gaps above, and add a relevance filter so off-topic records are dropped before they are written.
