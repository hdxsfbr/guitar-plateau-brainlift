# Knowledge tree — adaptive musicianship tutor for plateaued intermediate guitarists

Built 2026-10-07 (CT) from `research/evidence.csv` (97 claim rows, E001–E097; E093–E097 and corrections to E024/E064 added 2026-10-08) and `research/source-register.csv` (140 sources). Every finding cites evidence IDs; the quote, location and verification status for each ID are in `evidence.csv`.

**How to read this**
- **Finding** = empirical result reported by a source. **Theory** = a framework or mechanism claim. **Expert advice** = a recommendation. **Inference** = my reasoning from the findings (marked *Inference*). **Product hypothesis** = a testable bet for the tutor (marked *Product hypothesis*). Product hypotheses are not evidence.
- Relevance tags come from `relevance_to_learner_group`: **direct** = guitar-specific evidence at intermediate level or above (any age), or guitar-specific feasibility/health evidence; **adjacent** = music but a different population, instrument or level; **extrapolated** = non-music tasks, beginners in lab tasks, children, or very short interventions.
- **Scope (updated 2026-10-08).** The learner group is intermediate guitarists of any age, self-taught or lesson-taught, who are stuck on a multi-year plateau and determined to keep improving. Andre (an adult practising about 2 h/day) is the motivating real user, not the requirement. Rows that were *direct* only because they studied adults were re-tagged *adjacent*: E039, E040, E050, E069.
- **Bottom line on directness.** Only 8 of 97 rows are direct, and none of those tests a teaching method on plateaued players. No controlled study tests adaptive versus fixed instruction for intermediate guitarists over months. Most of the decision rests on adjacent and extrapolated evidence.

---

## 1. Problem — what a plateau is and why intermediates stall

**Findings**
- **Practice matters, but by itself it explains a minority of variance in music skill.** Estimates range from 21% (`E043`, Macnamara 2014) to 29.9% of reliable variance after correction (`E044`, Hambrick 2020). A corrected correlation of r = .61 in music samples (`E042`, Platz 2014) is the high end. The theory's originator argues for 29% raw and 61% corrected under stricter criteria (`E045`); this is contested.
- **Twin studies challenge a simple "more hours → more skill" model.** Within identical-twin pairs, the twin who practised more did not have better music *perception* ability (`E047`). Heritability of auditory discrimination rose with practice hours (`E048`). Both are *extrapolated*: the outcomes are perceptual tests, not guitar performance.
- **Direct plateau-trajectory data are close to absent.** The one source found describes logarithmic progress with plateau phases in vocal jazz students (`E049`), and its method is unclear (caution). For adult amateurs specifically, the literature itself says this is under-studied (`E050`).
- **Dropout and stall drivers (lapsed adult musicians) are mostly external or experiential.** Lapsed musicians name access and opportunity, activity experience, obligations and "difficulty with practicing" (`E038`, *adjacent*). In youth music schools, autonomous motivation predicts staying and controlled motivation predicts dropping out (`E041`, *extrapolated*).
- **Physical risk is real for guitarists who practise a lot.**
  - In a preprint meta-analysis, pooled prevalence of any playing-related problem was 51.8%, and of clinically diagnosed disorders 42.2% (`E051`, *direct*, cross-sectional).
  - A Portuguese survey found a lifetime injury rate of 53.3% (`E056`).
  - Causal evidence on risk factors is weak (`E052`), and nobody has tested playing position for classical guitar (`E054`).

**Where results differ by population/task**
- Variance explained by practice is higher in music than in education or professions (`E043`). It depends on how practice is measured (retrospective hours vs "deliberate" practice) and on the reliability correction used (`E044` vs `E045`).
- Genetic studies use perceptual outcomes, while deliberate-practice studies use performance outcomes, so they do not directly contradict each other.

**Open questions:** see `open-questions.md` Q1–Q4.

---

## 2. Current practice — how intermediate players and teachers actually work

**Findings**
- **Definition matters.** By Ericsson's criteria, practice without "individualized guidance by a qualified teacher" is *purposeful*, not *deliberate*, practice (`E046`, theory). Whether software can meet the fifth criterion is untested (*Inference*).
- **Conventional pedagogy advice from motor learning** is to give feedback sparingly, vary task order, use an external focus and let learners control practice (`E030`, expert advice, Wulf & Mornell 2008). Section 3 shows that several of these rules have since weakened.
- **Expert jazz guitarists** describe their skill in terms of chunks, schemas and templates that depend on context (`E071`, qualitative). Elite vs semi-elite improvisers differed in the *quality* of individual practice and in jam/network activity (`E070`, retrospective).
- **Learners want adjustable directiveness (adult evidence).** Adult instrumentalists welcomed more teacher direction when stuck technically or in an unfamiliar style, and advanced adults self-directed more (`E040`, *adjacent*, n=6).
- **The theory-first default.** A jazz-education scholar describes formal jazz education's main tendency as theory-based, chord–scale pedagogy. Interviewed professionals attribute this partly to it being easy to teach and measure (`E093`, `E094`; expert opinion, added 2026-10-08).
- **Pedagogy content debates** (tonic-based solmization `E072`; Kodály modality order `E073`; chord-scale vs transcription `E076`) are argued from theory or teacher perception, not outcome data.
- **Research landscape.** Music-practice research is mostly quantitative and centred on deliberate practice, strategies and SRL (`E078`). It is overwhelmingly about students rather than plateaued amateurs.

---

## 3. Learning evidence — what changes learning (schedules, feedback, self-regulation)

### 3a. Practice schedules (interleaving / variability)
- **Non-music evidence is strong.** Interleaving helped implicit motor-sequence learning (`E061`) and physics problem solving (median +50% / +125% on surprise tests, `E062`). The mechanism is discriminative contrast, which differs from spacing (`E063`, theory). All *extrapolated*.
- **Music evidence is mixed and small-n.**
  - Interleaving helped in some studies: advanced clarinetists, when raters differed (`E057`, n=10); interval novices without aids (`E012`, n=44); and variable leap practice in pianists (`E059`).
  - It made no difference in others: proficient pianists (`E058`, n=21), university musicians on a sticking task at retention (`E060`, n=120), and interval learners who had reference songs and singing (Exp 1 of `E012`).
- **Playing builds hearing (neural evidence, extrapolated).** In non-musicians, learning to play a piece made listening to it engage motor areas (`E095`). Two weeks of play-plus-listen training enhanced auditory-cortex responses more than listening alone (`E096`). Hearing and playing co-develop. Added 2026-10-08.
- **Learners misjudge schedules.** 75% judged blocking as good as or better than interleaving, even though 73% did as well or better with interleaving (`E013`).
- **Where results differ.** Benefits appear for discrimination-heavy tasks (intervals, similar categories) and novices, and wash out for proficient players or when other supports exist. Plateaued intermediates sit between these groups, so this is unresolved.

### 3b. Feedback amount, timing and control
- **The classic guidance hypothesis.** Faded or reduced knowledge-of-results improved delayed retention in a simple lab task (`E023`, Winstein & Schmidt 1990).
- **Counter-evidence 1: complexity.** For a complex ski-simulator skill, 100% concurrent feedback beat no feedback at retention, with 50% intermediate, so reduced feedback showed no advantage (`E024`; corrected 2026-10-08 from "beat 50%"). Principles from simple tasks do not generalise to complex skills (`E025`), and the augmented-feedback literature is dominated by simple or artificial tasks (`E029`).
- **Moderator: self-estimation.** With 100% feedback, learners who estimated their own error first retained best, and those who did not retained worst (`E097`, simple lab task). Added 2026-10-08.
- **Counter-evidence 2: replication.**
  - A meta-analysis of reduced-feedback-frequency studies (k = 75, N = 2,228) found no significant effect at any time point and no performance–learning reversal; the literature is severely underpowered (`E026`).
  - Self-controlled practice: a naive g = .44 drops to g = .107 after bias correction, which is "not currently distinguishable from zero" (`E028`). The early positive study is `E027`.
- **Music-specific.**
  - Real-time visual feedback for violin novices improved bowing kinematics but hurt sound quality while it was active. Sound quality was better once feedback was removed, within the same session (`E032`).
  - 55.2% said they "cannot play while watching the feedback" (`E033`).
  - External vs internal focus showed no consistent advantage across 15 music experiments (`E031`), which contradicts the sports-derived rule in `E030`.
- **Video self-observation (closest to the target learner).** College-level classical guitarists using video changed how they self-evaluated, more so the higher performers (`E068`, *direct*). Adult beginner classical guitarists using weekly video outperformed controls (p = .037; `E069`, thesis).

### 3c. Self-regulated learning
- Self-regulation correlates only weakly with music outcomes, and explicit SRL *instruction* is the strongest correlate (`E035`).
- Intervention reviews are mixed but mostly positive or null (`E036`). One reports a medium pooled effect, but only 7 studies were meta-analysed and the evidence is weaker outside secondary and university settings (`E037`).
- For adult beginners, an SRL worksheet changed behaviour but not self-efficacy (`E039`, *adjacent*, pilot).

---

## 4. Alternatives — adaptive vs fixed instruction, and other designs

**Findings**
- **ITS work in well-defined domains.**
  - Step-based ITS give d ≈ 0.76 vs no tutoring, close to human tutoring at d ≈ 0.79 (`E001`).
  - The median effect is 0.66 SD, but it is much larger on locally developed tests than on standardized tests (`E002`).
  - ITS beat large-group teaching, other computer-based instruction and textbooks (`E003`), but **not** individual human tutoring (g = −.11) or small groups (g = .05) (`E004`).
  - All *extrapolated* (STEM, school/college).
- **Mastery gating helps.** Average effect size 0.52, larger for weaker students (`E005`). The cost: self-paced mastery reduced college completion rates (`E006`).
- **Matching to learner "type" does not work.** Matching instruction to learning styles has d = 0.04 across 143 studies (`E009`). There is no crossover-interaction evidence (`E010`), and robust aptitude-treatment interactions are scarce (`E011`). This counts against adapting to *traits*. It does not count against adapting to *skill state*.
- **Music-specific adaptive sequencing is barely tested.**
  - The only controlled comparison found: an adaptive interval tutor vs a fixed sequence (n = 19, novices). Differences favoured adaptive but were not significant (`E007`).
  - It needed several hundred mastered items to confirm mastery (`E008`).
  - An "adaptive" music-instruction system reported only self-defined metrics (`E092`).
  - Augmented-piano prototypes have not shown learning benefits (`E034`).
- **Content and approach alternatives.** A practice-based approach beat a theory-based one (`E064`; improvisation outcome from 13 vs 21 soloists), and aural exercises beat notated ones (`E066`), in short or small studies of school or student improvisers. Task *order* made no difference over 12 weeks (`E065`). Weaker or qualitative evidence:
  - A randomized test of Gordon learning-sequence instruction found only an interaction effect (`E074`).
  - A-cappella ear training was evaluated by its own author (`E075`).
  - In 9 children, improvisation and repertoire produced equal transfer of a technique (`E080`).

**Where results differ**
- ITS effects shrink with standardized outcomes, strong comparators (a human tutor), nonconventional controls and flawed implementations (`E002`, `E004`).
- Guitar musicianship is ill-defined: many correct answers, and expressive quality matters. So VanLehn and Ma-type effects are an upper bound.

*Inference:* the strongest supported adaptive mechanisms are (a) mastery gating on reliably measurable sub-skills and (b) step-level feedback on checkable steps (pitch, rhythm, chord changes). The evidence does not support fine-grained adaptive *sequencing* or adaptation to learner type.

---

## 5. Feasibility — can a tutor do this for a determined intermediate over months to years?

**Findings**
- **Transcription technology is good for guitar.**
  - An instrument-agnostic model is state-of-the-art on GuitarSet (`E081`) and tiny (16,782 parameters, `E082`); there is an open-source library (`E083`).
  - A narrative review claims near-human MIR accuracy on recognition tasks (`E090`, caution).
  - A student pipeline reached tab F1 0.77, with pitch detection as the bottleneck (`E084`, not peer reviewed).
  - Benchmark recordings are clean; real home audio is untested here.
- **Feedback UI cost.** Concurrent visual feedback overloads novices (`E033`).
- **Adherence and health.**
  - Self-paced mastery can reduce completion (`E006`).
  - Breaks are recommended (5 min per 25 min, `E053`, expert advice), and strength-training prevention shows benefit in professionals (`E055`).
  - Dropout reasons among lapsed adult musicians are largely outside a tutor's control (`E038`).
- **Psychological effects of AI tools.** Assessment-type AI strengthens ability beliefs, and adaptive AI supports engagement (`E088`). The research base is young and university-centred (`E089`). Haptic or virtual guitars improve realism only (`E091`). Early computer courseware drew positive attitudes (`E079`).

---

## 6. Measurement — can bottlenecks and progress be diagnosed reliably?

**Findings**
- **Human raters are a noisy gold standard.**
  - Full faculty panels are reliable, but panels of 2–3 judges vary; at least five adjudicators are recommended (`E016`).
  - Agreement between three experienced evaluators was only moderate, with instrument-related bias (`E017`).
  - Sub-scores were so inter-correlated that categories barely discriminated, a halo effect (`E018`).
  - Raters differ in severity and in how they use the scale (`E019`), severity drifts across ensemble levels (`E020`), and raters attend to different dimensions (`E021`).
  - No published solo rubric differentiates criteria by learning stage (`E022`). Rubric dimensions exist for jazz improvisation but are unvalidated in the captured text (`E077`). Aural imitation and technique are core correlates (`E067`).
- **Machine scoring.**
  - Agreement with experts is high on pitch and rhythm: erhu r = .93/.83 (`E086`); piano technique r = .74–.91 by dimension (`E085`).
  - *Locating* specific problems is weaker: problem-note F1 = .705 (`E086`).
  - Automated creativity scoring reaches r = .48–.68 (`E087`, children, programming).
- **Learner-model reliability.** Ability estimates are reliable. Individual *learning-rate* estimates were reliable in only one of two datasets (`E014`). Reliable per-learner estimates need "deep" data, meaning many observations per skill (`E015`). Even a narrow interval tutor needed hundreds of items (`E008`).

**Where results differ:** reliability is good for low-level, objectively checkable dimensions (pitch, timing) and for panel averages. It is poor for single raters, for expressive or global dimensions, and for diagnosing *which* sub-skill is the bottleneck.

*Inference:* a tutor should score and adapt only on dimensions with demonstrated reliability against a multi-rater panel. It should treat "bottleneck diagnosis" as a hypothesis to test with targeted probes, not as a measured fact.

---

## Evidence index (ID → source → link)

| ID | Branch | Relevance | Type | Source | Quote verified |
|---|---|---|---|---|---|
| E001 | alternatives | extrapolated | empirical finding | [vanlehn2011](https://public.asu.edu/~kvanlehn/Stringent/PDF/EffectivenessOfTutoring_Vanlehn.pdf) | yes |
| E002 | alternatives | extrapolated | empirical finding | [kulikfletcher2016](https://eric.ed.gov/?id=EJ1090502) | yes |
| E003 | alternatives | extrapolated | empirical finding | [ma2014](https://cs.uky.edu/~sgware/reading/papers/ma2014intelligent.pdf) | yes |
| E004 | alternatives | extrapolated | empirical finding | [ma2014](https://cs.uky.edu/~sgware/reading/papers/ma2014intelligent.pdf) | yes |
| E005 | alternatives | extrapolated | empirical finding | [kulik1990](https://www.uky.edu/~gmswan3/575/kulik_kulik_Bangert-Drowns_1990.pdf) | yes |
| E006 | feasibility | extrapolated | empirical finding | [kulik1990](https://www.uky.edu/~gmswan3/575/kulik_kulik_Bangert-Drowns_1990.pdf) | yes |
| E007 | alternatives | adjacent | empirical finding | [elsadat2026](https://www.scitepress.org/Papers/2026/147268/147268.pdf) | yes |
| E008 | measurement | adjacent | inference | [elsadat2026](https://www.scitepress.org/Papers/2026/147268/147268.pdf) | yes |
| E009 | alternatives | extrapolated | empirical finding | [hattie2025](https://link.springer.com/article/10.1007/s10648-025-10002-w) | yes |
| E010 | alternatives | extrapolated | theory | [pashler2008](https://doi.org/10.1111/j.1539-6053.2009.01038.x) | yes |
| E011 | alternatives | extrapolated | theory | cronbach1977 | yes |
| E012 | learning-evidence | adjacent | empirical finding | [wong2021](https://www.sarahshihuiwong.com/_files/ugd/8b1a2f_8fe3ea44a34543d3b8f0568078ae4339.pdf) | yes |
| E013 | learning-evidence | adjacent | empirical finding | [wong2021](https://www.sarahshihuiwong.com/_files/ugd/8b1a2f_8fe3ea44a34543d3b8f0568078ae4339.pdf) | yes |
| E014 | measurement | extrapolated | empirical finding | [liu2017](http://educationaldatamining.org/EDM2017/proc_files/papers/paper_137.pdf) | yes |
| E015 | measurement | extrapolated | inference | [liu2017](http://educationaldatamining.org/EDM2017/proc_files/papers/paper_137.pdf) | yes |
| E016 | measurement | adjacent | empirical finding | [bergee2003](https://doi.org/10.2307/3345847) | yes |
| E017 | measurement | adjacent | empirical finding | [thompson2003](https://researchonline.rcm.ac.uk/id/eprint/2170/) | yes |
| E018 | measurement | adjacent | empirical finding | [thompson2003](https://researchonline.rcm.ac.uk/id/eprint/2170/) | yes |
| E019 | measurement | adjacent | empirical finding | [wesolowski2016](https://doi.org/10.1525/mp.2016.33.5.662) | yes |
| E020 | measurement | adjacent | empirical finding | [wesolowski2015](https://doi.org/10.1177/1029864915589014) | yes |
| E021 | measurement | adjacent | empirical finding | [wesolowski2016cog](https://doi.org/10.1177/0305735616665004) | yes |
| E022 | measurement | adjacent | empirical finding | [moura2024](https://europepmc.org/articles/PMC11496144) | yes |
| E023 | learning-evidence | extrapolated | empirical finding | [winstein1990](https://www.bisp-surf.de/Record/PU199111046086) | yes |
| E024 | learning-evidence | extrapolated | empirical finding | [wulf1998](https://europepmc.org/article/MED/20037033) | yes |
| E025 | learning-evidence | extrapolated | theory | [wulfshea2002](https://europepmc.org/article/MED/12120783) | yes |
| E026 | learning-evidence | extrapolated | empirical finding | [mckay2022ff](https://doi.org/10.31234/osf.io/v2cp7) | yes |
| E027 | learning-evidence | extrapolated | empirical finding | [chiviacowsky2002](https://europepmc.org/article/MED/12495242) | yes |
| E028 | learning-evidence | extrapolated | empirical finding | [mckay2022sc](https://open.lnu.se/index.php/metapsychology/article/view/2803) | yes |
| E029 | learning-evidence | extrapolated | theory | [sigrist2013](https://europepmc.org/article/MED/23132605) | yes |
| E030 | current-practice | adjacent | expert advice | [wulfmornell2008](https://musicperformanceresearch.org/wp-content/uploads/2020/11/Wulf-and-Mornell-Vol.-2-1-25.pdf) | yes |
| E031 | learning-evidence | adjacent | empirical finding | [hohagen2024](https://europepmc.org/articles/PMC11033434) | yes |
| E032 | learning-evidence | adjacent | empirical finding | [blanco2021](https://doi.org/10.3389/fpsyg.2021.648479) | yes |
| E033 | feasibility | adjacent | empirical finding | [blanco2021](https://doi.org/10.3389/fpsyg.2021.648479) | yes |
| E034 | alternatives | adjacent | empirical finding | [deja2022](https://arxiv.org/pdf/2208.09929) | yes |
| E035 | learning-evidence | adjacent | empirical finding | [varela2016](https://doi.org/10.1177/0305735614554639) | yes |
| E036 | learning-evidence | adjacent | empirical finding | [lubert2024](https://doi.org/10.1177/10298649241290448) | yes |
| E037 | learning-evidence | adjacent | empirical finding | [wang2025](https://www.mdpi.com/2079-3200/13/12/162) | yes |
| E038 | problem | adjacent | empirical finding | [krause2019](https://researchonline.jcu.edu.au/62727/15/JCU_Krause%2CKirby%2CDieckmann%26Davidson2019_reengage_PrePrint.pdf) | yes |
| E039 | feasibility | adjacent | empirical finding | [ritchie2018](http://redfame.com/journal/index.php/jets/article/view/2978) | yes |
| E040 | current-practice | adjacent | empirical finding | [leahy2021](https://doi.org/10.1177/0255761421991596) | yes |
| E041 | problem | extrapolated | empirical finding | [wieser2024](https://doi.org/10.3389/fpsyg.2024.1378843) | yes |
| E042 | problem | adjacent | empirical finding | [platz2014](https://doi.org/10.3389/fpsyg.2014.00646) | yes |
| E043 | problem | adjacent | empirical finding | [macnamara2014](https://doi.org/10.1177/0956797614535810) | yes |
| E044 | problem | adjacent | empirical finding | [hambrick2020](https://doi.org/10.3389/fpsyg.2020.01134) | yes |
| E045 | problem | adjacent | empirical finding | [ericsson2019](https://doi.org/10.3389/fpsyg.2019.02396) | yes |
| E046 | current-practice | adjacent | theory | [ericsson2021](https://doi.org/10.1007/s00426-020-01368-3) | near |
| E047 | problem | extrapolated | empirical finding | [mosing2014](https://doi.org/10.1177/0956797614541990) | yes |
| E048 | problem | extrapolated | empirical finding | [mosing2024](https://doi.org/10.3390/jintelligence12090087) | yes |
| E049 | problem | adjacent | empirical finding | [musicahodie_jazz](https://doi.org/10.5216/mh.v25.82965) | yes |
| E050 | problem | adjacent | theory | [hartz2016](https://www.semanticscholar.org/paper/e2edb968e003cdc2ae89fd1199fb572c) | yes |
| E051 | problem | direct | empirical finding | [castillo2025](https://www.medrxiv.org/content/10.1101/2025.10.08.25337619) | near |
| E052 | problem | adjacent | empirical finding | [rotter2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7007903/) | yes |
| E053 | feasibility | adjacent | expert advice | [chan2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4086404/) | yes |
| E054 | problem | direct | empirical finding | [lund_guitar](http://lup.lub.lu.se/luur/download?fileOId=1530022&func=downloadFile&recordOId=1530017) | yes |
| E055 | feasibility | adjacent | empirical finding | [laseur2023](https://doi.org/10.21091/mppa.2023.3022) | yes |
| E056 | problem | direct | empirical finding | [dossantos2024](https://doi.org/10.3233/WOR-230701) | yes |
| E057 | learning-evidence | adjacent | empirical finding | [carter2016](https://doi.org/10.3389/fpsyg.2016.01251) | yes |
| E058 | learning-evidence | adjacent | empirical finding | [uwo_pianists](https://uwo.scholaris.ca/items/6fdcc793-acc2-455d-939f-b2a216d22c3e) | yes |
| E059 | learning-evidence | adjacent | empirical finding | [bangert2013](https://www.semanticscholar.org/paper/22b218bfef560249169fd6cad1ae378e) | yes |
| E060 | learning-evidence | adjacent | empirical finding | [rose2006](https://repository.lsu.edu/gradschool_dissertations/1643) | yes |
| E061 | learning-evidence | extrapolated | empirical finding | [schorn2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8476370/) | yes |
| E062 | learning-evidence | extrapolated | empirical finding | [rohrer2021](https://www.nature.com/articles/s41539-021-00110-x) | yes |
| E063 | learning-evidence | extrapolated | theory | [chen2021](https://doi.org/10.1007/s10648-021-09613-w) | yes |
| E064 | alternatives | adjacent | empirical finding | [brumbach2022](https://doi.org/10.2979/jazzeducrese.1.1.05) | yes |
| E065 | alternatives | extrapolated | empirical finding | [marino2023](https://doi.org/10.1177/00224294221150019) | yes |
| E066 | alternatives | adjacent | empirical finding | [laughlin2001](https://digital.library.unt.edu/ark:/67531/metadc2886/) | yes |
| E067 | measurement | adjacent | empirical finding | [palmer2016](https://doi.org/10.1177/0022429416664897) | yes |
| E068 | learning-evidence | direct | empirical finding | [boucher2019](https://doi.org/10.1177/0305735619842374) | yes |
| E069 | learning-evidence | adjacent | empirical finding | [uwo_video_guitar](https://ir.lib.uwo.ca/etd/4733) | yes |
| E070 | current-practice | adjacent | empirical finding | [wopereis2015](https://www.semanticscholar.org/paper/f687718b5d8e797df29ec56de9c34ca1) | yes |
| E071 | current-practice | adjacent | theory | [solstad2020](https://doi.org/10.4324/9780429022692) | yes |
| E072 | current-practice | adjacent | theory | [karpinski2021](https://mtosmt.org/issues/mto.21.27.2/mto.21.27.2.karpinski.html) | yes |
| E073 | current-practice | extrapolated | expert advice | [stthomas_kodaly](https://researchonline.stthomas.edu/view/pdfCoverPage?instCode=01CLIC_STTHOMAS&filePid=13439812430003691&download=true) | yes |
| E074 | alternatives | extrapolated | empirical finding | [shareok_gordon](https://shareok.org/server/api/core/bitstreams/2ccb5baf-26a6-4fb8-883c-ab3f147d5bdb/content) | yes |
| E075 | alternatives | adjacent | empirical finding | [russell2017](https://www.semanticscholar.org/paper/e57d6153b94376e49cb931580a21f395) | yes |
| E076 | current-practice | adjacent | empirical finding | [hu2026](https://doi.org/10.2979/jerp.00015) | yes |
| E077 | measurement | adjacent | empirical finding | [moore2016](https://www.semanticscholar.org/paper/17ac4b6c657d441eadde6226f1c7574e) | yes |
| E078 | current-practice | adjacent | empirical finding | [how2021](https://doi.org/10.1177/10298649211005531) | yes |
| E079 | feasibility | adjacent | empirical finding | [zorn1995](https://www.semanticscholar.org/paper/a21114ee38a25441b01ee18848dfbbe7) | yes |
| E080 | alternatives | extrapolated | empirical finding | [minnich2014](https://www.semanticscholar.org/paper/bf370abae153159ac76b3aef44ae3d7f) | yes |
| E081 | feasibility | direct | empirical finding | [bittner2022](https://arxiv.org/abs/2203.09893) | yes |
| E082 | feasibility | direct | empirical finding | [bittner2022](https://arxiv.org/abs/2203.09893) | yes |
| E083 | feasibility | direct | expert advice | [basicpitch](https://github.com/spotify/basic-pitch) | yes |
| E084 | feasibility | direct | empirical finding | [fretwork2026](https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists) | yes |
| E085 | measurement | adjacent | empirical finding | [pianoeval2026](https://www.nature.com/articles/s41598-026-72157-y) | yes |
| E086 | measurement | adjacent | empirical finding | [erhu2026](https://www.researchsquare.com/article/rs-10127105/latest.pdf) | yes |
| E087 | measurement | extrapolated | empirical finding | [ej1483320](https://files.eric.ed.gov/fulltext/EJ1483320.pdf) | yes |
| E088 | feasibility | adjacent | empirical finding | [pmc12953392](https://pmc.ncbi.nlm.nih.gov/articles/PMC12953392/) | yes |
| E089 | feasibility | adjacent | empirical finding | [ijim2024](https://doi.org/10.3991/ijim.v18i18.50545) | yes |
| E090 | feasibility | adjacent | expert advice | [sciltp2026](https://media.sciltp.com/articles/2602003085/2602003085.pdf) | yes |
| E091 | feasibility | extrapolated | empirical finding | [passalenti2019](https://air.uniud.it/handle/11390/1165358) | yes |
| E092 | alternatives | extrapolated | empirical finding | [aismfc2025](https://link.springer.com/article/10.1186/s13636-025-00391-9) | yes |
| E093 | current-practice | adjacent | expert advice | [bjerstedt2016](https://www.cambridge.org/core/journals/british-journal-of-music-education/article/stealing-knowledge-in-a-landscape-of-learning-conceptualizations-of-jazz-education/77013C652DEC5588A5AB3AF990E0BAE8) | yes |
| E094 | current-practice | adjacent | expert advice | [bjerstedt2016](https://www.cambridge.org/core/journals/british-journal-of-music-education/article/stealing-knowledge-in-a-landscape-of-learning-conceptualizations-of-jazz-education/77013C652DEC5588A5AB3AF990E0BAE8) | yes |
| E095 | learning-evidence | extrapolated | empirical finding | [lahav2007](https://doi.org/10.1523/jneurosci.4822-06.2007) | yes |
| E096 | learning-evidence | extrapolated | empirical finding | [lappe2008](https://doi.org/10.1523/jneurosci.2254-08.2008) | yes |
| E097 | learning-evidence | extrapolated | empirical finding | [guadagnoli2001](https://doi.org/10.1080/00222890109603152) | yes |
