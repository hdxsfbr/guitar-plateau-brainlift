Executive summary

This report synthesizes the empirical and engineering evidence on (a) how accurately automatic systems can measure guitar and other-instrument performances, and (b) whether automated or recorded-video feedback produces durable improvements in independent musical performance for adult intermediate guitarists. It integrates recent MIR system results (NMP, Spotify Basic Pitch, Fretwork), domain-specific assessment experiments (PianoEval, erhu practice system), controlled trials in adjacent domains (violin SkyNote, surgical simulation, VR box-trainer comparisons), and meta-level findings about AI-assessment behavior and human-rating reliability. Where possible I report numeric performance, study population, sample sizes and design features, and I highlight known failure modes, boundary conditions, and research gaps. The bottom-line for an AI-supported, adaptive guitar tutor for intermediate adults: automatic measurement is now good enough to support informative, actionable, frame-level feedback for many routine rhythmic/pitch errors and for tablature estimation in controlled conditions, but important limitations persist — especially in multipitch/pitch-detection under bleed/distortion, expressive technique recognition, and in producing feedback that transfers beyond the practice context. High-value product and research directions are (1) combine state-of-the-art polyphonic AMT (Basic Pitch/NMP) with guitar-specific tab assignment models and robust pre-processing (source separation/noise reduction), (2) implement rubric-aligned, explainable feedback with human‑in‑the‑loop calibration, (3) evaluate using randomized designs that measure delayed retention and transfer to new repertoire and ensemble playing, and (4) avoid over-reliance on real-time visual feedback that can impair on-task performance and create dependency.

Scope and approach

Research question: How accurately and validly can recordings of guitar (and other instrument) performances be assessed automatically, and does automated or recorded-video feedback improve learners' later independent performance? The learner profile is adult intermediate guitarists (2 hours/day practicing for ~2 years; ~1,400 hours total) aiming for advanced musicianship (hearing, technique, rhythm, harmony, expression, repertoire, improvisation, playing with others). I prioritized peer-reviewed empirical work, conference proceedings (ISMIR, ICASSP), dissertations, and technical reports from recognized MIR groups. I included adjacent-domain RCTs where they bear on motor-skill feedback (violin, surgical simulation, VR training) and automated-assessment reliability studies (PianoEval, erhu system, automated rater agreement experiments). I explicitly sought counterevidence and null results.

Terminology and evaluation metrics

- Automatic Music Transcription (AMT) / Audio-to-MIDI: conversion of audio to a symbolic representation (notes with onset, offset, pitch). For guitar, AMT must handle polyphony (chords) and guitar-specific articulations (bends, slides, vibrato). - Standard MIR evaluation metrics: note F-measure (precision/recall over detected notes), onset F1 with tolerance windows (common tolerance ±50 ms or ±25 ms), frame-wise F1, multi-pitch estimation (MPE) metrics, pitch accuracy measured in cents or semitone distances, and near-match F1 for allowable fret/voicing mismatches. - Assessment agreement/validity metrics: Pearson/Spearman correlations with expert ratings, intraclass correlation coefficients (ICC) for inter-rater reliability, Cohen’s kappa / Gwet’s AC2 for categorical rubric agreement, problem-note F1 for detection of erroneous notes.

1) Measurement accuracy: what automatic systems can (and cannot) do

Key systems and datasets

- NMP (Notes and Multipitch; Bittner et al., Spotify/ICASSP 2022): instrument-agnostic, fully-convolutional polyphonic AMT architecture producing onset/note/pitch posteriorgrams; small parameter count (~16,782). Reported state-of-the-art results on GuitarSet and outperformed recent strong instrument-agnostic baselines across five datasets. Runtime/memory: on a 2017 MacBook Pro, 490 MB peak / 7 s for a short file; 951 MB / 24 s for a 7m45s Slakh file. NMP performs comparably for MPE to larger systems using harmonic stacking while remaining low-resource. (Source: Bittner et al.)

- Spotify Basic Pitch: open-source, instrument-agnostic, polyphonic audio→MIDI transcription library that supports multipitch and pitch-bend detection (vibrato/glissando/bends). Designed to be lightweight and fast and used as the pitch-detection module in multiple downstream pipelines. The Basic Pitch GitHub integrates with GuitarSet for dataset processing (multif0 contours). (Source: Basic Pitch repository and Spotify engineering notes.)

- Fretwork (UC Berkeley capstone, 2026): an end-to-end guitar pipeline that merges GuitarSet with the large DadaGP tablature dataset and a transformer sequence model for playable-tab prediction. Full-pipeline F1 on GuitarSet improved from ~0.42 (baseline greedy) → 0.54 (CAGED+voicing heuristics) → 0.72 (+DadaGP) → 0.77 (transformer); near-match F1 = 0.78. Authors identify pitch detection (Spotify Basic Pitch) as the primary bottleneck (i.e., mapping audio→pitches before fret assignment). (Source: Fretwork capstone report.)

- GuitarSet (dataset): commonly used benchmark for guitar AMT research; Fretwork and NMP both report strong results on it. (Source references embedded in the systems above.)

Representative numeric accuracies and practical conditions

- Full-pipeline playable-tab F1 (Fretwork): improved to 0.77 (transformer + DadaGP), with near-match F1 0.78. These figures represent end-to-end accuracy from raw audio to playable tablature on GuitarSet using LOOCV evaluation. Conditions: GuitarSet recordings and aligned tab ground truth; pipeline used Spotify Basic Pitch for pitch detection. The main remaining errors were attributed to pitch detection failures under difficult audio conditions (bleed, distortion, certain chord voicings). (Population: dataset-level; not human subjects; experimental LOOCV.)

- NMP: reported state-of-the-art recording-level AMT performance on GuitarSet; superior to other instrument-agnostic baselines. Exact F-measures depend on dataset splits and metric definitions; NMP was especially notable for low-resource deployment (small model size and modest runtime memory). (Population: dataset-level.)

- Runtime/memory: NMP’s runtime on older hardware is practical for batch or near-real-time offline processing (490 MB / 7 s for short file). This matters for on-device or low-latency flows. (Source: Bittner et al.)

- Spotify Basic Pitch: performs well for multipitch and pitch-bend detection but remains a bottleneck in end-to-end tab pipelines: its pitch-detection errors propagate strongly to fretboard assignment and technique inference. (Source: Fretwork authors.)

Robustness to distortion, chords, recording quality and bleed

- Pitch detection under polyphony and bleed is the main practical limitation. Fretwork and other guitar AMT efforts explicitly identify pitch detection as the bottleneck. This reflects a broader MIR reality: instrument-agnostic multipitch methods can struggle under heavy harmonic complexity, expected bleed from backing tracks or amplified stage setups, and strong distortion or effects that alter harmonic spectra.

- Datasets like GuitarSet typically include multiple microphone positions and controlled performance conditions; real-world practice recordings (room mic, backing-track bleed, phone mics) are often more challenging and yield lower effective F1s. Neither NMP nor Basic Pitch intrinsically resolves bleed or extreme distortion — preprocessing (dereverberation, source separation) and guitar-specific post-processing improve robustness.

- Practical accuracies degrade substantially as SNR worsens or backing-track bleed increases; the literature and capstone reports indicate that the major failure modes are missed onsets, octave errors, and merged polyphonic pitches. Exact published degradation curves are sparse; the Fretwork report qualitatively attributes remaining full-pipeline error primarily to pitch-detection failures rather than fret assignment.

Conclusions on measurement accuracy

- For controlled recordings (close mic, minimal bleed, moderate effects), state-of-the-art instrument-agnostic AMT (NMP, Basic Pitch) plus guitar‑specific tab models (transformer+DadaGP) can generate near-playable tablature with full-pipeline F1 ≈ 0.72–0.78 on GuitarSet.

- For noisy, reverberant, distorted, or backing-track‑bleeding practice files typical of home practice, expect materially lower accuracy unless preprocessing (source separation, denoising) is applied and models are fine-tuned to those conditions.

- Latency and compute are feasible for offline and near-online processing using NMP/Basic Pitch on modern hardware; fully real-time assessment remains constrained by pitch-detection reliability and attention-management issues for learners.

2) Assessment validity: agreement with human experts and what can be assessed

What automatic systems match humans on

- Low-level pitch and rhythm: In many instrument contexts automatic systems produce high agreement with experts for pitch accuracy and rhythmic correctness when transcription is feasible. Example: an erhu end-to-end AI practice system (36 recordings from 18 conservatory students) reported very strong agreement with two expert raters (ICC = 0.92); system vs expert correlations were r = 0.93 (pitch) and r = 0.83 (rhythm). Problem-note F1 = 0.705 and problem-measure F1 = 0.763. This suggests highly structured, single-line bowed instruments in controlled conditions are amenable to automated error detection with good validity. (Source: erhu practice system report.)

- Multi-dimensional technical assessment (piano): On PianoEval (1,012 expert-annotated performances), a multi-task deep model achieved Pearson correlations of 0.91, 0.89, 0.85, 0.80 and 0.74 across five technique dimensions (average r ≈ 0.838), MSE = 0.024, and three-tier classification accuracy 81.7%. This is a high benchmark showing automated scoring can track multiple technique dimensions concurrently with strong criterion validity against expert annotations (Population: large dataset; system-level evaluation). (Source: PianoEval paper.)

- Automated creativity/expressivity proxies: In non-audio tasks (M-Flow music programming), automated creativity scores correlated with consensual human ratings (LLM-based r = 0.68; ECD-based r = 0.48), showing LLMs can approximate human judgments on open-ended creative artifacts with moderate-to-strong agreement when suitably calibrated. (Source: M-Flow study.)

Where automatic systems fall short

- Expressiveness, higher-level musicality, and technique nuance (free rubato, tone quality, nuanced right-hand fingering, subtle microtiming) are difficult to score robustly from audio alone. Even where pitch/rhythm are detected, mapping these low‑level features to high-level judgments (e.g., musically appropriate phrase shaping) is complex and often underdetermined.

- Polyphonic mixtures: complex chord voicings, dense textures, and strong distortion or effects upset pitch detectors and lead to false negatives/merging errors. Piano results do not map directly to guitar: piano is a percussive instrument with cleaner attack envelopes and less continuous pitch modulation than guitar techniques like bends and microtonal slides.

- Human expert agreement is itself imperfect. Automated systems can show high agreement against the average human label but may exceed consistency of human raters on open-ended tasks (e.g., ChatGPT-4 vs Gemini AI–AI agreement exceeded human–human in an OE scoring experiment). This raises the paradox that AI may be more internally consistent than human experts yet still fail to capture desirable subjectivity in performance assessment. (Source: automated rater study.)

Known failure modes and robustness

- Onset detection tolerance: Small onset timing errors (tens of ms) matter for rhythm evaluation; commonly used tolerances are ±50 ms or ±25 ms depending on tempo. Systems commonly use ±50 ms as a pragmatic threshold; tighter tolerances sharply reduce apparent F1.

- Pitch-bend and ornamentations: systems that ignore pitch-bend or vibrato will misrepresent intentional expressive pitch motion as errors unless pitch-bend-aware models (Basic Pitch supports this) are used and the scoring rubric accounts for expressiveness vs intonation errors.

- Source bleed and backing tracks: in ensemble or accompaniment contexts, high bleed dramatically lowers multipitch estimation reliability; source separation models help but are imperfect and introduce artifacts that can confuse downstream inference.

- Technique recognition (plucking hand position, fretting technique, pick angle): requires audio+video multimodal input or contact sensors. Pure audio models can infer some technique proxies (attack envelope, spectral centroid changes) but cannot reliably identify many technique categories with human-level validity.

3) Human rubrics and reliability for performance/improvisation

Benchmarks for how well automated assessment must perform

- Consensual Assessment Technique (CAT): widely used benchmark for creative/artistic evaluation where expert judges evaluate creative products on domain‑relevant criteria. CAT assumes that aggregate expert ratings serve as the validity criterion. For music performance and improvisation, CAT-like rubrics typically include dimensions such as technical accuracy, rhythmic precision, melodic/harmonic content, stylistic appropriateness, expressivity, and originality.

- Collegiate jazz improvisation rubrics and conservatory performance rubrics: The literature and pedagogical practice provide structured rubrics with ordinal scales for phrasing, motivic development, harmonic awareness, rhythmic placement, articulation, and time feel. Inter-rater reliability for such high-level constructs is often moderate (ICC or Pearson in the 0.5–0.8 range), depending on rater training and rubric specificity.

- Human reliability observed in studies: automated systems can match or exceed some pairwise human–human agreement metrics in constructed-response tasks (AI–AI A = 0.71 vs human–human A = 0.67; Gwet’s AC2 = 0.82 vs 0.43 in one 46-response study), but for music performance the reliability of experienced raters varies. The PianoEval dataset demonstrates that with carefully defined technical dimensions and expert annotations, high inter-rater consistency and system correlations are attainable (PianoEval multi-task model correlations up to r = 0.91). (Sources: automated-rater study; PianoEval.)

Implication: an automated system should target at least the range of human inter-rater reliability (ICC ~0.7–0.9 on technical dimensions) to be considered practically useful; for higher-level expressive judgments aim for moderate agreement and explicitly present uncertainty.

4) Learning benefit: does automated or recorded-video feedback improve later independent performance?

Positive evidence

- Erhu AI-practice system: reported high agreement with expert raters (ICC = 0.92) and problem-note/measure F1 ≈ 0.70–0.76. The study focused on assessment validity; while not a long-term RCT on learning transfer, such detection can enable targeted practice that plausibly supports learning. (Population: conservatory students; N = 18 students, 36 recordings.)

- PianoEval-style approaches (not necessarily RCTs) indicate multi-dimensional automated feedback can track technique reliably, an important prerequisite for effective practice systems that are adaptive and targeted. Large dataset benchmarking (N = 1,012) supports scalable model training.

- TELMI SkyNote (violin, RCT with beginners): Real-time visual feedback (RTVF) during practice improved bowing kinematics while feedback was present; although sound quality degraded during practice with RTVF, at retention the feedback group showed better sound-quality outcomes, particularly in control of dynamics. However, RTVF was attentionally demanding: 55.2% of RTVF participants agreed/strongly agreed they could not play while watching feedback. (Population: beginner violinists; randomized trial; sample size not cited in provided learning summary.)

- Broader psychological effects: assessment-oriented AI tends to strengthen learners’ ability beliefs and support self-monitoring/self-reflection; generative AI enhances value and intentionality; comprehensive/adaptive AI supports forethought and sustained engagement. These motivational effects can indirectly support learning outcomes when systems are well-designed. (Source: review on psychological effects of AI tools.)

- Surgical simulation and motor learning analogies: automated assessment systems in structured motor tasks can produce high classification accuracies (AUC 0.85–1.00; accuracies up to 99% on simulated tasks). Although domain differences exist, this indicates potential for automated feedback to accelerate acquisition of structured procedural skills. (Sources: surgical-simulation literature.)

Evidence for durable transfer vs limited/no effect

- Positive delayed retention from feedback: SkyNote’s RCT found that while RTVF impaired concurrent sound-quality, it produced better retention (improved sound-quality control) — suggesting that feedback can have beneficial delayed effects even if it distracts during practice. This points to the importance of evaluating retention/transfer rather than in-session performance only.

- Counterevidence in VR vs box-trainers: Seven RCTs comparing VR with haptics vs box trainers for laparoscopic skills found box trainers produced superior learning curves and greater improvements; VR did not show transfer superiority. The surgical literature cautions that high-fidelity or immersive feedback does not automatically translate to transfer. (Source: VR vs box trainer RCTs.)

- Dependency and attentional load: RTVF and many real-time visualizations impose attentional costs—over half of SkyNote participants reported inability to play while watching feedback—raising the risk that learners rely on the visualization rather than internalizing skill. This raises design constraints for real-time visual feedback in instrumental practice, especially for adult intermediate players who may need to practice in context (with backing tracks/ensemble) where visual attention must be directed to playing and listening.

- Studies showing no benefit or mixed results: multiple comparative studies in motor training show heterogeneity; some RCTs yield null results, and reporting gaps impair generalizability. The existence of null findings in adjacent domains means we must not assume automated feedback reliably produces large transfer without careful instructional design, spacing, and evaluation. (Sources: surgical sim literature; systematic reviews noting heterogeneity.)

5) Counterevidence, limitations, and risks

Major limitations

- Measurement limitations: pitch detection remains a primary bottleneck for end-to-end automatic assessment and tab generation. Distortion, backing-track bleed, polyphonic chords, and non-ideal microphone setups can all produce large accuracy losses.

- Expressive/interpretive judgments: automated systems have limited validity on higher-level expressive features and creative aspects of improvisation. Even when internally consistent, automated ratings may not capture what teachers value.

- Dependency and attentional issues: real-time visual feedback can degrade on-task performance and foster dependence; many learners struggle to integrate visual feedback while playing. This is a documented risk across instrument learning trials and must be managed via feedback scheduling and pedagogically informed UI.

- Misleading scores and overconfidence: objective-looking scores may reify narrow metrics (e.g., note F1, onset accuracy) and inadvertently shift learner focus away from musical goals (tone, groove, phrasing). The psychological literature suggests assessment-oriented AI strengthens ability beliefs but may also narrow attention.

- Generalization across genres/instrumentation: many validation studies involve classical conservatory players or controlled datasets; adult intermediate guitarists practicing with backing tracks and improvisation demands have fewer directly applicable controlled studies.

- Small samples and reporting gaps: several studies (e.g., erhu N=18 subjects) provide promising but small-sample evidence. Surgical simulation literature warns about generalizability limits due to heterogenous techniques and reporting gaps.

Synthesis for adult intermediate guitarists aiming to progress beyond a plateau

What automatic assessment can reliably support now

- Accurate detection of note onsets and sustained pitches under controlled recording conditions; robust tab inference when pitch detection is reliable. Expect near-playable tab generation (F1 ≈ 0.72–0.78) for clean recordings using modern pipelines (Basic Pitch / NMP + transformer tab models trained on DadaGP/GuitarSet).

- Reliable identification of recurring problem notes/measures (problem-note F1 ~0.70 in erhu system; similar performance may be achievable for single-line guitar tasks in clean conditions).

- Objective rhythmic evaluation at human-comparable reliability for fixed tolerance windows (e.g., ±50 ms); automated rhythm scoring can detect consistent timing errors and metronome alignment problems.

What remains fragile or out-of-scope

- Robust detection of playing technique (right-hand fingerings, subtle fretting-hand technique, pick angle) from audio alone — requires video, sensor, or hybrid input.

- Valid, general-purpose scoring of expressiveness, musicality, and improvisational quality — these require carefully designed rubrics and likely human calibration.

- Robust performance under real-world noisy practice contexts (backing track bleed, phone mic) without additional preprocessing or fine-tuning to those recording conditions.

Recommendations for an AI-supported adaptive guitar and musicianship tutor

System architecture suggestions (engineering + pedagogy)

1) Multi-stage audio pipeline
   - Preprocessing: source separation/denoising (Spleeter / X-UMX or hybrid ML+DSP restoration) to reduce backing-track bleed and reverb; optional dereverberation. (Note: ML+DSP hybrid approaches are active research; see 2025 Manchester dissertation for hybrid restoration techniques.)
   - Multipitch & note detection: use instrument-agnostic low-resource AMT (NMP, Basic Pitch) as base; enable pitch-bend support in Basic Pitch for correct handling of bends/vibrato.
   - Post-processing guitar specialization: map multipitch outputs to fretboard assignment via a transformer sequence model trained on DadaGP + GuitarSet (Fretwork approach). Include CAGED/voicing constraints as priors to prefer plausible fingerings; use near-match matching to accept musically equivalent voicings.
   - Technique classifiers: enrich with video (hand keypoint detection, optical flow) and audio attack/spectral features to infer pick vs finger, palm muting, slides, bends, vibrato. Labeling may require a small, high-quality multimodal dataset.

2) Assessment & rubric layer
   - Map low-level detections to pedagogical rubric dimensions: intonation (mean cents error, note error rates), rhythm (onset deviation distributions, tempo drift), timing (microtiming and groove metrics), technique (binary/multi-class tags for common issues), and expressivity (variance features and comparison to exemplar templates). - Provide explicit uncertainty intervals and probabilistic explanations for each detected problem.

3) Feedback design and pedagogy
   - Avoid continuous high-resolution real-time visual displays that demand visual attention while playing. Instead use (a) brief in-place cues (haptics/audio) for gross errors, (b) post-pass visualizations and short video-synced playback for reflection, and (c) scheduled delayed feedback to support retention. SkyNote suggests delayed retention gains although RTVF is attentionally demanding during practice.
   - Provide scaffolded practice tasks: isolated measures, slow deliberate practice, targeted technique drills, and varied-context transfer (different tempos/backing tracks). Use spaced repetition scheduling and simulated ensemble/practice-with-others modes.
   - Combine assessment-oriented feedback (objective, diagnostic) with generative accompaniment and suggestions (LLMs for practice plans) to support motivation and forethought. Be wary of over-reliance on the score; present broader musical goals.

4) Human-in-the-loop and explainability
   - Allow teachers to calibrate scoring rubrics, to override or annotate automated feedback, and to train personalization models. Provide exportable reports that match standard human rubrics (e.g., CAT-style dimensions) for teacher review.

Evaluation protocol for product validation and research

Design a rigorous RCT targeted at adult intermediate guitarists (this is essential to prove transfer beyond in-app improvement):
- Subjects: N = 90–150 adult intermediate guitarists (randomized) or larger if feasible; stratify for acoustic vs electric, amp/effects use, and prior improvisation skill.
- Arms (example): (A) Automated feedback (post-pass, rubric-based, multimodal) + practice plan; (B) Recorded-video self-review group with same rubric prompts but no automated scoring; (C) Control (practice as usual or metronome-only). Optionally include a fourth arm with real-time visual feedback to replicate SkyNote-style conditions.
- Duration: 8–12 weeks intervention with baseline, immediate post-test, and delayed retention test at 4–8 weeks post-intervention.
- Outcome measures: blind expert ratings using consensual assessment technique (multiple raters, compute ICC), independent performance on transfer pieces (unfamiliar repertoire and ensemble/play-along), objective AMT-derived measures (note F1, onset F1 with ±50 ms, mean cents error, problem-note F1), and psychosocial measures (self-efficacy, engagement). Also measure in-practice behavior logs (time, task types).
- Hypotheses: automated post-pass rubric-aligned feedback will outperform control on delayed retention/transfer of targeted technical dimensions; recorded-video self-review will show intermediate benefit; real-time visual feedback may aid kinematic measures but risk poorer immediate sound quality during practice and mixed retention advantages.

Research gaps and prioritized next experiments

1) Robust multipitch/pitch-detection under real-world practice conditions: quantify degradation curves (F1 vs SNR, backing track loudness, distortion level) using controlled signal manipulations on GuitarSet/augmented datasets. 2) Multimodal technique dataset: build a labeled corpus of guitar audio+high-resolution video+tab for fingerings and common techniques (slides, bends, vibrato, palm mute) to train technique classifiers. 3) RCT in target population: adult intermediate guitarists, with delayed retention and transfer tasks, to measure real learning effects (not just in‑app gains). 4) Study of feedback timing: compare immediate real-time visual feedback vs brief post-pass feedback vs delayed weekly summaries to assess retention, dependency and attentional costs. 5) Human rubric calibration studies: measure inter-rater reliability on improvisation rubrics and develop mapping functions from low-level features to rubric dimensions.

Practical recommendations for product development (prioritized)

1) Build the core transcription pipeline using Basic Pitch (for pitch-bend support) and/or NMP for low-resource needs; integrate DadaGP and a transformer tab model (Fretwork approach). Expect near-playable tabs for clean recordings; implement preprocessing for home-practice conditions. 2) Make feedback post-pass and rubric-aligned by default; offer optional recorded-video self-review workflows synchronized with the automated analysis. 3) Provide uncertainty and explicit limitations in feedback statements; surface common failure modes (‘‘low confidence in pitch detection due to backing track bleed’’). 4) Include teacher calibration mode so instructors can override and retrain assessment mappings. 5) Instrument evaluation: run an internal RCT with retention/transfer endpoints before product claims.

Speculative ideas (flagged)

- Use foundation audio models (e.g., MusicBERT/MERT-style pretrained encoders) as representations for downstream assessment; early evidence suggests Transformer/pretrained audio models provide powerful features for MIR tasks (speculative but promising).  - Leverage LLMs to generate pedagogically effective practice plans and explainable narrative feedback from quantified diagnostics, but validate that generated advice aligns with expert pedagogical practice. - Consider on-device light-weight AMT (NMP’s small parameter count is attractive) combined with cloud-based heavier models for in-depth post-practice analysis.

Concluding assessment

Automated analysis of guitar performance has reached considerable maturity for structured, single-line tasks and for generating playable tabs from clean recordings: end-to-end F1s of ≈0.72–0.78 (Fretwork) are now reported on benchmark datasets. AMT models like NMP and tools such as Spotify Basic Pitch provide practical building blocks. Automated assessment correlates strongly with human raters for many low-level technical dimensions (e.g., pitch, rhythm), as shown in PianoEval and erhu system reports. However, expressive evaluation, robust performance under noisy/bleeding backing tracks, and reliable technique recognition from audio-only inputs remain important challenges. Evidence about learning transfer is mixed: automated and recorded-video feedback can improve retention and technique in some controlled trials (SkyNote, surgical simulation analogies), but there are documented attentional costs, dependency risks, and multiple null or mixed findings in adjacent domains. For an adult intermediate guitarist population seeking to overcome plateaus, the most promising AI tutor strategy is a hybrid approach: robust preprocessing + state‑of‑the‑art AMT + guitar‑specific tab/technique modules + rubric-aligned, multimodal feedback delivered in pedagogically informed schedules with human-in-the-loop calibration and rigorous evaluation using retention/transfer endpoints.

Appendix: Key quantitative findings and sources summarized (from provided learnings)

- Fretwork full-pipeline playable-tab F1: ~0.42 (baseline greedy) → 0.54 → 0.72 → 0.77 (transformer + DadaGP); near-match F1 0.78. Main bottleneck: pitch detection (Basic Pitch). (Source: Fretwork capstone, UC Berkeley, 2026.)

- NMP (Bittner et al., ICASSP 2022): instrument-agnostic AMT architecture with ~16,782 parameters; state-of-the-art results on GuitarSet; runtime/memory: 490 MB/7s short-file; 951 MB/24s for 7m45s Slakh file. (Source: ICASSP/ArXiv paper.)

- Spotify Basic Pitch: open-source polyphonic audio→MIDI library; supports multipitch and pitch-bend detection; used in GuitarSet processing. (Source: Basic Pitch engineering notes/GitHub.)

- PianoEval: multi-task deep model on 1,012 expert-annotated piano performances; Pearson correlations across five technique dimensions: 0.91, 0.89, 0.85, 0.80, 0.74 (avg ≈0.838); MSE = 0.024; 3-tier classification accuracy = 81.7%. (Source: PianoEval publication.)

- Erhu practice system: 36 recordings from 18 conservatory students; ICC (system vs experts) = 0.92; system vs expert r = 0.93 (pitch), r = 0.83 (rhythm); problem-note F1 = 0.705; problem-measure F1 = 0.763. (Source: research report on erhu system.)

- Automated rater comparison (OE responses): AI–AI pairwise agreement higher than human–human (Robinson’s A = 0.71 AI–AI vs 0.67 human–human; Gwet’s AC2 = 0.82 vs 0.43). (Source: automated rater study.)

- TELMI SkyNote violin RCT: RTVF improved bowing kinematics during practice but degraded sound quality while feedback was present; however, at retention the feedback group showed better sound-quality outcomes (esp. dynamics). RTVF was attentionally demanding (55.2% could not play while watching feedback). (Source: SkyNote RCT.)

- Surgical-simulation automated assessment: very high accuracies reported (AUC 0.85–1.00; 97–99% accuracy on some VR box datasets); heterogeneous reporting limits generalizability. (Source: surgical simulator literature.)

- Liverpool St. Pölten gait classification: SVM on GRF components achieved 91% classification accuracy on GaitRec; 97% when using FFNN‑estimated physiological GRFs. (Included as an example of structured motor-skill classification successes.)

- Hybrid ML+DSP audio restoration dissertation (Manchester, 2025): documents recent advances in combining ML and traditional DSP for restoration; relevant for preprocessing/backing-track bleed mitigation. (Source: dissertation.)

Final note on research pragmatics

When building or evaluating an AI tutor, explicitly separate measurement reliability (how well we can detect what happened) from pedagogical efficacy (whether feedback improves learning and transfer). Current methods provide useful measurement for many tasks in controlled settings; product design must explicitly address robustness to real-world recordings, pedagogical sequencing, attention/load issues, and external validation via randomized retention/transfer studies. If you want, I can draft a detailed experimental protocol (power analysis, measurement instruments, rater training, data pipelines and labeling schema) targeted to an RCT with intermediate adult guitarists, or produce a prioritized feature roadmap and dataset plan for building the multimodal technique classifier and the Fretwork-like tab model adapted to noisy home-practice recordings.

## Sources

- https://github.com/spotify/basic-pitch
- https://arxiv.org/pdf/2203.09893
- https://engineering.atspotify.com/2022/6/meet-basic-pitch
- https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists
- https://huggingface.co/spotify/basic-pitch/blame/main/README.md
- https://ieeexplore.ieee.org/abstract/document/9746549/
- https://oadoi.org/10.1109/icassp43922.2022.9746549
- https://openreview.net/forum?id=zvjrteYiTd
- https://arxiv.org/html/2203.09893v2
- https://github.com/spotify/basic-pitch/blob/main/basic_pitch/data/datasets/guitarset.py
- https://huggingface.co/AEmotionStudio/basic-pitch-onnx-models/blob/main/nmp.onnx
- https://books.google.com/books?hl=en&lr=lang_en&id=gYuMOUYwgvIC&oi=fnd&pg=PA6&dq=Basic+Pitch+robustness+study+backing-track+bleed+SNR&ots=BoG52w2-KY&sig=NsPsPSidEYKXvaS5ryyogk5WuMY
- https://search.proquest.com/openview/1337c6c8a22a243dc4ebae56e4676f4f/1?pq-origsite=gscholar&cbl=2026366&diss=y
- https://ieeexplore.ieee.org/abstract/document/9829265/
- http://etheses.bham.ac.uk/5942/1/Senanayake15MD.pdf
- https://link.springer.com/article/10.1007/s10639-026-13949-7
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12807625/
- https://asgordon.github.io/publications/AVA.PDF
- https://oadoi.org/10.1007/s10111-018-0499-6
- https://www.nature.com/articles/s41598-026-72157-y.pdf
- https://files.eric.ed.gov/fulltext/EJ1483320.pdf
- https://www.researchsquare.com/article/rs-10127105/latest.pdf
- https://transactions.ismir.net/articles/343/files/6a634dd4d7c6a.pdf
- https://cs231n.stanford.edu/2025/papers/text_file_840592643-CS231n_Final_Paper__digital_audio_effects-4.pdf
- https://oadoi.org/10.3389/fpsyg.2021.648479
- https://pdfs.semanticscholar.org/666a/e0bb8574c45ff4b3263444843bf27c5ed72d.pdf
- https://oadoi.org/10.3758/s13423-012-0333-8
- https://www.ncbi.nlm.nih.gov/pubmed/33981275
- https://www.sciltp.com/journals/tai/articles/2602003085
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12953392/
- https://ieeexplore.ieee.org/iel8/6287639/10820123/11275896.pdf
- https://media.sciltp.com/articles/2602003085/2602003085.pdf
- https://oadoi.org/10.3991/ijim.v18i18.50545
- https://oadoi.org/10.1007/s00779-023-01723-2
- https://air.uniud.it/handle/11390/1165358