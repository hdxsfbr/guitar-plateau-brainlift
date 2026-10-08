# Guitar Plateau BrainLift

BrainLift (Gauntlet education assignment) on an integrated, adaptive guitar and musicianship tutor for **intermediate guitarists of any age, self-taught or lesson-taught, stuck on a multi-year plateau and determined to keep improving**. Andre (an adult practising about 2 h/day) is the motivating real user, not the requirement. The scope was broadened on 2026-10-08; see `research/decisions.md`.

## Status

Draft submission in `deliverables/brainlift.md`. The research is in `research/`; the assignment and the original Elicit exports are in `sources/`. `CODEX_HANDOFF.md` and `sources/` are historical: their "adult, 2 h/day for 2 years" scope has been superseded.

## Key files

- `CODEX_HANDOFF.md`: scope decisions, assignment requirements, research questions, source leads, evidence rules
- `sources/assignment-brainlift-education.pdf`: authoritative assignment
- `sources/elicit-*`: raw Elicit exports (brief, citation audit, 31-record source CSV, UTF-8 with BOM); keep unmodified, put corrections in derived files

## Main documents

- `deliverables/brainlift.md`: the submission draft (purpose, experts, knowledge tree, POVs, pressure tests, next test, AI usage, requirement checklist)
- `research/povs.md`, `research/pressure-tests.md` (with raw outputs in `research/pressure-tests/`), `research/next-test.md`
- `research/evidence.csv` (one claim per row, with verified quotes), `research/source-register.csv`, `research/knowledge-tree.md`, `research/open-questions.md`
- `research/search-log.md`, `research/ai-usage-log.md`, `research/decisions.md`

## Original planned layout

```
sources/                       # supplied original exports (read-only)
research/search-log.md         # queries, dates, inclusion/exclusion, access failures
research/source-register.csv   # deduplicated bibliographic identities
research/evidence.csv          # one claim/finding per row, with provenance
research/knowledge-tree.md
research/pov-candidates.md
research/pressure-tests.md
research/open-questions.md
deliverables/brainlift.md      # submission draft
```

## Lab notes

- Host: `hdx-lab` at `~/code/guitar-plateau-brainlift`
- Remote: labs.gauntletai.com/andrebatista/guitar-plateau-brainlift (private)
- Owner: Andre (Gauntlet Cohort G7)
