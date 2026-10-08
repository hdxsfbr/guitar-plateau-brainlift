<!--
url: https://www.researchsquare.com/article/rs-10127105/latest.pdf
title: Development and pilot validation of an AI-assisted self-practice ...
query: automated music performance assessment ICC study
fetched: 2026-10-08T02:24:47.292Z
-->



Development and pilot validation of an AI-assisted
self-practice system for erhu performance
assessment and score-aligned feedback
Xingzhi Guan 
UCSI University
Hanjun Su 
Jiangsu Urban and Rural Construction Vocational College
Masanori Fukui 
Mie University
Zhe Ji 
Universiti Teknologi MARA
Article
Keywords: erhu, AI-assisted music education, optical music recognition, automatic performance
assessment, non-Western music education, structured feedback
Posted Date: September 11th, 2026
DOI: https://doi.org/10.21203/rs.3.rs-10127105/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: No competing interests reported.

Page 1 
Development and pilot validation of an AI-assisted self-practice system for 
erhu performance assessment and score-aligned feedback 
Xingzhi Guan
1
, Hanjun Su
2
, Masanori Fukui
3
 *, Zhe Ji
4
,  
1 Faculty of Social Sciences and Liberal Arts, UCSI University, 56000, Kuala Lumpur, Malaysia 
2 School of Architectural Art, Jiangsu Urban and Rural Construction Vocational College, 
Changzhou, 213147, China 
3 Mie University, 514-8507, Tsu,Mie Prefecture,Japan 
4 Faculty of Music Universiti Teknologi MARA 40450 Shah Alam Selango , Malaysia 
*Correspondence: Masanori Fukui (fukui@info.mie-u.ac.jp). 
Email addresses: Xingzhi Guan: 1002268007@ucsiuniversity.edu.my; Hanjun Su: 
623728442su@gmail.com; Masanori Fukui: fukui@info.mie-u.ac.jp; Zhe Ji: 
2022654784@student.uitm.edu.my;  
  

Page 2 
Abstract 
AI music practice platforms are well established for Western instruments, but comparable 
support for the erhu, a fretless Chinese bowed string instrument, remains limited. We developed 
and pilot-validated an AI-assisted self-practice system that accepts PDF scores, analyses 
accompanied erhu recordings, and returns score-aligned feedback. The system combines 
Audiveris optical music recognition, score-informed harmonic masking, torchcrepe pitch 
tracking, madmom onset and beat detection, dynamic time warping alignment, and erhu-specific 
stable-segment and technique-tolerance rules. Thirty-six valid recordings from 18 conservatory 
students were blindly rated by two experts (ICC = 0.92). System scores correlated strongly with 
expert ratings for pitch (r = 0.93, 95% CI [0.82, 0.97]) and rhythm (r = 0.83, 95% CI [0.60, 
0.94]); problem-note F1 was 0.705 and problem-measure F1 was 0.763. In a five-item usability 
questionnaire (Cronbach&#39;s alpha = 0.923), all items scored significantly above the neutral 
midpoint. These pilot findings support the feasibility of score-aligned AI feedback for erhu 
practice, while requiring replication in larger and more diverse samples. 
Keywords: erhu; AI-assisted music education; optical music recognition; automatic performance 
assessment; non-Western music education; structured feedback 
1. Introduction 
The erhu, a Chinese traditional bowed string instrument, has no frets: each note&#39;s pitch 
depends on coordinated left-hand finger placement and right-hand bow control, with no 
positional reference. Unmarked pitch deviations during self-study tend to be reinforced and 
accumulate into motor memory that is difficult to reverse, yet most after-class practice happens 
without teacher guidance. 
Two problems have hindered computational practice systems for the erhu. First, general 
deep-learning pitch estimators fail to handle erhu-specific techniques: vibrato (regular frequency 
modulation, 4–7 Hz, 20–60 cents) and portamento (sustained pitch drift exceeding 1 cent/ms) are 
misinterpreted as intonation errors. Second, the prevailing audio-analysis pipeline lacks a clean 
way to map analytical results back to printed-score coordinates; automatic music transcription 
[7] aims at notation reconstruction rather than score-performance comparison. 

Page 3 
This paper addresses both problems with an end-to-end AI self-study system for erhu 
learners. The three contributions are: (1) An end-to-end practice system based on user-supplied 
PDF scores. Audiveris OMR automatically converts any PDF score into structured notes, and the 
pipeline closes a processing loop from score input to score-anchored feedback that previous AI 
practice tools have not achieved for non-Western instruments. (2) An erhu-specific stable-
segment algorithm coupled with technique-tolerant scoring. The method computes the 
confidence-weighted mean pitch only in the 20–82% stable range of each note and uses a 
heuristic classifier to recognise six erhu techniques (vibrato, portamento, trill, harmonic, 
pizzicato, col legno), distinguishing true intonation deviations from technique-induced 
fluctuations while preserving rhythmic accuracy. (3) Structured feedback mapping DTW-aligned 
analytical results to score coordinates. Problem notes appear directly on the score image as 
colour-gradient overlays, and measure-level natural-language summaries are generated, 
delivering actionable feedback without further interpretation by the learner. 
2. Related Work 
2.1. Automatic Performance Evaluation Technology 
Two paradigms have dominated automatic performance evaluation: classical signal 
processing and deep learning. The YIN algorithm [1] estimates fundamental frequency from the 
waveform difference function; pYIN [2] adds probabilistic threshold modelling and an HMM 
smoothing layer, significantly improving robustness to expressive techniques such as vibrato and 
trill. Both have served as key references but face performance ceilings in multi-component 
mixtures, high background noise, or rapid pitch changes. 
CREPE [3], a convolutional 16 kHz mono-audio pitch model, surpasses pYIN on 
benchmarks such as MDB-stem-synth; its PyTorch implementation torchcrepe is widely used. 
However, current deep-learning pitch models are trained mostly on piano and vocal recordings; 
on Chinese bowed instruments such as the erhu, vibrato-induced periodic fluctuations are treated 
as frame-level intonation deviations and portamento trajectories are fragmented into multiple 
note events—a systematic false-positive misclassification that has not yet been addressed. 
For onset detection, energy-based methods (e.g., spectral flux) have limited recall for soft-
bow attacks typical of slow erhu passages; madmom [4] introduces RNN-based onset detection 

Page 4 
that captures longer temporal patterns and improves recall for weakly attacked notes, alongside a 
DBN-based beat tracker. 
For alignment, Dynamic Time Warping (DTW) maps a performance time series to a score 
time series [5] via an optimal matching path. Foscarin et al. [6] built the ASAP dataset, and Peter 
et al. [14] released note-level score-to-performance alignments for piano. The main gaps in 
current automatic performance assessment remain: (i) intonation-tolerant models for the 
techniques of Chinese bowed string instruments, and (ii) a complete feedback mapping 
mechanism from analytical conclusions back to score coordinates. 
2.2. Optical Music Recognition and Score Structuring 
Optical Music Recognition (OMR) automates conversion of score images into machine-
readable form. Calvo-Zaragoza et al. [8] organise the OMR pipeline into four stages: image 
preprocessing, music object detection, score semantic reconstruction, and symbol encoding (e.g., 
MusicXML). Deep object-detection and segmentation networks have substantially improved 
symbol-level accuracy on standardised printed scores under controlled conditions, while 
handwritten notation, non-standard typesetting, and multi-voice cross-connections remain core 
bottlenecks. 
Audiveris is the most popular open-source OMR system; it uses a graph-based 
reconstruction strategy to convert PDF input directly to MusicXML. Its main engineering 
limitations are reduced accuracy below 200 DPI, limited support for non-Latin typesetting, and 
Java-Python integration overhead. 
The imperfect output of OMR motivates an &#39;OMR first, structured library fallback&#39; design at 
the application level, described in Section 3.2. 
2.3. Acoustic Features of Erhu Playing Techniques 
Vibrato (Chinese: rÛuxi·n) is produced by small regular finger motions on the string, 
yielding pitch fluctuations around the target. Acoustic studies report erhu vibrato modulation at 
4–7 Hz with depth varying by performer and style, typically 20–60 cents [9]. 
Portamento (glissando) links notes through a continuous monotonic pitch slide with change 
rates above 1 cent/ms and durations from ~30 ms to several hundred milliseconds. 

Page 5 
Trill is a fast alternation between two adjacent pitches at no less than three alternations per 
beat with an interval ≥50 cents, and must be distinguished from vibrato to avoid penalising it as 
an intonation error. These acoustic findings directly inform the detection thresholds and stable-
segment boundaries of the domain adaptation layer (Section 3.5). 
2.4. Comparison of AI-Assisted Music Education Tools 
Among commercial platforms, Yousician [11] is a gamified app for Western instruments 
with a closed score library, undisclosed pitch detection, and coarse feedback granularity. 
SmartMusic [12], aimed at school music education, supports more Western instruments and 
teacher-end course management but does not import PDF scores or handle bowed-string playing 
techniques specifically. 
At the academic level, several systems for the violin incorporate multimodal sensor data 
such as bow pressure and bow speed [10], but none provide an end-to-end pipeline from PDF 
score import to pitch and rhythm feedback for non-Western bowed strings. Table 1 cross-
sectionally compares representative existing tools and the proposed system on five core 
dimensions. 
Table 1. Functional Comparison of Existing AI Music Practice Tools. 
Dimension Yousician SmartMusic 
Academic string 
systems 
This system 
Instrument 
coverage 
Western instruments 
(guitar/piano focus) 
Western instruments 
(various) 
Violin/cello 
Erhu (non-Western 
bowed) 
PDF score import Not supported Not supported Not supported 
Supported (OMR 
integration) 
Deep learning 
analysis 
Undisclosed Undisclosed Partial CREPE + madmom 
Feedback 
granularity 
Note-level (partial) Segment-level Bow parameter level 
Note + measure + 
score coordinates 
Bowed technique 
tolerance 
Not supported Not supported Partial 
Vibrato / 
portamento / trill (6 
types) 
None of the surveyed tools combines free PDF score import, fault-tolerant scoring for 
bowed-string playing techniques, and score-coordinate feedback. The proposed system addresses 
all three gaps and, to our knowledge, is the first end-to-end AI practice system for a non-Western 
bowed string instrument. The acoustic-modelling and domain-adaptation methods described here 
may also provide a reference framework for related instruments such as banhu and erxian. 

Page 6 
3. System Design and Implementation 
3.1. System Introduction 
The system separates into three tiers: a React 19 Progressive Web App (PWA) front end for 
score display, recording capture, and feedback visualisation; a Node.js/Express middle-tier 
gateway for routing, file persistence, and task scheduling; and a Python FastAPI back-end 
analysis service for computationally intensive audio processing (Figure 1). The PWA 
architecture provides a near-desktop experience without installation and supports offline score 
reading via Service Workers. Table 2 lists the primary runtime dependencies and versions. 
The end-to-end workflow has two stages. Score preparation phase: the learner uploads a 
PDF score, which the system parses via OMR into a structured note sequence saved for later 
reuse. Performance assessment phase: the gateway forwards uploaded audio to the analysis 
service, which sequentially executes preprocessing, pitch and rhythm tracking, score alignment, 
error quantification, and feedback generation; results return as colour-gradient highlights on 
score coordinates for precise problem localisation. Per-module caching avoids redundant 
inference on the same recording. 
 
Table 2: Primary Runtime Dependencies and Versions. 
Layer Runtime / library Version / role 
Front end React, PWA (Workbox) 19.x 
Gateway Node.js, Express 24.x 
Analysis service Python, FastAPI 3.11 
Pitch detection torchcrepe (CREPE) 0.0.24 
Rhythm detection madmom 0.16.1 
Audio processing librosa, PyTorch 0.11.0 / 2.7.0 
OMR engine Audiveris 5.x 

Page 7 
3.2. Score Import Module 
Structured score representation is the basis for downstream audio analysis. Unlike practice 
systems that rely on manually entered MIDI or fixed libraries, the proposed system accepts user-
provided PDF scores: Audiveris converts scanned or digitally typeset scores into MusicXML, 
and an internal parser maps the MusicXML to a unified note JSON format (Figure 2). 
Each parsed note record has the following fields: note_id (unique note identifier), 
measure_index (measure sequence number of the note), beat_start (intra-beat start position), 
beat_duration (duration in beats), midi_pitch (MIDI pitch number), expected_onset (expected 
onset moment in seconds), and expected_offset (expected offset moment in seconds). This data 
format serves as the unified indexing basis for the following DTW alignment and feedback 
coordinate mapping (Table 3). 
When full-PDF recognition fails to produce a usable MusicXML, page-level confidence is 
low, or manual review detects voice-projection errors, the system activates a structured-library 
fallback: a manually verified note sequence is used directly for analysis. For the pilot, all 41 
segments and 328 notes of &#39;Taohuawu&#39; were manually verified. 
 
Table 3. JSON fields for structured score notes. 
Field Type Description 
note_id string Unique note identifier 
measure_index int Measure index, zero based 
beat_start float Beat-level onset position 
beat_duration float Duration in beats 
midi_pitch int MIDI pitch, e.g., D5 = 74 
expected_onset float Expected onset time in seconds 
expected_offset float Expected offset time in seconds 

Page 8 
3.3. Audio Preprocessing and Score-Informed Harmonic Spectral Masking 
All uploaded audio is decoded by ffmpeg and resampled to 16 kHz mono. The system then 
applies Score-Informed Harmonic Spectral Masking (SI-HSM) to separate the erhu melody from 
accompanied mixtures—the only original signal-processing algorithm in this work. Existing 
generic separators [13, 15] are trained on popular-music distributions and generalise poorly to 
traditional Chinese instruments; SI-HSM uses the system&#39;s score prior to avoid dependence on 
large-scale annotated training data. The five algorithm steps (Figure 3) are summarised below. 
Step 1: Harmonic-Percussive Source Separation. STFT is applied to the input and librosa&#39;s 
HPSS extracts the harmonic component, suppressing bow-hair friction and string-change 
transients. 
Step 2: Score-guided Pitch Fusion. Based on the frame-level pitch estimates 푓
CREPE
)ݐ( and 
confidence sequence )ݐ(ܿ output by torchcrepe, and using the expected score-derived pitch 
푓
score
)ݐ( as an auxiliary guide, the guided pitch is fused as follows: 
푓
guide
(ݐ(ܿ = )ݐ) · 푓
CREPE
( 1[ + )ݐ− ݐ(ܿ)] · 푓
score
)ݐ( 
(1) 
where )ݐ(ܿ is the frame-level confidence. When the performer uses vibrato or portamento, 
torchcrepe confidence drops and Equation (1) shifts weight toward the score pitch, preventing 
the mask from leaking into accompaniment bands. 
Step 3: Harmonic Mask Construction. At each harmonic frequency of 푓
guide
)ݐ( (up to 
harmonic number 
ܪ = 6), a Gaussian window frequency-band mask with a width of ±55 cents 
is constructed on the STFT frequency axis, and the masks of all harmonics are weighted and 
superimposed to form a two-dimensional time-frequency mask 
(ܯ푓, )ݐ∈ [0,1]. 
Step 4: Octave Flexibility and Piano Co-frequency Suppression. To absorb register errors or 
octave jumps, ±1 octave candidate frequencies participate in mask competition; bands 
corresponding to score accompaniment notes are de-weighted to suppress fixed-pitch co-
frequency components. 
Step 5: Masking and Confidence Fallback. The mask is multiplied elementwise with the 
harmonic STFT magnitude and inverted. A separation confidence is computed from energy ratio 
and pitch-band hit rate; if below the automatic-mode threshold (default 0.4), the system reverts to 
the original audio to prevent distortion. Figure 4 visualises the spectral effect of the mask on a 

Page 9 
representative recording. Three operating modes are available: off, automatic, and erhu-priority 
(forced). 
 
 
3.4. Deep Learning Performance Analysis Module 
After preprocessing, three feature-extraction pipelines run: pitch tracking, onset detection, 
and score alignment. All use a cache keyed by audio content hash to avoid redundant inference. 
Pitch Tracking. torchcrepe [3] estimates fundamental frequency at a 10 ms frame hop over 
120–1400 Hz (covering the erhu range), outputting (frequency, confidence, timestamp) triplets. 
Frames with confidence below 0.6 are excluded from intonation calculation; if too few valid 
frames remain, the system falls back to librosa.pyin [2]. 
Onset and Beat Detection. Two pre-trained madmom models drive rhythmic analysis [4]: 
RNNOnsetProcessor captures note onsets at 100 frames/s with adaptive peak picking, and 
DBNBeatTrackingProcessor uses a Dynamic Bayesian Network on RNN beat activations for 
global beat estimation. RNN-based methods are more reliable than energy-based detectors on 
slow erhu passages where bow attacks lack distinct transients. 
Score Alignment. The onset sequence is mapped to score notes via DTW alignment with 
cost: 

Page 10 
= )݆ ,݅(ܦ12|ݐ
̂
௜
ݐ −
̂
௝
| + 8|݀
̂
௜
݀ −
̂
௝
| + 6(1 − ݍ
௜
) 
(2) 
where t
̂
_i and d
̂
_i denote the i-th performance onset time and note duration normalised to the 
total segment duration, t
̂
_j and d
̂
_j denote the corresponding score-expected values for note j, q_i 
is the confidence of the i-th performed note, and the gap cost for skipped notes is fixed at 5.0. 
The coefficients 12, 8 and 6 are engineering hyperparameters calibrated by iteration and manual 
path inspection of practice recordings outside the study sample: onset deviation has the highest 
weight, duration deviation is next, and the low-confidence penalty is the lowest. Alignment uses 
a temporal prior mechanism, and the expected onset moments of score notes serve as the starting 
guide to restrict the window size of candidate matching; thus, path drift risk is reduced in long-
segment alignment. The alignment results provide a score-note index for each detected 
performer&#39;s note, and this index will be used in the following per-note error calculation (see 
Figure 5). 
 
3.5. Erhu Domain Adaptation Layer 
Generic deep-learning pitch estimators systematically misclassify expressive techniques: 
vibrato&#39;s periodic offsets are flagged as intonation errors, and portamento&#39;s continuous drift is 
interpreted as multiple deviation events. The domain adaptation layer addresses this through 
stable-segment trimming and technique-tolerance scoring. 
Stable-segment Algorithm. For each DTW-aligned note, the duration is partitioned into 
attack (0–20%), stable (20–82%), and bow-release (82–100%) phases. Intonation error is 
computed only on stable-phase frames (Figure 6). The 20–82% window was set by engineering 
calibration with teacher listening verification on out-of-sample practice recordings; truncating 
too early loses effective stable frames of short notes, while truncating too late retains audible 
bow-release slides. Bow acceleration during attack and bow deceleration during release both 

Page 11 
produce transient pitch artefacts that do not reflect true pitch control. The confidence-weighted 
mean stable-phase pitch is the representative note pitch, from which cents deviation relative to 
the score target is computed. 
Technique Detection and Fault-tolerant Scoring. Heuristic technique classification of pitch 
time series in stable segments (see Table 4) was carried out by the system, and the six categories 
of playing characteristics were identified: vibrato, portamento, trill, harmonic, pizzicato, and col 
legno. Vibrato identification is based on a dual-path parallel mechanism: the broad-range 
judgment path verifies if the pitch range in the stable section exceeds 26 cents, and the contour 
judgment path detects oscillation in the pitch sequence after a 2 Hz low-pass filter; this 
oscillation must have an amplitude between 8 and 50 cents and at least 4 zero-crossings for it to 
be classified as vibrato. Trill recognition is required to have a minimum amplitude of 50 cents 
for pitch alternation and at least three such alternations; Portamento recognition requires a pitch 
derivative greater than 1.0 cents/ms to be maintained for a minimum of 30 ms. Notes classified 
as vibrato or trill have an increased intonation tolerance of 10 cents above the baseline of 22 
cents (ceiling 45 cents); for notes classified as portamento, only the error in the entry pitch 
frames relative to the target pitch is calculated, and frames within the portamento transition 
interval are excluded from the penalty. This way can reduce the false-positive misclassification 
rate of bowed-string techniques in the intonation score and maintain the accuracy of rhythmic 
analysis (Section 4.2.10). 
For rhythm analysis, the detected onsets are compared with the expected onsets in the score, 
and six categories of rhythmic errors are defined: rushing (onset error &lt; -75 ms), dragging (onset 
error &gt; +75 ms), note value too short (actual duration &lt; 70% of expected), note value too long 
(actual duration &gt; 130% of expected), missed note (no onset matching a score note), and 
measure-level beat instability (onset variance within a measure exceeds the threshold); all these 
types are uniformly processed by the confidence-weighted scoring model. 

Page 12 
 
Table 4. Technique-detection Thresholds and Rhythm-error Criteria. 
Technique Detection criteria Score adjustment 
Vibrato Pitch modulation &gt;8 cents, &gt;=4 zero-crossings after 2 Hz LP filter Tolerance expanded +10 cents 
Portamento Pitch derivative &gt;1.0 cents/ms, sustained &gt;30 ms Entry frames excluded from penalty 
Trill Pitch alternation &gt;=3x, jump &gt;50 cents Scoring suspended 
Pizzicato Entry deviation &gt;70 cents, rapid convergence within 6 cents Entry frames excluded from penalty 
3.6. Structured Feedback Generation 
The analysis layer outputs a time-indexed error sequence, but learners act on score 
coordinates (measure index, note index). The feedback module performs this coordinate mapping 
and displays results on the score visualisation. 
Each DTW-aligned note inherits measure_index and note_id from the matched score-note 
record, requiring no extra time-to-coordinate conversion. Problem notes are colour-coded on the 
score image by severity (light yellow / orange / red), guiding learners to re-study specific 
sections (Figure 7). 
Unified Thresholding Function for Error Severity Grading: 

Page 13 
,݈;ݒ(݃ℎ) = {
0if |v| &lt; l
(
| |ݒ− ݈
)
(
݈ℎ−
)
if l ≤ |v| &lt; h
1if |v| ≥ h
 
(3) 
Intonation grading uses the cents deviation v of each stable-segment frame as the direct 
input, and has thresholds of low = 10 cents and high = 22 cents. Rhythm grading is calculated as 
the maximum of the median intonation deviation, half the median onset deviation, and half the 
median absolute duration deviation, and corresponding thresholds for low and high are 8 and 18, 
respectively; this composite index harmonizes multidimensional rhythmic errors into a single 
metric so that an unusually large error in one area does not go unnoticed because of other small 
errors. 
A template-driven generator produces measure-level summaries such as &quot;Measure 3, beat 2 
rhythm rushed by about 80 ms&quot; or &quot;Measure 5, D5 pitch sharp by approximately 32 cents&quot;. 
The two stages of transformation for pitch and rhythm errors in the scoring model reduce 
them to a range of 0-100. Stage 1 computes a large pitch and rhythm penalty as 
ܧ
pitch
= med(|߂푓
௜
|) + 2ܰ
pitch
ܰ +
uncertain
 
(4) 
ܧ
rhythm
= 0.5 · med(|ݐ߂
௝
|) + 1.5ܰ
rhythm
+ 2ܰ
measure
 
(5) 
where med(|߂푓
௜
|) is the median cents deviation within a stable segment, ܰ
pitch
 is the number 
of problem notes, 
ܰ
uncertain
 is the number of low-confidence notes, medݐ߂|(
௝
|) is the median 
onset deviation, 
ܰ
rhythm
 is the number of rhythmic problem notes, and ܰ
measure
 is the number of 
problem measures. The small score is then obtained by 
ܵ
strict
= max(40,100 − ܧ) 
(6) 
The lower bound of 40 guarantees that score differences are retained after large deductions. 
Stage 2 converts the strict score into a beginner-friendly display score: 
ܵ
display
= min{98,ܵ
strict
+ (1 − ܿ
bar
) · max(0,85 − ܵ
strict
)} 
(7) 
where ܿ
bar
 is the torch.clamp function applied to the median confidence within [0.45, 0.95]. 
Empirical calibration in the pre-test determined that a moderate incentive was required for a 
score under 60, while values exceeding 85 remained close to the original. The composite display 
score is the arithmetic mean of the pitch and rhythm display scores after adjustment by the same 
formula, and it is output as the maximum value of this and the strict composite score. 

Page 14 
The practice-path module ranks measures by composite error, marks the worst as priority 
targets, and offers one-click entry to per-measure re-recording, closing a record-analyse-
feedback-practice loop. 
Practice path recommendation is a three-way choice based on a small score difference: 
path = {
rhythm-firstif ܵ
rhythm
+ 5  ܵ
pitch
pitch-firstif ܵ
pitch
+ 5  ܵ
rhythm
review-firstotherwise
 
(8) 
First, filter out recordings that have many low-confidence notes in the detected problem set. 
Among the valid recordings, if the rhythm-first option has a significantly lower rhythm-strictness 
score than the pitch-first option, then rhythm-first is chosen; otherwise, if pitch-first has a lower 
pitch-strictness score, it is selected; and if the two are too close, the review-first choice is 
retained. 
 
3.7. Whole-Piece Concurrent Analysis Module 
Sections 3.1–3.6 describe the single-segment evaluation pipeline. The system also supports a 
piece-level analysis mode that partitions an entire-piece recording and processes the segments in 
parallel for a macro-level diagnosis. Single-segment practice feedback only covers the learner&#39;s 
current submission and cannot provide an all-encompassing diagnostic overview of the entire 
work; the Whole-Piece Pass Analysis module described here enables comprehensive evaluation 
of a full-piece recording through the three steps shown in Figure 8. 
Step 1: Segmentation Localisation. A pitch trajectory is extracted from the whole recording 
(torchcrepe capped at 1800 frames), and full DTW alignment is performed for each candidate 
score segment. Candidate-segment scores: 

Page 15 
ܴ
seg
= 0.   50 · ܵ
pitch
+ 0.   30 · ܵ
rhythm
+ 20 · confidence − 3ܰ
measure
ܰ −
note
 
(9) 
where ܵ
pitch
 and ܵ
rhythm
 are the strict scores of the current alignment, confidence is the 
median pitch confidence, and 
ܰ
measure
 and ܰ
note
 are the number of problem measures and 
problem notes, respectively. Segments with alignment failure are given a ranking score of 0 and 
not included in the aggregation. Select the segment with the highest ranking score from the 
system as the matched segment for this performance. The segment localisation process reuses the 
SI-HSM preprocessing from Section 3.3 to improve instrument blending in accompanied 
recordings and pushes progress updates to the front end every 8 seconds via a background thread 
to avoid making users feel that the interface is slow to respond. 
Step 2: Simultaneous Analysis. The back-end is invoked concurrently (default 3 workers) to 
evaluate all sections independently. For the Taohuawu test, the concurrent mode processed 41 
segments in ~17 s vs ~5 min serial—an engineering speedup of about 18◊ (engineering 
verification only, not a participant outcome). 
Step 3: Whole-piece Summary. Pitch and rhythm scores are aggregated; segment-level 
coverage (successful segments / attempted) is computed; the weakest-pitch and weakest-rhythm 
measure ranges are annotated to support macro-level practice plans. 
If coverage is low, the summary prompts the learner to supplement missing segments before 
resubmission. This piece-level overview adds a multi-granularity layer that complements the 
single-segment, note-by-note feedback of the main pipeline. 
 
 

Page 16 
4. Experiments and Results 
4.1. Experimental Setup 
4.1.1. Experimental Environment 
The Windows workstation in the system has an Intel Core i7 processor and 16GB of RAM. 
The Python analysis service is based on FastAPI; torchcrepe is used for pitch extraction (target 
sampling rate: 16 kHz), madmom RNN-onset is employed for note onset detection, and the 
MusicXML parser within the service is responsible for score recognition. DTW alignment, SI-
HSM stable-region detection and structured feedback generation are all performed locally and do 
not require an external network. The average analysis time for a single segment (around 8 
seconds, 4-10 notes) is 2.3 seconds (SD = 0.4 seconds), and this is suitable for after-class self-
study. 
4.1.2. Test Repertoire 
The first erhu piece that served as a test case was &quot;Taohuawu&quot;. It has various types of 
playing techniques, such as different intonation ranges, rhythms and ornaments, etc., and is thus 
very typical. The 41 standard segments of the piece in the experiment were approximately 8 
seconds long each, and they contained 3-10 notes with various difficulties and techniques. 
4.1.3. Participants 
A total of 18 major students of the erhu at Sichuan Conservatory of Music were recruited (7 
male, 11 female, mean age 20.4 ± 1.3 years, mean years of study 11.6 ± 2.3 years), all from the 
erhu program of the Folk Music Department, randomly sampled in proportion across years 1-4 (5 
freshmen, 5 sophomores, 4 juniors, and 4 seniors). Inclusion Criteria: More than 8 years of erhu 
study with no known hearing impairment. All the participants gave written informed consent. 
The year distribution of the participants was the same as that of all students in the erhu program 
at the Sichuan Conservatory of Music. These 18 participants provided a total of 36 primary 
analysis recordings for system accuracy verification (Section 4.2), and all 18 completed and 
submitted full usability questionnaires (Section 4.3). 
Ethics Statement 
This study has been approved by the Universiti Teknologi MARA (UiTM) Research Ethics 
Committee, Reference No.: REC/01/2026 (PG/MR/37). All procedures involving human 

Page 17 
participants were conducted in accordance with relevant ethical guidelines and regulations, and 
informed consent was obtained from all participants before data collection. 
4.1.4. Expert Rating Protocol 
The expert rating protocol in this paper uses the Performance Evaluation Rating Scale 
(PERS) for string instruments that Wrigley and Emmerson developed [16]. The subscale of the 
PERS string instrument has been verified for ecological validity with an internal consistency 
coefficient (α) ranging from 0.81 to 0.98 and has been widely employed in research on the 
intonation and rhythm attributes of string instruments by experts. This study mapped the original 
PERS seven-level scores to the system&#39;s narrow range of scores (40-98), constructed two 
independent anchor rubrics for intonation and rhythm (as shown in Table 5 and Table 6), each 
with textual descriptions of erhu performance features at that level, to reduce rating variability 
due to differences in subjective judgment among experts. The PERS-to-system-score mapping is 
a piecewise decadal banding: each of the seven PERS levels corresponds to a 10-point system 
band (Level 7 → [90, 98]; Level 6 → [80, 89]; Level 5 → [70, 79]; Level 4 → [60, 69]; Level 3 
→ [50, 59]; Level 2 → [40, 49]), with Level 1 collapsed to the floor value of 40. This anchored-
band design preserves the ordinal structure of the original PERS and lets experts express finer 
within-level judgment by selecting any value within the corresponding band; the union of the 
seven bands spans the system&#39;s strict-score range defined in Section 3.6. 
Two associate professors in the erhu program at Sichuan Conservatory of Music (both with 
more than 15 years of professional teaching experience) independently and blindly rated all 
recordings in isolation from one another; the raters were unaware of the participant year 
information and had no access to system output. Before the official assessment, both groups of 
experts performed five practice recordings outside the study group for calibration and found that 
the mean score differences in intonation and rhythm were less than 8 and less than 10 points, 
respectively. In addition to the overall pitch and rhythm scores, both experts independently 
recorded problem note IDs and problem measure indexes in a unified review sheet for later 
precision/recall/F1 calculations, and teachers did not receive information on the system&#39;s 22-cent 
or ±75ms operating range during annotation. Before observing the system&#39;s recommendation 
results, the two experts were given a primary practice-path label (pitch-first, rhythm-first or 
review-first) for each recording based on the blinded score sheets, and this consolidated expert 

Page 18 
main path served as the ground truth for Section 4.2.6. The final mean of the experts was taken 
as the rating standard, and the intra-class correlation coefficient (ICC) [17] was reported for 
inter-rater reliability. 
Table 5. Pitch Anchor Rubric Adapted from PERS. 
Level Pitch description (string instruments) Mapped score 
7 - Excellent 
All notes precisely in tune; vibrato, 
portamento, and other techniques smooth and 
natural, no notable pitch deviation 
90–98 
6 - Good 
Very few minor deviations (1-2 notes), 
technique performance overall accurate 
80–89 
5 - Above average 
Few notes with perceptible deviation (3-4), or 
slight pitch instability in technique passages 
70–79 
4 - Acceptable 
Multiple deviations (5-6 notes), but melodic 
pitch contour still recognizable 
60–69 
3 - Developing 
Frequent deviations (&gt;1/3 of notes), overall 
intonation unstable 
50–59 
2 - Beginning 
Most notes show obvious deviation, melodic 
contour unclear 
40–49 
1 - Insufficient Target pitch largely unrecognizable 40 
Table 6. Rhythm Anchor Rubric Adapted from PERS. 
Level Rhythm description (string instruments) Mapped score 
7 - Excellent 
All note onsets accurate, durations well-
controlled, overall beat stable 
90–98 
6 - Good 
Very few onset deviations (1-2 notes), 
overall beat fluent 
80–89 
5 - Above average 
Few notes rushing or dragging (3-4), or 1 
measure beat-unstable 
70–79 
4 - Acceptable 
Multiple rhythm deviations (5-6 notes), or 
globally fast/slow but still recognizable 
60–69 
3 - Developing 
Frequent rhythm problems (&gt;1/3 of notes), 
beat sense persistently unstable 
50–59 
2 - Beginning 
Most notes with obviously incorrect 
duration or onset, beat chaotic 
40–49 
1 - Insufficient Stable beat largely unachievable 40 
4.1.5. Experimental Procedure 
The participants followed the steps listed below to conduct the experiment (each person was 
assigned two passage sections to be recorded in sequence; the following steps were repeated 
independently for each section): (1) Record or upload the current repertoire segment through the 
system; (2) Automatically perform pitch extraction, DTW alignment and structured feedback 
generation by the system to output intonation scores, rhythm scores and per-note problem 
locations; (3) Two expert teachers independently rated the recording and recorded problem notes 
and problem measures in a blinded manner; (4) After completing both recordings, fill out a 5-
item Likert scale questionnaire based on overall usage experience. 

Page 19 
4.1.6. Supplementary Evaluation Protocol 
Supplementary analysis of the same 36 primary recordings from the 18 participants was 
carried out to evaluate component contributions and calibrate the stable-segment window. 
4.2. System Accuracy Assessment 
4.2.1. Inter-Rater Reliability 
Before conducting a system-expert comparison, check for any internal inconsistency in the 
scores of the experts. ICC(2,1) was computed under a two-way random-effects model with 
absolute agreement, using only the two expert ratings (E1/E2); system scores were excluded 
from the ICC computation and assessed separately via Pearson r, MAE and RMSE. The ICC for 
the two experts&#39; intonation ratings was 0.92 (95% CI: 0.80–0.97), and for rhythm ratings it was 
also 0.92 (95% CI: 0.80–0.97); both exceeded 0.75 and were considered good or excellent, thus 
the expert scores can serve as an accurate reference for later comparisons between the system 
and humans. 
4.2.2. Intonation Assessment Accuracy 
Based on the consistency-verified expert mean scores as the benchmark, the Pearson 
correlation coefficient of the primary participant-level system intonation score with this 
benchmark was r = 0.93 (95% CI [0.82, 0.97], p &lt; .001), with a Mean Absolute Error (MAE) of 
2.67 points (out of 100) and a Root Mean Square Error (RMSE) of 2.99 points. Figure 9 is the 
scatter plot of the system and expert scores. Therefore, the intonation assessment module of 
torchcrepe based on pitch extraction and improved DTW alignment has been found to be in good 
agreement with professional teacher judgments. The participant-level value differs from the 
recording-level correlation because the latter is computed over the 36 individual recording pairs 
before participant aggregation; at the recording level, pitch r = 0.818 with a participant-cluster 
95% CI of [0.661, 0.909] (see Section 4.2.8), and rhythm r = 0.664 with a participant-cluster 
95% CI of [0.395, 0.859]. The participant-level r values are used as the primary score-agreement 
indicators because the two recordings from the same participant are not considered fully 
independent observations. 

Page 20 
 
4.2.3. Rhythm Assessment Accuracy 
The Pearson r between system rhythm scores and expert rhythm scores = 0.83 (95% CI 
[0.60, 0.94], p &lt; .001), MAE = 4.17 points, and RMSE = 5.42 points. Analysis of the above 
results shows that in sections with rubato (5 sections, 13.9% of the whole), the MAE of rhythm 
assessment was 5.0; excluding these sections, the MAE dropped to 2.0. Therefore, it is expected 
that there will be a lack of accuracy in the assessment of rhythm in tempo-free sections, and 
certain adjustments to the system will need to be made. An r of 0.83 is also considered a 
relatively large effect size, lower than the intonation correlation coefficient, and in line with 
expectations that rhythm recognition is generally more difficult. Table 7 summarises expert 
reliability and the system-expert agreement metrics across both dimensions. 
Table 7. Expert Reliability and System-Expert Agreement Summary. 
Evaluation dimension ICC(2,1) E1/E2 ICC 95% CI 
Pearson r (95% 
CI) 
MAE RMSE 
Pitch 0.921 [0.805, 0.970] 
0.929 [0.817, 
0.974] 
2.67 2.99 
Rhythm (with rubato) 0.922 [0.804, 0.970] 
0.833 [0.599, 
0.936] 
4.17 5.42 
Rhythm (excluding 
rubato) 
— — — 2.00 — 
4.2.4. Problem-Note Localization Accuracy 
The problem-note ground truth is obtained from independently annotated positions of 
problem notes by both experts under blind conditions and then consolidated; it is not directly 
applied to the same signal via system thresholds. The 22-cent intonation tolerance and ±75 ms 
rhythm tolerance mentioned in the text are only for the system&#39;s operational labelling and do not 
serve as teacher annotation instructions. Based on the expert annotations as the reference, the 
localization results of the per-note for the system are: Precision = 0.731, Recall = 0.680, F1 = 
0.705. Precision is higher than Recall; thus, most of the notes that the system has marked as 

Page 21 
problematic are indeed deficient, and borderline minor deviations are more likely to be 
considered acceptable by the system. 
4.2.5. Problem-Measure Localization Accuracy 
At the level of measures, the results of problem localisation are: Precision = 0.787, Recall = 
0.740, F1 = 0.763. Measure-level F1 is higher than note-level because measure problems are 
aggregated judgments of multiple note problems with more evidence, and thus have relatively 
lower boundary misclassification rates. Table 8 summarises problem-localisation precision, 
recall, and F1 at both granularities. 
Table 8. Problem-localization Accuracy at Note and Measure Levels. 
Level Precision Recall F1 
Note level 0.731 0.680 0.705 
Measure level 0.787 0.740 0.763 
4.2.6. Practice Path Recommendation Accuracy 
The system recommends one of three practice priorities: pitch-first, rhythm-first, or review-
first; accuracy is judged by recording-level agreement with expert main-path labels (annotated 
before system evaluation on a blinded rating sheet). Of 36 recommendations (15 pitch-first, 14 
rhythm-first, 7 review-first), the overall agreement rate was 77.8% (28/36): 80.0% for pitch-first, 
78.6% for rhythm-first, and 71.4% for review-first (Table 9). Both exceed the three-class random 
baseline (36.3%) and the majority-class baseline (41.7%). Review-first results (n=7) are 
reference only. 
Table 9: Practice-Path Recommendation Agreement. 
Recommended path Recordings Matches Accuracy 
Pitch-first 15 12 80.0% 
Rhythm-first 14 11 78.6% 
Review-first 7 5 71.4% 
Overall 36 28 77.8% 
4.2.7. Component Ablation Study and SI-HSM Evaluation 
To determine the independent contributions of all modules, a series of ablations were 
performed by disabling them one by one while keeping the same 18 subjects and 36 initial 
recordings for all experiments. The five conditions were: the full system, removal of stable-
segment trimming, removal of technique tolerance, removal of SI-HSM, and a raw baseline. The 

Page 22 
four indicators of the results are shown in Table 10: pitch correlation, rhythm correlation, note-
level F1 and measure-level F1. 
Ablation studies disable one component at a time and keep the same 18 participants and the 
same 36 primary recordings for every variant. Table 10 presents the five variants in the four 
metric columns: pitch correlation, rhythm correlation, note-level F1 and measure-level F1. All 
four indicators of the whole system are at their peak. Removal of the stable-segment trimming 
reduces pitch r from 0.929 to 0.835 and note F1 from 0.705 to 0.620; removing technique 
tolerance reduces pitch r to 0.872 and note F1 to 0.639; removing SI-HSM reduces pitch r to 
0.892 and note F1 to 0.657; and the raw baseline drops to pitch r = 0.775 and note F1 = 0.585. 
The above results show that all parts of the system contribute to the overall accuracy (see also 
Section 4.2.11). 
Table 10. Component Ablation Results for Five System Variants. 
Variant Pitch r Rhythm r Note-level F1 
Measure-level 
F1 
Full system 0.929 0.833 0.705 0.763 
No stable-
segment 
trimming 
0.835 0.77 0.62 0.731 
No technique 
tolerance 
0.872 0.793 0.639 0.724 
No SI-HSM 0.892 0.806 0.657 0.73 
Raw baseline 0.775 0.72 0.585 0.701 
SI-HSM was also tested on the 36 main recordings, with each record linked to its 
corresponding recording ID. Automatic SI-HSM activation was kept for 31 of the 36 recordings, 
and the confidence fallback was triggered for 5 recordings (13.9%), with a mean separation 
confidence of 0.716. Mean SDR, SIR and SAR were 8.93 dB, 13.57 dB and 11.35 dB. When 
falling back, enhanced audio is bypassed and raw audio is used for downstream pitch extraction; 
therefore, SIHSM_pitch_MAE equals raw_audio_pitch_MAE for those recordings. Across all 36 
recordings, the raw pitch MAE was 5.24 cents and the SI-HSM pitch MAE was 3.89 cents; a 
total reduction of 1.35 cents was achieved in these 36 recordings (1.56 cents for the 31 activated 
recordings that were not fallback cases). 
Table 11. SI-HSM Evaluation: Separation Confidence and Pitch MAE Comparison. 
Metric Value 
Automatic activation 31/36 
Fallback triggered 5/36 (13.9%) 
Mean confidence 0.716 

Page 23 
Simulated SDR / SIR / SAR 8.93 / 13.57 / 11.35 dB 
Raw vs SI-HSM pitch MAE 5.24 vs 3.89 cents 
4.2.8. Hyperparameter Sensitivity and Clustered Uncertainty 
Sections 4.2.8–4.2.11 report supplementary analyses that probe hyperparameter robustness 
(ß4.2.8), engineering coverage (ß4.2.9), heuristic-classifier validity (ß4.2.10), and a comparison 
against open-source separation baselines (ß4.2.11). These analyses do not introduce new claims; 
they support the main results above. To make the stable-segment calibration logic more explicit, 
three different window settings were used on the same 36 recordings for a sensitivity analysis. A 
15%-85% wide window achieved pitch r = 0.911, pitch MAE = 3.18, and note F1 = 0.691; a 
20%-82% wide window achieved pitch r = 0.929, pitch MAE = 2.67, and note F1 = 0.705; and a 
narrower 25%-80% wide window achieved pitch r = 0.917, pitch MAE = 2.98, and note F1 = 
0.687. Therefore, the selected window is retained as the operating point because the wider 
window has more attack/release frames and the narrower window reduces recall for short notes. 
Window settings and corresponding metrics are summarised in Table 12. Participant-cluster 
bootstrap resampling (B = 2000) produced the 95% CIs reported in Table 13: path agreement 
[0.611, 0.917], note-level F1 [0.647, 0.762], measure-level F1 [0.716, 0.812], recording-level 
pitch r [0.661, 0.909], and recording-level rhythm r [0.395, 0.859]. 
Table 12. Sensitivity Analysis of the Stable-Segment Window Parameter. 
Window Pitch r Pitch MAE Note P Note R Note F1 Interpretation 
15%-85% 0.911 3.18 0.714 0.696 0.691 
wider window 
keeps 
attack/release 
frames 
20%-82% 0.929 2.67 0.731 0.68 0.705 
selected 
operating point 
25%-80% 0.917 2.98 0.739 0.642 0.687 
narrower 
window drops 
valid short-
note frames 
Table 13. Participant-cluster bootstrap uncertainty estimates. 
Metric Point estimate Participant-cluster 95% CI B 
Path agreement 0.778 [0.611, 0.917] 2000 
Note-level F1 0.705 [0.647, 0.762] 2000 
Measure-level F1 0.763 [0.716, 0.812] 2000 
Recording-level pitch r 0.818 [0.661, 0.909] 2000 
Recording-level rhythm r 0.664 [0.395, 0.859] 2000 
 
 

Page 24 
 
4.2.9. OMR Import and Whole-piece Engineering Verification 
The score-import and whole-piece modules have been verified according to the project 
engineering log. The import log shows that out of the 301 completed score-import jobs, 246 are 
in pagewise OMR mode and 48 are in score-store/library mode; the overall success rate is 95.0% 
(286/301). The whole-piece project export for the Taohuawu test fragment reports the complete 
section and note coverage, and at the same time, the concurrent module aggregates the segment 
results into a piece-level practice-priority summary. The above checks examine the system&#39;s 
operability and scope, not learner outcome effects. Table 14 summarises the OMR-import and 
whole-piece engineering verification logs. 
Table 14. OMR Import and whole-piece engineering verification based on project logs. 
Item n Successful / covered Rate or speedup Source note 
OMR/import jobs in 
project log 
301 286 95.0% 
pagewise=246; score-
store/library=48 
Unknown-PDF 
OMR stress samples 
3 3 100.0% 
completed=3; 
failed=0 
Whole-piece section 
coverage 
41 41 100.0% 
Taohuawu test 
fragment 
Whole-piece note 
coverage 
328 328 100.0% 
dominant 
path=rhythm-first 
Concurrent analysis 
timing 
41 41 17.6x 
serial about 300 s vs 
concurrent about 17 
s; value is speedup 
 
4.2.10. Heuristic Technique Classifier Validation 
This section validates the heuristic technique classifier (Section 3.5) on the same 36 
recordings. Two independent experts blind-annotated all stable-segments using a seven-category 
scheme (vibrato, portamento, trill, harmonic, pizzicato, col legno, none); recordings, segments, 
and system predictions are inherited from the main experiment. Two experts produced 282 
paired annotations (mean 7.83 per recording, range 4–12, SD 2.08); max segment duration 1.98 
s. 
Inter-rater agreement between the two experts was Cohen&#39;s κ = 0.822 (95% bootstrap CI 
[0.771, 0.871], B = 2000), exceeding the prespecified κ ≥ 0.60 threshold for substantial 
agreement. To produce a conservative ground truth, only segments where both experts assigned 
the same label were retained, yielding 242 consensus segments; the 40 disagreement segments 

Page 25 
(14.2% of 282) concentrated on the boundary between expressive techniques and the residual 
none category—of the 40 disagreement events, 24 (60%) involved the none label paired with 
vibrato (n=8), portamento (n=5), col legno (n=4), or harmonic (n=4); the remaining 
disagreements were technique-vs-technique confusions such as col legno/pizzicato (n=4) and col 
legno/harmonic (n=4), consistent with their acoustic proximity. The 242 retained consensus 
segments form a conservative ground truth that may slightly overestimate per-class F1 for 
boundary-ambiguous categories. Every category had at least 15 ground-truth instances (range 15 
for pizzicato to 85 for none). 
The heuristic classifier&#39;s overall macro-F1 score on the consensus ground truth was 0.660. 
Per-class performance is reported in Table 15 and the full 7◊7 confusion matrix in Table 16. 
Table 15. Per-class Precision, Recall and F1 of the heuristic technique classifier against expert-
consensus ground truth (n = 242 segments). 
Label Precision Recall F1 n 
vibrato 0.732 0.854 0.788 48 
none 0.776 0.776 0.776 85 
portamento 0.733 0.688 0.710 32 
harmonic 0.800 0.615 0.696 26 
col legno 0.688 0.579 0.629 19 
trill 0.615 0.471 0.533 17 
pizzicato 0.409 0.600 0.486 15 
macro avg 0.679 0.655 0.660 242 
Table 16. Confusion matrix of the heuristic technique classifier against expert-consensus ground truth 
(n = 242 segments). Rows: ground-truth label; columns: system-predicted label; diagonal is correct. 
GT \ Sys vibrato portamento trill harmonic pizzicato col legno none 
vibrato 41 0 3 0 0 0 4 
portamento 4 22 2 0 0 0 4 
trill 4 2 8 0 0 0 3 
harmonic 0 0 0 16 4 4 2 
pizzicato 0 0 0 2 9 1 3 
col legno 0 0 0 1 4 11 3 
none 7 6 0 1 5 0 66 
The classifier performs best on vibrato and none (both F1 &gt; 0.77), consistent with the rule-
based design that targets sustained periodic frequency modulation (vibrato) and treats the 
residual category as default. The weakest categories are pizzicato (F1 = 0.486) and trill (F1 = 
0.533). The confusion matrix reveals that pizzicato is most often misclassified as harmonic or 
none, and 5 of 17 trill instances are mistaken for vibrato—both error patterns reflect the acoustic 
proximity of these techniques (transient bow-attack envelopes for pizzicato; periodic but lower-
amplitude pitch fluctuations for trill). These limitations motivate future work on data-driven 

Page 26 
technique classification. The none class accounts for 35.1% of consensus GT (85/242); the 
averaging scheme affects the headline metric: macro-F1 = 0.660 (all 7 classes), weighted-F1 = 
0.715 (weighted by support), and macro-F1 = 0.678 over the 6 technique classes excluding none. 
The macro-F1 ceiling is bounded by weaker technique classes (pizzicato, trill) rather than by 
none-class dominance. We report macro-F1 as the primary, more conservative metric. 
 
4.2.11. SI-HSM Source Separation Baseline Comparison 
This section extends the SI-HSM evaluation reported in Section 4.2.7 by adding two open-
source separation baselines—Demucs v4 (htdemucs, --two-stems=vocals) and Hybrid 
Transformer Demucs (htdemucs_ft)—on the same 36 recordings, using the same reference 
waveforms and pitch ground-truth as the original analysis. This is a within-subject 
methodological comparison, not an independent experiment. 
All baseline outputs were resampled to 16 kHz mono and processed by the same museval-
based SDR/SIR/SAR pipeline and torchcrepe pitch script used for SI-HSM in Section 4.2.7. The 
SI-HSM row in Table 17 reproduces Table 11 exactly; the raw audio row also matches Table 11 
(5.24 cents pitch MAE), confirming pipeline consistency before cross-method comparison. 
Table 17. Source separation baseline comparison on the same 36 recordings (mean ± SD). 
Method SDR (dB) SIR (dB) SAR (dB) pitch MAE (cents) 
raw audio 5.62 ± 1.02 9.18 ± 1.83 8.04 ± 0.67 5.24 ± 0.46 
SI-HSM 8.93 ± 0.57 13.57 ± 1.28 11.35 ± 0.61 3.89 ± 0.32 
Demucs v4 7.38 ± 0.65 11.05 ± 1.18 9.72 ± 0.86 4.57 ± 0.55 
HT-Demucs 7.82 ± 0.62 11.64 ± 1.08 10.18 ± 0.79 4.33 ± 0.67 
SI-HSM achieves the highest SDR, SIR, SAR and the lowest pitch MAE across all four 
methods, consistent with the design rationale that the score-informed harmonic mask leverages 
prior knowledge unavailable to general-purpose separators. Paired Wilcoxon signed-rank tests on 
pitch MAE (n = 36) confirm the advantage, with median differences and p-values reported in 
Table 18. 
Table 18. Paired Wilcoxon signed-rank tests of SI-HSM vs each comparator on pitch MAE (lower is 
better; positive median Δ favours SI-HSM). 
Comparison Median Δ (cents) p 
SI-HSM vs raw audio +1.28 &lt; 0.001 
SI-HSM vs Demucs v4 +0.74 &lt; 0.001 
SI-HSM vs HT-Demucs +0.46 &lt; 0.001 

Page 27 
The smaller—though still statistically significant—gap against HT-Demucs (median 0.46 
cents) suggests that more recent neural source separators are partially closing the gap on this 
erhu-specific task while still trailing SI-HSM. These results support the methodological choice to 
retain SI-HSM rather than replace it with an off-the-shelf neural separator. This section evaluates 
separation quality only; whether HT-Demucs could substitute SI-HSM in the downstream 
pipeline (Table 10 ablation columns: pitch r, rhythm r, note F1, measure F1) is an open empirical 
question for future work. 
4.3. Usability Study 
4.3.1. Questionnaire Results 
All 18 participants filled in and submitted a 5-item Likert scale questionnaire (1 = strongly 
disagree, 5 = strongly agree). Good reliability of the questionnaire (Cronbach&#39;s α = 0.92). Table 
19 shows the mean, standard deviation, 95% confidence interval, one-sample t-test and effect 
size of the items; t(17), p and Cohen&#39;s d for each of the 5 items are listed in the table. All five 
items were higher than the neutral midpoint (M range: 3.56–4.28; all p &lt; 0.01), and two items 
(feedback clarity and confidence improvement) were slightly above the criterion (M = 3.56, d ≈ 
0.79–0.90). To control family-wise error across the five Likert comparisons, Holm-Bonferroni 
correction was applied: the threshold for the smallest unadjusted p-value is α/5 = 0.01 at family-
wise α = 0.05, and since all five unadjusted p-values were below this threshold, all items 
remained significant after correction (all adjusted p &lt; .05). The range of the lowest and highest 
item means was 0.72, and there were no uniformly ceiling-level responses. Feedback clarity was 
relatively low, and some of the open-ended feedback from participants indicated that the wording 
of the feedback could be improved further. 
Table 19. Results of the Usability Questionnaire (n=18, 5-point Likert scale). 
Item Dimension Mean SD 95% CI t(17) p Cohen&#39;s d 
UX1 
Perceived 
usefulness 
4.28 0.67 [3.95, 4.61] 8.10 &lt; .001 1.91 
UX2 Ease of use 3.83 0.62 [3.53, 4.14] 5.72 &lt; .001 1.35 
UX3 Feedback clarity 3.56 0.62 [3.25, 3.86] 3.83 .001 0.90 
UX4 
Learning 
confidence 
3.56 0.70 [3.21, 3.91] 3.34 .004 0.79 
UX5 
Continuance 
intention 
3.94 0.87 [3.51, 4.38] 4.59 &lt; .001 1.08 

Page 28 
4.3.2. Qualitative Feedback 
Participants were generally positive in open-ended feedback. Examples: &quot;It is convenient to 
find problem notes without having to listen to the whole recording multiple times&quot; and &quot;It is easy 
to see which note was raised.&quot; A few suggested adjusting the feedback tone (&quot;the prompts could 
be more casual&quot;). These responses align with the quantitative questionnaire and will inform the 
next-generation system. 
4.4. Case Analysis 
Beyond the aggregate accuracy and usability results, two recorded cases illustrate how the 
system&#39;s diagnostic output translates into targeted practice actions during a re-recording cycle. 
The two cases below illustrate the feedback-practice-re-recording workflow for an intonation-
dominated and a rhythm-dominated case. They show how the system converts diagnostic results 
into practical practice actions but do not provide causal evidence of learning gains under 
controlled conditions. 
Case A (intonation-dominant): Participant P14 performed the opening-theme of &#39;Taohuawu&#39; 
(8.3 s, 4 notes). System intonation score 71 (expert mean 74), rhythm score 83 (expert mean 
81)—within the study&#39;s MAE range. The system localised the second note of measure 3 (D5, 
expected 587.3 Hz), with mean stable-segment deviation −18.6 cents (SD 4.9), a systematic flat-
type deviation caused by insufficient finger-pressure depth. The note was marked high-priority 
(red highlight) and pitch-first practice was recommended. After three targeted slow-practice 
sessions, the participant re-recorded: intonation rose to 84 (+13), the note&#39;s stable-segment 
deviation dropped to −5.3 cents, and experts confirmed improvement (E1 = 84, E2 = 86). Figure 
10 visualises score localisation, the practice path, and error convergence. 
 
Case B (rhythm-dominated): Participant P07 performed the post-introduction entry (9.1 s, 8 
notes). System rhythm score 60 (expert mean 61), intonation 64 (expert mean 60). Four 

Page 29 
consecutive notes in measure 2 were rushed (mean +54 ms, SD 12); two notes in measure 4 were 
also rushed; one note in measure 7 approached but did not exceed threshold. The system flagged 
three problems and recommended a rhythm-first path with a reference demonstration. After 
slow-follow practice (60% speed, gradually increasing), the participant re-recorded: rhythm 
score rose to 76 (+16), measure-2 onset deviation dropped to M = +14 ms (SD 8), and problem 
measures dropped from 3 to 1. Both cases illustrate workflow rather than learning gain, since no 
no-feedback control condition was used. 
4.5. Functional Dimension Comparison with Existing Tools 
Table 20 is a table of functional coverage for this system and other representative tools. This 
comparison is a qualitative feature audit rather than a performance benchmark under uniform 
conditions; its purpose is to show that this system has integrated the three capabilities of PDF 
score import, erhu technique fault-tolerant scoring, and score-coordinate feedback into a single 
self-practice workflow. 
Table 20. Functional Comparison of the Proposed System and Existing Tools. 
Functional dimension This system Yousician SmartMusic 
Target instrument 
Erhu (non-Western 
bowed) 
Western instruments 
(primary) 
Western instruments 
(various) 
PDF score import Supported Not supported Not supported 
Pitch assessment 
algorithm 
torchcrepe (open-
source) 
Undisclosed Undisclosed 
Rhythm assessment Supported Supported Limited 
Technique tolerance (6 
types) 
Supported Not supported Not supported 
Note-level problem 
localization 
Supported Limited Not supported 
Score-coordinate 
annotation 
Supported Not supported Not supported 
End-to-end pipeline Supported Supported Supported 
Therefore, Table 20 should be seen as a comparison of scopes rather than an assertion that 
this system is superior to other products in all aspects. 
5. Discussion 
The stable-segment algorithm and technique-tolerance layer form the main design choice 
distinguishing this system from general-purpose pitch pipelines. Generic deep-learning models 
output a frame-level pitch sequence and frequently misclassify vibrato&#39;s periodic fluctuation as 
intonation deviation or fragment a single portamento gesture into multiple false problem notes. 
The Section 4.2.7 ablation made the cost tangible: removing stable-segment trimming, technique 

Page 30 
tolerance, or SI-HSM each reduced agreement and localisation metrics, confirming all three 
components are additive. 
The score-coordinate feedback interface is a second key design choice. As Table 20 shows, 
none of the surveyed tools combines PDF score import, fault-tolerant erhu-technique scoring, 
and original-score problem localisation. The proposed system projects DTW-aligned errors back 
onto score coordinates and highlights the problem area directly on the score image, moving from 
general performance evaluation to specific error localisation. The usability questionnaire and 
open-ended comments converge on the same conclusion: this design reduces the cognitive load 
required to translate feedback into corrections. 
The system offers a clean transfer path to other fretless bowed string instruments. The SI-
HSM harmonic masking mechanism is guided by the score pitch prior rather than any 
instrument-specific timbre template, making it generally applicable to related instruments such as 
the banhu and erxian. The stable-segment proportion (20%–82%), the technique-detection 
thresholds (e.g., vibrato full range of 26 cents and portamento derivative of 1.0 cents/ms), and 
the DTW cost weights (onset 12, duration 8, low confidence 6) were all empirically optimised 
for the erhu. Transfer to another instrument requires recalibrating these numbers, but the 
surrounding pipeline and the MusicXML schema remain unchanged. 
Several limitations of this research are noted below. First, the empirical evidence was based 
on a single conservatory, a single work (Taohuawu), and two segments per participant; thus, the 
results could only be regarded as a pilot validation and not as a general-population claim. 
Second, the system has not been tested on other erhu repertoires, other institutions, or learner 
groups outside the present sample, and has therefore not been examined for beginners or 
advanced students. Third, the practice-path recommendation logic was adjusted according to the 
specific scoring rubric and weightings of this study; instructors who gave different importance to 
pitch, rhythm, or a review-first approach would likely need to recalibrate. Fourth, torchcrepe was 
trained on general music data, and its confidence output is less reliable in the high register and 
during rapid vibrato—two situations of particular demand for the erhu. Fifth, the assessment 
dimensions are restricted to intonation and rhythm; tonal quality and bow continuity remain 
relevant to expert judgment but have not yet been incorporated. Sixth, the 36 recordings were 
derived from 18 participants who each provided two segments, so segment-level estimates are 

Page 31 
not independent observations, and participant-cluster bootstrap intervals were reported 
accordingly (Section 4.2.8). Case A and Case B (Section 4.4) illustrate the re-practice workflow 
but do not serve as controlled learning-gain experiments. 
6. Conclusion 
This paper fills the gap in existing automatic performance assessment systems—which focus 
on Western instruments—by presenting what is, to our knowledge, the first end-to-end AI-
assisted self-practice system for the erhu. The system imports user-uploaded PDF scores, 
provides fault-tolerant scoring of bowed-string techniques, and delivers feedback at specific 
score coordinates. Existing commercial tools, designed for Western instruments, neither accept 
user scores nor model erhu techniques such as vibrato, portamento, or harmonics, and therefore 
cannot give precise score-surface feedback to erhu learners. 
The Six Modules of the Pipeline. The Audiveris-based score-import module parses PDF 
scores into structured note sequences. The SI-HSM preprocessing module uses the score pitch 
prior to drive harmonic masking and suppress accompaniment bleed-through. torchcrepe and 
madmom are combined in the analysis module to perform pitch tracking and onset detection, and 
DTW is then used to align the performance with the score. The erhu domain adaptation layer 
uses stable-segment trimming and technique-recognition tolerance to suppress most false 
positives. The structured feedback module maps the error sequence to score coordinates and 
displays per-note problems with a colour-gradient highlighting scheme. Finally, the entire-piece 
concurrent analysis module (Section 3.7) assesses all parts of a piece simultaneously and 
generates a high-level practice-priority summary. Throughout the evaluation, the system&#39;s scores 
for intonation and rhythm correlated with expert assessments at r = 0.93 and r = 0.83, 
respectively; the F1 score of problem-note recognition reached 0.705, and every item on the 
usability questionnaire was significantly higher than the neutral midpoint (all p &lt; .01). 
As deep-learning audio analysis and the digital foundation of non-Western music continue to 
develop, AI-assisted practice tools become increasingly viable for non-Western music education. 
The system reported here provides end-to-end technical support for subsequent research and 
offers teachers and scholars a practical path for applying modern AI technology to traditional 
music education. 

Page 32 
Data availability 
The datasets generated and/or analysed during the current study are not publicly available 
because they include student performance recordings and educational evaluation records, but de-
identified data supporting the findings are available from the corresponding author upon 
reasonable request and subject to applicable ethical and institutional approvals. 
References 
1. de Cheveigne, A. &amp; Kawahara, H. YIN, a fundamental frequency estimator 
for speech and music. J. Acoust. Soc. Am. 111, 1917-1930, 
https://doi.org/10.1121/1.1458024 (2002). 
2. Mauch, M. &amp; Dixon, S. pYIN: a fundamental frequency estimator using probabilistic 
threshold distributions. in 2014 IEEE International Conference on Acoustics, Speech and 
Signal Processing (ICASSP) 659-663, https://doi.org/10.1109/ICASSP.2014.6853678 
(2014). 
3. Kim, J. W., Salamon, J., Li, P. &amp; Bello, J. P. CREPE: a convolutional representation for pitch 
estimation. in 2018 IEEE International Conference on Acoustics, Speech and Signal 
Processing (ICASSP) 161-165, https://doi.org/10.1109/ICASSP.2018.8461329 (2018). 
4. Bock, S., Korzeniowski, F., Schluter, J., Krebs, F. &amp; Widmer, G. madmom: a new Python 
audio and music signal processing library. in Proceedings of the 24th ACM International 
Conference on Multimedia 1174-1178, https://doi.org/10.1145/2964284.2973795 (2016). 
5. Muller, M. Fundamentals of Music Processing: Audio, Analysis, Algorithms, Applications 
(Springer, 2015). 
6. Foscarin, F., McLeod, A., Rigaux, P., Jacquemard, F. &amp; Sakai, M. ASAP: a dataset of aligned 
scores and performances for piano transcription. in Proceedings of the 21st International 
Society for Music Information Retrieval Conference 534-541 (2020). 
7. Benetos, E., Dixon, S., Duan, Z. &amp; Ewert, S. Automatic music transcription: an overview. 
IEEE Signal Process. Mag. 36, 20-30, https://doi.org/10.1109/MSP.2018.2869928 (2019). 

Page 33 
8. Calvo-Zaragoza, J., Hajic, J. Jr. &amp; Pacha, A. Understanding optical music 
recognition. ACM Comput. Surv. 53, 77, https://doi.org/10.1145/3397499 
(2020). 
9. Yang, L., Rajab, K. Z. &amp; Chew, E. Vibrato performance style: a case study comparing erhu 
and violin. in Proceedings of the 10th International Symposium on Computer Music 
Multidisciplinary Research 340-356 (2013). 
10. Dalmazzo, D. &amp; Ramirez, R. Bowing gestures classification in violin performance: a 
machine learning approach. Front. Psychol. 10, 344, 
https://doi.org/10.3389/fpsyg.2019.00344 (2019). 
11. Yousician. Yousician: learn to play and master your instrument. 
https://yousician.com (2024). 
12. MakeMusic. SmartMusic: music education technology. 
https://www.smartmusic.com (2024). 
13. Defossez, A. Hybrid spectrogram and waveform source separation. in Proceedings of the 
ISMIR 2021 Workshop on Music Source Separation. Preprint at 
https://arxiv.org/abs/2111.03600 (2021). 
14. Peter, S. D. et al. Automatic note-level score-to-performance alignments in the ASAP 
dataset. Trans. Int. Soc. Music Inf. Retr. 6, 27-42, https://doi.org/10.5334/tismir.149 (2023). 
15. Rouard, S., Massa, F. &amp; Defossez, A. Hybrid transformers for music source separation. in 
IEEE International Conference on Acoustics, Speech and Signal Processing 1-5. Preprint at 
https://arxiv.org/abs/2211.08553 (2023). 
16. Wrigley, W. J. &amp; Emmerson, S. B. Ecological development and validation of a music 
performance rating scale for five instrument families. Psychol. Music 41, 97-118, 
https://doi.org/10.1177/0305735611418552 (2013). 
17. Koo, T. K. &amp; Li, M. Y. A guideline of selecting and reporting intraclass correlation 
coefficients for reliability research. J. Chiropr. Med. 15, 155-163, 
https://doi.org/10.1016/j.jcm.2016.02.012 (2016). 
 

Page 34 
 
 
 
 
 
 
 
 
 
 
 
 
Acknowledgements 
The authors would like to express their sincere gratitude to the faculty and the erhu major 
students from the Folk Music Department at the Sichuan Conservatory of Music for their 
valuable participation, recording contributions, and support during the empirical validation phase 
of this study. We also thank the professional experts who provided blind evaluation benchmarks 
for the performance dataset. 
Author contributions 
X.G. led system implementation, data analysis and manuscript drafting. H.S., M.F. and Z.J. 
contributed to study design, technical review and manuscript revision. J.Z. supervised the 
project, coordinated validation and reviewed the manuscript. All authors reviewed and approved 
the final manuscript. 

Page 35 
Funding 
The authors received no financial support for the research. 
Competing interests 
The authors declare no competing interests. 
Figure legends 
Figure 1 | Three-layer System Architecture and End-to-end Data Flow. React PWA collects 
score and audio data; the Node.js gateway handles routing and analysis tasks, and then the 
Python FastAPI service returns score-aligned diagnostic artifacts to the feedback interface. 
Figure 2 | Score-import workflow for PDF to structured JSON notes. The pipeline attempts 
Audiveris OMR first, converts MusicXML into the internal note schema, and falls back to 
the verified phrase library if the OMR output is incomplete or has a low confidence level. 
Figure 3 | SI-HSM Pipeline for Waveform Input to Erhu-Enhanced Output. Score-guided 
pitch priors restrict harmonic masking, and a confidence check avoids damage to the 
following analysis of pitch and rhythm caused by low-quality masks. 
Figure 4 | Spectral Comparison of the Original Mixture, Harmonic-Mask Proxy, and 
Separated Erhu Signal. As shown in the figure, the score-driven mask has strengthened the 
harmonic progression of the erhu and reduced the intensity of the accompaniment section. 
Figure 5 | DTW Alignment of Performed Onsets and Score-Expected Onsets. The 
alignment path maps detected performance events to structured score notes, and 
subsequently, pitch/rhythm errors can inherit measure and note coordinates. 
Figure 6 | Stable-segment Definition for Pitch Evaluation. Pitch scoring only uses the 20%–
82% stable interval and excludes the attack and release regions where bow acceleration, 
deceleration and position changes can cause transient pitch artifacts. 
Figure 7 | Score-aligned feedback interface with note highlighting and practice-path 
recommendation. The interface connects the diagnostic score, recommended path, target 
measure/note and error details to guide learners to focus their re-recording activities based 
on the assessment. 

Page 36 
Figure 8 | Whole-piece concurrent analysis workflow. Scan the entire-piece recording for 
score-segment coverage, distribute the segments to parallel workers, and compile a piece-
level summary of weak sections and practice priorities. 
Figure 9 | System-Expert Agreement Scatterplots for Pitch and Rhythm. Each point is the 
aggregated score of a participant, and the fitted trend line shows how the system scores 
compare to the mean benchmark of experts. 
Figure 10 | Two Re-recording Cases After Targeted Training. 

Supplementary Files
This is a list of supplementary files associated with this preprint. Click to download.
Fig10.png
Fig6.png
Fig4.png
Fig5.png
Fig7.png
Fig8.png
Fig9.png
Fig3.png
Fig2.png
Fig1.png