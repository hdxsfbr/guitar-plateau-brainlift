# BrainLift: Breaking the intermediate guitar plateau

*Draft, 2026-10-08. Author: Andre Batista. Research support: AI tools, all logged in [`research/ai-usage-log.md`](../research/ai-usage-log.md).*

**How to read this.** Each factual claim carries an evidence ID (E###). The ID points to a row in [`research/evidence.csv`](../research/evidence.csv) holding a verbatim quote, its location and a verification status, and that row links to a source in [`research/source-register.csv`](../research/source-register.csv). Text marked *Inference* or *Bet* is my reasoning, not a finding.

---

## 1. Purpose

Intermediate guitarists can practise for years and stop improving, and the standard prescription is more scales, more theory and more hours. I want to improve their *retained, transferable* playing skill, not their in-session scores, by deciding how an adaptive practice tutor should order practice (should ear work gate drilling?) and deliver feedback (how often, and when?). Boundaries: intermediate guitarists of any age, self-taught or lesson-taught, practising alone with a phone for about 30 minutes to 2 hours a day, with no beginners, classrooms or special hardware.

**Learner group.** Intermediate guitarists stuck on a multi-year plateau who are determined to keep improving.

**Why me.** *[Andre to write, 2–3 sentences in his own voice. Suggested content: he is an adult guitarist practising about 2 h/day who has hit this plateau, and he is the motivating real user. He is not the requirement.]*

---

## 2. Experts and sources that disagree

| Who | Link | Why it matters here | Key finding | Limitation |
|---|---|---|---|---|
| **K. Anders Ericsson** (deliberate practice) | [Ericsson & Harwell 2019](https://doi.org/10.3389/fpsyg.2019.02396); [Ericsson 2021](https://doi.org/10.1007/s00426-020-01368-3) | The intellectual root of "practise more, practise deliberately" | Under strict criteria, practice explains 29% of variance (61% corrected) (E045). Deliberate practice *requires* individualized guidance from a qualified teacher; without it, it is only "purposeful" practice (E046) | An advocate reanalysing critics' data. Correlational |
| **Macnamara, Hambrick & Oswald** | [2014 meta-analysis](https://doi.org/10.1177/0956797614535810); [Hambrick et al. 2020](https://doi.org/10.3389/fpsyg.2020.01134) | Direct rebuttal of Ericsson | Deliberate practice explains about 21% of variance in music (E043), or 29.9% after correction (E044) | Depends on retrospective practice estimates |
| **Mosing, Ullén et al.** (twin studies) | [Mosing et al. 2014](https://doi.org/10.1177/0956797614541990); [Mosing et al. 2024](https://doi.org/10.3390/jintelligence12090087) | Tests whether practice *causes* ability | In identical twins, the twin who practised more did not have better music perception (E047). Heritability *rose* with practice (E048) | Perceptual tests, not guitar playing |
| **Gabriele Wulf** (motor learning applied to music) | [Wulf & Mornell 2008](https://musicperformanceresearch.org/wp-content/uploads/2020/11/Wulf-and-Mornell-Vol.-2-1-25.pdf) | The standard advice imported into music teaching | Give feedback "sparingly", use an external focus, let learners control practice (E030) | A narrative review that predates the replication meta-analyses. Wulf's own complex-skill study found 100% feedback beat none (E024) |
| **Brad McKay et al.** (replication meta-analyses) | [Feedback frequency 2022](https://doi.org/10.31234/osf.io/v2cp7); [Self-control 2022](https://open.lnu.se/index.php/metapsychology/article/view/2803) | Tests whether Wulf-style rules survive bias correction | No benefit from reducing feedback frequency at any time point (k = 75, E026). The self-control benefit drops from g = .44 to .107 after bias correction (E028) | Lab motor tasks; an underpowered literature |
| **Jazz pedagogy: theory-first vs practice-first** | [Bjerstedt 2016](https://www.cambridge.org/core/journals/british-journal-of-music-education/article/stealing-knowledge-in-a-landscape-of-learning-conceptualizations-of-jazz-education/77013C652DEC5588A5AB3AF990E0BAE8); [Brumbach 2022](https://doi.org/10.2979/jazzeducrese.1.1.05) | Is theory the right entry point? | Formal jazz education leans on theory and chord–scale methods (E093), and interviewed professionals say that's partly because they're easy to teach and measure (E094). A practice-based approach beat a theory-based one on improvisation gains (E064) | Bjerstedt is conceptual. Brumbach's improvisation comparison rests on 13 vs 21 high-school soloists over 4 weeks |
| **Thompson & Williamon; Bergee** (rater reliability) | [Thompson & Williamon 2003](https://researchonline.rcm.ac.uk/id/eprint/2170/); [Bergee 2003](https://doi.org/10.2307/3345847) | Can anyone, human or AI, grade playing reliably? | Experienced judges agree only moderately and show halo effects (E017, E018). Panels of 2–3 judges are unstable, and at least 5 are recommended (E016) | Conservatoire and university juries, not home recordings |

All sources were read in the original, as full text or abstract (`access` column in the register). AI-suggested citations were verified before use. The pressure-test models cited three studies, which were checked against their abstracts and added as E095–E097. Two model misstatements were caught and discarded ([pressure-tests.md](../research/pressure-tests.md)).

---

## 3. Knowledge tree

The full tree is in [`research/knowledge-tree.md`](../research/knowledge-tree.md), and the open questions in [`research/open-questions.md`](../research/open-questions.md).

**Evidence base, honestly:**
- 97 claims from 140 screened sources (46 excluded).
- Only **8 are direct**: guitar-specific, intermediate level or above, or guitar-specific feasibility.
- 55 are adjacent: music, but another instrument, level or population.
- 34 are extrapolated: lab motor tasks, STEM tutoring, non-musicians.
- **No study tests any teaching method on plateaued guitarists.**

### Problem and learners — what's going wrong, for whom, how do we know?
- **Practice matters, but it is not the whole story.** It correlates with achievement (r = .61 corrected, E042). It explains only 21–30% of variance in music (E043, E044). Twin data suggest that much of the practice–ability link is genetic (E047, E048).
- **We barely know what a plateau looks like.**
  - The only trajectory data show plateau phases in vocal-jazz students, with unclear methods (E049).
  - The adult-amateur literature says this is understudied (E050, wind players).
- **Lapsed musicians cite access, obligations and "difficulty with practicing"** (E038).
- **Playing hurts.** 51.8% of guitarists report playing-related problems (pooled, E051, preprint), and in one survey 53.3% reported an injury (E056).
- **Open:** On which dimensions are plateaued players actually stuck: ear, time, technique or practice design? Do self-taught and lesson-taught players plateau differently?

### Current practice — what's recommended, and what assumptions sit underneath?
- **Theory-first and chord–scale pedagogy dominate formal jazz teaching** (E093). Popular guitar advice says theory "accelerates the learning process" (register: `wpma`, flagged exclude, cited only as an example of the advice).
- **Feedback "sparingly", external focus, learner control** (E030).
- **The hidden assumption:** more correctly structured hours will push through the plateau. Ericsson's own definition makes the *teacher's individualized guidance* the active ingredient, not volume (E046).
- **Open:** What do guitar teachers actually diagnose, and do they agree? No study found.

### Learning and evidence — how is learning supposed to happen, and for whom does it hold?
- **Ear and hands co-develop.**
  - In non-musicians, learning to play a piece made listening to it engage motor areas (E095).
  - Play-plus-listen training enhanced auditory responses more than listening alone (E096).
- **Aural approaches beat notation- or theory-first ones in small studies:** aural vs notated exercises, n = 20 (E066); practice-based vs theory-based (E064). Aural imitation is a core correlate of improvisation skill (E067). None of these studied plateaued players or guitarists.
- **The feedback rules are weaker than advertised.**
  - Faded feedback helped in simple lab tasks (E023).
  - Across 75 experiments, reducing feedback did nothing measurable (E026).
  - Complex skills did better with 100% feedback than with none (E024, which used *concurrent* feedback).
  - Self-estimating before feedback turned 100% feedback from the worst condition into the best (E097, simple lab task).
- **Live visual feedback splits attention.** On violin, sound got worse while the feedback was on, and 55.2% said they "cannot play while watching" (E032, E033). Sound was *better* afterwards in the same session, so live feedback's harm is to attention, not shown harm to retention.
- **Video self-review changes how college guitarists evaluate themselves** (E068, direct).
- **Open:** Does interleaving help intermediates, or only novices (E012, E058)? Does any of this hold for teens?

### Alternatives — what else exists, and at what cost?
- **Intelligent tutors work about as well as human tutors (d = .76 vs .79, E001), but not better than them** (g = −.11, E004). Effects inflate on researcher-made tests (E002).
- **Mastery gating helps** (ES 0.52, E005), but self-paced mastery cut completion rates in college courses (E006).
- **Matching instruction to learning styles does nothing** (d = 0.04, E009).
- **Music-specific adaptive sequencing:** one study, n = 19, not significant (E007).
- *Inference:* the real comparator is a good fixed curriculum plus a weekly teacher, not "no instruction".
- **Open:** Does adaptivity add anything over that comparator?

### Feasibility — what breaks on cost, workload, access, motivation or scale?
- **Guitar transcription is good on benchmarks.** It is state of the art on GuitarSet (E081), the model is tiny (E082), and there is open-source code (E083). A student tab pipeline reached F1 .77, with pitch detection as the bottleneck (E084). Benchmarks are clean recordings; home phones are untested.
- **Motivation.** Dropout drivers are largely outside a tutor's control (E038). Gating can frustrate (E006).
- **Workload.** Reliable human grading needs 5 or more judges (E016). That is unaffordable per take, which is exactly why machine scoring is tempting.
- **Open:** Does transcription hold up on real practice audio? Will learners keep up recording and self-estimation for months?

### Measurement — how would we know, including retention and transfer, and what would change my mind?
- **Machines match experts on pitch and rhythm** (erhu r = .93 and .83, E086; piano technique dimensions .74–.91, E085). **They are weak at pinpointing which note went wrong** (F1 .705, E086).
- **Human graders are noisy** (E016–E021), and no rubric is stage-specific (E022).
- **Learner models need "deep" data.** Individual learning-rate estimates were reliable in only one of two datasets (E014, E015). Confirming mastery of even intervals took hundreds of items (E008).
- **Success measure:** no-feedback retention after a delay, plus transfer (new key, new tune, improvisation). Not in-session scores.
- **What would change my mind:** the kill criteria in §6.

---

## 4. Two spiky POVs

Full versions, with the v1 → v3 history, are in [`research/povs.md`](../research/povs.md).

### POV A — Hear it before you drill it

**Claim.** For a plateaued intermediate guitarist, no scale, lick or chord sound gets high-volume drilling until they can hear it and play (or hum) it back by ear. Scales and theory stay; the ear decides when they get drilled.

**Bet.** The plateau is more often a hearing problem than a technique or theory problem. The tutor *tests* this for each learner with a week-1 screen: ear, rhythm, fretboard mapping and technique. It doesn't assume it.

**Consensus.** Theory first, scales first, more technique hours. Chord–scale methods dominate jazz teaching partly because they're "easy to verbalize" and "measurable" (E093, E094). The popular reading of deliberate practice is volume (E042), even though Ericsson's own definition centres on guidance (E046).

**Counterpoint.** Naming a sound is not hearing it. The best evidence we have favours ear- and practice-based entry over theory- and notation-first entry (E064, E066), and aural imitation is a core correlate of improvisation (E067). Ear and hands build each other (E095, E096), so the ear should *gate volume*, not *forbid contact*.

**Evidence limits.**
- **Zero direct studies.** It is all small, short, school or college jazz work, plus neural data from non-musicians.
- The one randomized test of Gordon's audiation-based learning sequence that we found showed only an interaction effect (E074).
- No source measures how common hearing bottlenecks are.

**Practical implication.**
- **Tutor:**
  - Screen first.
  - Gate tempo ladders and repetition behind a by-ear check passed on two separate days.
  - Keep slow mapping work, slow improvisation and pure motor drills (picking, legato) ungated.
- **Learner, tomorrow:** take the lick you've drilled most. Have someone play a 4-note fragment of it over a drone, then play it back without looking. If you can't, stop speeding it up and spend the time on call-and-response.

### POV B — Feedback after every take, never during

**Claim.** Every full take gets feedback, right after the learner calls their own mistakes. "Withhold feedback so they don't depend on it" hasn't held up, and live on-screen feedback is out.

**Consensus.** Give feedback sparingly, fade it, let learners choose when to get it (E023, E027, E030).

**Counterpoint.**
- Reducing feedback showed no benefit across 75 experiments (E026).
- Complex skills did better with frequent feedback than with none (E024, E025).
- "Learner control" barely survives bias correction (E028).
- The dependency risk is real, but it has a cheap fix: make the learner estimate their own errors first. In Guadagnoli & Kohl, 100% feedback with self-estimation retained best, and 100% without it retained worst (E097).
- Live display costs attention (E033).

**Evidence limits.**
- **This is "withholding doesn't help", not "more is better".** Nearly all the evidence is lab motor tasks.
- The only direct row is video self-review in college guitarists (E068). The adult-beginner guitar thesis is adjacent (E069).
- Feedback quality caps everything. Machines are reliable for pitch and timing (E086) and weak at locating errors (E086), and human raters are noisy (E016–E018).

**Practical implication.**
- **Tutor:** record every take. After each take:
  1. The learner marks their slips.
  2. The tutor reveals its analysis, on reliable dimensions only.
  3. The tutor gives one priority. That can be a self-review or teacher-check item, not only a machine metric.
- Also: show "couldn't assess" instead of a false all-clear. Keep the metronome; ban on-screen scoring while playing.
- **Learner, tomorrow:** record every take on your phone. Write down where you think you slipped *before* you listen back, then check yourself and pick one fix.

---

## 5. AI pressure test

**Prompt (verbatim):**

> "Evaluate this education POV: [insert POV]. Where is it weak or unlikely to work? Identify the strongest objection, the specific constraint behind it, and the evidence needed to resolve it. Give an honest assessment; do not agree or disagree just because I asked."

**Models.** `anthropic/claude-opus-5.5` ran both POVs in two rounds; `openai/gpt-5.5` ran round 1 as a contrast. Six runs on 2026-10-08 cost about $0.53 via OpenRouter. Raw outputs are verbatim in [`research/pressure-tests/`](../research/pressure-tests/), and the analysis is in [`research/pressure-tests.md`](../research/pressure-tests.md). The runs used the earlier "adult, 2 h/day" framing, and the objections don't depend on it.

| | Strongest objection | Constraint behind it | Evidence needed | What I changed |
|---|---|---|---|---|
| **A, round 1** (both models) | Hearing and playing co-develop. A strict gate blocks the playing that builds hearing | Auditory–motor coupling (E095, E096); slow harmonic hearing → stalls and dropout | Base rates of ear, time and technique deficits; ear-gated vs ear-coupled vs conventional trial; gate pass-time telemetry | The gate covers only *volume*, not first contact. "Usually" became a tested bet. Singing is optional |
| **A, round 2** | Guitar playback conflates *hearing* with *fretboard mapping*, and mapping is built by the drilling the gate withholds | The gate's measure can't separate the two deficits | Dissociation test (discrimination vs hum-back vs guitar); matched-time trial | Added a non-guitar screen; mapping work is ungated; pass on 2 separate days |
| **B, round 1** | Per-take machine feedback outsources self-evaluation (Claude); too much to act on (GPT) | Transfer must be shown without the tutor, and attention is limited | Retention and transfer RCT with a self-estimation arm, plus analyser error rates on home audio | "Withholding doesn't help", not "more is better". Self-estimate first (E097). One priority per take |
| **B, round 2** | **Streetlight:** if only measurable things can be the priority, every take steers toward timing and pitch | Measurable ≠ limiting (tension, time feel, tone) | Do teachers' top limiting factors fall within machine-measurable dimensions? Do metric gains track blind expert ratings? | The priority slot can be self-review or teacher-check. "Couldn't assess" is shown. Take = full run-through |

**What I didn't change.** Neither model argued for theory-first or for withholding feedback. Both said the direction holds and the *mechanism* carries the burden of proof. The next test targets the mechanism.

---

## 6. Next test: an 8-week pilot

Full design: [`research/next-test.md`](../research/next-test.md).

- **Who.** 12–16 plateaued intermediate guitarists, aged **18 or over**. Teens belong to the target group, but they need parental consent, which is too heavy for a pilot. Eligibility: self-reported plateau of 2 years or more, and at least 30–45 min/day for 8 weeks.
- **Design.** Each learner's 8 practice items are randomized two ways: ear-gated vs conventional drilling, and feedback after every take with self-estimate first vs faded feedback. Each learner is their own control.
- **Measures.**
  - Weeks 7–8, with no feedback: retention, new-key transfer and blind-rated improvisation.
  - Gate pass times, self-estimate accuracy, adherence.
  - **Reliability before outcomes:** 3 blind teacher-raters (rating dimensions with ICC below .60 are dropped); machine–panel agreement on home recordings; and how far teachers agree on each learner's main limit, which also tests the streetlight objection.
- **Kill criteria.**
  - **A dies** if gated items aren't better on transfer and are worse at tempo.
  - **A's bet dies** if fewer than a third of learners screen as ear-limited.
  - **B dies** if every-take items are worse at no-feedback retention by 0.3 SD or more, or if self-estimate accuracy doesn't improve.
  - **Machine scoring is switched off** for any dimension with r < .70 against the panel.

**Candour about numbers.** I chose the gate threshold (4 of 5, on 2 days), the screen, and every cut-off in the pilot (0.3 SD, r ≥ .70, ICC ≥ .60, the one-third base rate) as reasonable starting values. **None comes from the evidence.** n = 12 gives go/stop signals, not proof, and carry-over between items biases both POVs toward a null result.

---

## 7. AI usage

AI was used for:
- source discovery: Elicit, and a deep-research tool with `gpt-5-mini`;
- brainstorming: ChatGPT;
- evidence extraction, quote verification and drafting: Grok Bot;
- pressure tests: Claude Opus 5.5 and GPT-5.5.

Every quote in the evidence table was machine-checked against the saved source text: 95 exact matches, 2 near (line-break artefacts), 0 failures. AI-written summaries are never cited as evidence, and one invented quote clause from the deep-research tool was caught and replaced. Each tool, prompt, model, output and cost is logged in [`research/ai-usage-log.md`](../research/ai-usage-log.md). Searches are logged in [`research/search-log.md`](../research/search-log.md).

---

## Requirement checklist

| Requirement (assignment PDF + portal PRD) | Where | Status |
|---|---|---|
| Purpose in 2–3 sentences: problem, who, outcome, decision, boundaries | §1 (3 sentences) | Done. The personal "Why me" is left for Andre |
| Specific learner group and setting | §1 | Done |
| ≥3 credible experts/sources with different perspectives, each with link, relevance, key finding, limitation | §2 (7 entries) | Done |
| Read originals; verify AI-suggested citations | §2 note; `evidence.csv` `quote_verified`; `pressure-tests.md` | Done. Some sources were read at abstract level only, as flagged in the register |
| Knowledge tree: 6 branches, each with findings, source links and open questions | §3; full tree in `research/knowledge-tree.md` | Done. Findings link through E-IDs; key sources are linked in §2 |
| Measurement includes retention/transfer and "what would change my mind" | §3 Measurement; §6 | Done |
| Two spiky POVs, each with consensus, counterpoint, evidence + limits, practical implication | §4 | Done |
| Pressure test with the exact prompt; strongest objection; constraint; evidence needed | §5; raw outputs | Done |
| Defend, narrow or revise; propose one small test | §5 "What I changed"; §6 | Done |
| Clear about what could prove it wrong | §6 kill criteria | Done |
| AI usage documentation (required) | §7; `ai-usage-log.md` | Done |
| Traceable to evidence | E-IDs throughout | Done. Direct evidence is thin (8 of 97 rows), and the document says so |
