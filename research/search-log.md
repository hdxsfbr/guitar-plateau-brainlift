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

## Manual targeted searches (Task 4, Part A)

These were run by Grok Bot on 2026-10-07 with WebSearch/WebFetch and the public Europe PMC, OpenAlex and ERIC APIs, called from the box with Python. Firecrawl was not used and there was no OpenRouter spend. Times are CT; "~" means approximate, reconstructed from file timestamps.

**Search themes**
1. fixed vs adaptive instruction, ITS, mastery learning and ATI
2. reliability of diagnosis: CDMs, knowledge tracing and music rater reliability
3. feedback: the guidance hypothesis, reduced and self-controlled feedback, and music-specific feedback
4. adult self-regulated learning (SRL) and adherence

Where an original could be read, short verbatim quotes were captured with page or section. Each one is stored in `research/manual-sources/<source_id>.md` as the quote with ±250 characters of surrounding text, and re-checked by script against the saved text. Full-text PDFs stayed on the box and are not committed. The "kept/excluded" column records what entered `source-register.csv`.

| When (CT) | Tool | Query / target | Kept / excluded |
|---|---|---|---|
| 2026-10-07 9:41 PM CT | WebSearch | VanLehn 2011 relative effectiveness of human tutoring intelligent tutoring systems effect size 0.76 Educational Psychologist | kept: VanLehn 2011 (ERIC EJ946764 abstract + author PDF Table) |
| 2026-10-07 9:41 PM CT | WebSearch | Kulik Fletcher 2016 effectiveness of intelligent tutoring systems meta-analytic review | kept: Kulik & Fletcher 2016 (ERIC EJ1090502 abstract) |
| 2026-10-07 9:41 PM CT | WebSearch | Ma Adesope Nesbit Liu 2014 intelligent tutoring systems and learning outcomes meta-analysis | kept: Ma et al. 2014 (ERIC EJ1049508 abstract) |
| 2026-10-07 9:41 PM CT | WebSearch | Kulik Kulik Bangert-Drowns 1990 effectiveness of mastery learning programs meta-analysis | kept: Kulik, Kulik & Bangert-Drowns 1990 (abstract + full-text PDF p.~269) |
| 2026-10-07 ~9:42 PM CT | WebFetch | scitepress.org CSEDU 2026 paper 147268 (Elsadat et al. MAB ear-training tutor) full text | kept: Elsadat et al. 2026 (full text §4.2, §5) |
| 2026-10-07 ~9:42 PM CT | WebSearch | Pashler McDaniel Rohrer Bjork 2008 learning styles meshing hypothesis crossover interaction; Cronbach Snow aptitude-treatment interaction critique | kept: Pashler et al. 2008 (via quote in Springer 2025 review 10.1007/s10648-025-10002-w); Cronbach & Snow 1977 quote via same review (secondary). excluded: blog/learning-styles popular pages |
| 2026-10-07 ~9:42 PM CT | WebSearch | cognitive diagnostic models reliability attribute classification Templin Bradshaw | kept as metadata only: Templin & Bradshaw 2013 (not read; caution). excluded: CDM software tutorials |
| 2026-10-07 ~9:42 PM CT | WebSearch | knowledge tracing reliability student parameter estimates learning rate Pelánek; Liu Koedinger 2017 EDM | kept: Liu & Koedinger 2017 EDM (full text); Pelánek 2017 metadata only (abstract not retrieved). excluded: BKT tutorials/blogs |
| 2026-10-07 ~9:43 PM CT | WebSearch + WebFetch | Bergee 2003 faculty interjudge reliability music performance evaluation JRME (Sage timed out; Gale 404; abstract later via OpenAlex API) | kept: Bergee 2003 (abstract) |
| 2026-10-07 ~9:43 PM CT | WebSearch | Wesolowski Wind Engelhard rater precision / rater fairness music performance assessment Rasch | kept: Wesolowski et al. 2016 Music Perception (abstract via OpenAlex); Wesolowski et al. 2015 Musicae Scientiae (search summary only -> caution); lead: rater cognition typology 10.1177/0305735616665004 (abstract) |
| 2026-10-07 ~9:43 PM CT | WebSearch + WebFetch | Thompson Williamon 2003 evaluating evaluation musical performance assessment research tool; researchonline.rcm.ac.uk eprint 2170 | kept: Thompson & Williamon 2003 (abstract, RCM repository) |
| 2026-10-07 ~9:43 PM CT | WebFetch (Europe PMC REST) | PMCID:PMC11496144 (PMC direct fetch 403) | kept: Moura et al. 2024 solo music performance assessment criteria systematic review (abstract) |
| 2026-10-07 ~9:43 PM CT | WebSearch + Europe PMC REST | Salmoni Schmidt Walter 1984 knowledge of results and motor learning review guidance hypothesis | kept: Salmoni et al. 1984 (metadata; no abstract in PubMed record -> claim from search summary, caution) |
| 2026-10-07 ~9:43 PM CT | WebSearch + WebFetch | Winstein Schmidt 1990 reduced frequency of knowledge of results enhances motor skill learning (krigolson PDF 404; abstract via bisp-surf.de) | kept: Winstein & Schmidt 1990 (abstract) |
| 2026-10-07 ~9:43 PM CT | WebSearch + Europe PMC REST | Wulf Shea 2002 principles derived from simple skills do not generalize to complex skill learning; Wulf Shea Matschiner 1998 frequent feedback complex skill | kept: Wulf & Shea 2002 (abstract); Wulf, Shea & Matschiner 1998 (abstract). excluded: Reid & Swafford 2020 rats; Chiviacowsky 2010 Parkinson's (off-population) |
| 2026-10-07 ~9:43 PM CT | WebSearch + WebFetch | McKay Yantha Hussien Carter Ste-Marie 2022 self-controlled motor learning meta-analysis Meta-Psychology | kept: McKay et al. 2022 Meta-Psychology (abstract) |
| 2026-10-07 ~9:43 PM CT | WebSearch + Europe PMC REST | Chiviacowsky Wulf 2002 self-controlled feedback RQES | kept: Chiviacowsky & Wulf 2002 (abstract). excluded: Down syndrome / children follow-ups (off-population) |
| 2026-10-07 ~9:43 PM CT | WebSearch | augmented feedback music instrument learning systematic review real-time visual feedback retention | kept: Blanco, Tassani & Ramirez 2021 violin RCT (abstract via Europe PMC; same study as pass4 record); Sensory feedback integrative review 10.1177/0305735620928397 (abstract); augmented piano survey 10.1145/3567719 (abstract). excluded: cogneurosociety blog |
| 2026-10-07 ~9:43 PM CT | WebSearch + OpenAlex API | Wong Chen Lim 2021 learning melodic musical intervals block or interleave | kept: Wong, Chen & Lim 2021 Psychology of Music (abstract; numeric results from search summary of author PDF -> caution on numbers) |
| 2026-10-07 ~9:43 PM CT | WebSearch + OpenAlex API | adult amateur musicians practice adherence dropout self-regulation motivation | kept: Krause et al. 2019 dropping out/dropping in (abstract); Ritchie 2018 adult beginner SRL pilot (abstract); adult self-directed learning qualitative 10.1177/0255761421991596 (abstract); Who stays who goes 2024 (abstract; children/adolescents in music schools -> adjacent). excluded: Slovenian dropout qualitative (children), SDT university-student PDF (not read), parenting-style lifelong intention |
| 2026-10-07 ~9:44 PM CT | OpenAlex API | self-regulation and music learning systematic review (Varela, Abrami & Upitis); McPherson SRL chapter; SRL microanalysis musicians; psychological interventions self-regulated enhancement music performance systematic review | kept: Varela et al. 2016 (abstract); Osborne/McPherson et al. 2024 Musicae Scientiae interventions review (abstract); SRL microanalysis 2017 (abstract, case study -> caution). excluded: e-book design paper, flow case study, children's tech thesis |
| 2026-10-07 ~9:44 PM CT | OpenAlex API + Europe PMC REST | meta-analysis reduced relative feedback frequency motor learning (McKay et al. 2022 PSE / PsyArXiv); Sigrist augmented feedback review; bandwidth KR | kept: McKay, Hussien et al. 2022 feedback-frequency meta-analysis (preprint abstract; published PSE 102165); Sigrist et al. 2013 (abstract). excluded: small bandwidth-KR keypad/volleyball studies (low n, not decision-relevant), Sensors 2024 postural single study |
| 2026-10-07 ~9:44 PM CT | OpenAlex API | music teachers error detection accuracy (teacher diagnostic agreement) | excluded: LSU error-detection dissertation & sight-reading priming (music majors / HS; tangential). Gap: no direct study of teacher agreement on *diagnosing* a learner's bottleneck found |
| 2026-10-07 ~9:45–9:47 PM CT | curl (box) of open full texts found above | PDFs: VanLehn 2011, Ma 2014, Kulik 1990, Elsadat 2026, Wong 2021, McKay 2022 Meta-Psychology, Liu & Koedinger 2017, Krause 2019; McKay 2022 PSE PsyArXiv download returned HTML | kept: full texts converted to text for quote checks (PDFs not committed). McKay 2022 PSE quoted from abstract only. |
| 2026-10-07 ~9:48 PM CT | WebFetch | Hattie & O'Leary 2025 learning styles matching meta-meta-analysis (Springer page; curl returned only a stub) | kept: Hattie & O'Leary 2025 (verbatim excerpts saved from the fetched page: d = 0.04 across 143 studies) |
| 2026-10-07 ~9:49 PM CT | Europe PMC REST | Hohagen Immerz 2024 focus of attention music performance systematic review | kept: Hohagen & Immerz 2024 (abstract + open full text) |
| 2026-10-07 ~9:49 PM CT | WebSearch | "Insights about practice from the perspective of motor learning: a review" Wulf Mornell Music Performance Research 2008 | kept: Wulf & Mornell 2008 (confirms the Elicit row; used as expert advice only) |
| 2026-10-07 ~9:50–9:59 PM CT | OpenAlex API (works by DOI/title) | Metadata, DOI and author checks for deep-research pass records and Elicit rows (e.g. Samani & Pan 2021, Li & Liu 2025, Wang & Li 2026, Guan et al., Liu et al. 2025, Passalenti 2019, Zhang 2024, Rotter 2020, Bittner 2022) | kept: corrected authors/years in source-register (e.g. the pass record said "Rohrer" for Samani & Pan 2021). No new sources added from this step. |

**Gaps the searches did not fill**
- No study measured whether teachers agree on *which* bottleneck is holding a learner back. The one search on this returned only error-detection studies of music majors and high-school students.
- No controlled study of adult intermediate guitarists, plateaus or adaptive tutoring was found.
- The full texts of Salmoni et al. 1984, Templin & Bradshaw 2013, Pelánek 2017, Bergee 2003 and Wesolowski et al. were not read. Those sources are flagged caution or used at abstract level only.

## Building the source register and evidence table (Task 4, Parts B–C)

- `research/source-register.csv` has 136 sources, deduplicated by study identity (DOI, or author + year + title) across the Elicit export (31 rows), the evidence records from deep-research passes 1–4 (103 records) and the Part A searches. `origin_records` maps every Elicit row and every pass record to one source; the build script checks that nothing is left unmapped.
  - Duplicates merged include:
    - Elicit rows 4/5 (Hartz)
    - Elicit rows 11/13 (Macnamara)
    - pass2#07/#22/#24 (Rotter)
    - pass2#06/#25 (Castillo)
    - four Bittner/Basic Pitch records
    - Solstad (5 records)
  - Author attributions in the pass records were checked against OpenAlex. For example, pass3#06/#23 attributed the physics study to "Rohrer et al." when it is by Samani & Pan.
- `research/evidence.csv` has 92 claim rows from kept and caution sources only. YouTube, marketing, off-topic, paywall-stub and pirate-copy records are excluded; they are listed in the register with `quality_flag = exclude` and a reason.
  - Every supporting quote was re-checked against saved text: the deep-research `pages/` copy, the full text downloaded on the box, the abstract text from Europe PMC/OpenAlex/ERIC, or the Elicit export.
  - The normalization used is NFKC, whitespace, quote and dash characters, and markdown link targets.
  - Result: 90 `yes`, 2 `near`, 0 `no`.

### Re-check of near-miss and unverified pass quotes

| Record | Original status | Disposition |
|---|---|---|
| pass1#26 | not verified | Replaced with the exact abstract sentence → yes |
| pass2#03 (Ericsson 2021) | not verified | Matches only after joining a PDF line-break hyphen ("indi- vidualized") → **near** (E046) |
| pass2#04 | not verified | Two exact segments joined with "…" → yes |
| pass2#06 (Castillo 2025) | not verified | Matches only after removing medRxiv line numbers → **near** (E051). pass2#25 is a duplicate. |
| pass3#07 | not verified | The model had dropped the words "with recovery during rest-from-deliberate-learning". Restored verbatim → yes |
| pass4#00 | not verified | Trimmed to an exact span → yes |
| pass4#02 | not verified | **Contained an invented clause** ("for which we are constrained by Spotify's Basic Pitch…"). Replaced with the verbatim quote from pass4#22 → yes |
| pass4#09 | not verified | Trimmed to drop a "Fig. [1]" link artefact → yes |
| pass4#16 | not verified | Shortened to an exact span → yes |
| pass4#23, pass4#24 | not verified | Not used (no evidence row) |
| pass1#24, pass2#14, pass2#19/20, pass3#02/03/17, pass3#10, pass3#21, pass4#08, pass4#11, pass4#13, pass4#17 | not verified | Belong to excluded sources (YouTube, marketing, off-topic, stubs). Not used. |
