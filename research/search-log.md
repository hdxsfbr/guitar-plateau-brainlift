# Search log

Every automated or manual search pass that feeds the BrainLift is logged here. Times are US Central (CT).
Raw outputs per pass live in `research/deep-research/<pass>/`. Scrape working copies stay on hdx-lab in `~/code/deep-research/output/`.

## Tooling for automated passes

- **Tool:** fork of [dzhng/deep-research](https://github.com/dzhng/deep-research) (upstream `1f8f3e2`) on hdx-lab, local branch `provenance`. The provenance patch is commit `b16a237` and the query files are commit `bb09770`. The patch saves every learning with its source URL and a verbatim supporting quote, checks that quote against the scraped page, and keeps the raw page markdown.
- **Model:** `openai/gpt-5-mini` via OpenRouter. It is used for query generation, learning extraction and report writing.
- **Search/scrape:** Firecrawl search API (free plan, 1,000 credits per month, concurrency 2). Each search returns up to 5 results, and every result is scraped to markdown.
- **Verification:** `scripts/verify-quotes.py` re-checks each `supporting_quote` against the saved page text, using whitespace- and markdown-normalized exact substring matching. A verified quote shows that the passage exists on the page. It does **not** show that the learning is a fair reading of the source or that the source is credible.

## Passes

| Pass | When (CT) | Query file | Breadth / depth | Searches | Pages scraped | Evidence records | Quotes verified | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| smoke-interleaved (tool test) | 2026-10-07 8:07–8:09 PM | inline: "evidence on interleaved vs blocked practice for intermediate guitarists" | 2 / 1 | 2 | 10 | 6 | 6/6 | $0.028 OpenRouter, 35 Firecrawl credits |
| pass1-theory-integration | 2026-10-07 8:47–8:53 PM | `deep-research/pass1-theory-integration/query.md` | 3 / 2 | 9 | 42 unique (44 returned) | 27 | 20/27 | $0.19 OpenRouter, **1,005 Firecrawl credits** |
| pass2-expertise-development | not run | `queries/pass2-expertise-development.md` (fork repo) | planned 3 / 2 | – | – | – | – | – |
| pass3-adaptive-instruction | not run | `queries/pass3-adaptive-instruction.md` (fork repo) | planned 3 / 2 | – | – | – | – | – |
| pass4-recording-assessment | not run | `queries/pass4-recording-assessment.md` (fork repo) | planned 3 / 2 | – | – | – | – | – |

Smoke-run outputs were not copied into this repo. They are at `~/code/deep-research/output/smoke-interleaved/` on hdx-lab.

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

## Lessons for any further automated passes

- Cap PDF cost: exclude `.pdf` results or set `SEARCH_LIMIT` lower, and add a per-page character/credit guard before scraping. Alternatively, search without scraping and fetch selected full texts manually.
- Carry the original brief (population and source preferences) into deeper-level queries. Upstream only passes the research goal and follow-up questions downward.
- Keep queries short. The model generated long boolean strings full of quoted phrases, which return few relevant results.
