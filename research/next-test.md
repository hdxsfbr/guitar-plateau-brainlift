# Next test: an 8-week pilot of both POVs

**Headline:** an 8-week pilot with 12–16 plateaued intermediate guitarists aged 18 or over. Each learner's practice items are randomly split two ways: *ear-gated vs conventionally drilled* (POV A) and *feedback after every take with self-estimate first vs faded feedback* (POV B). Outcomes are no-feedback retention, transfer and blind-rated improvisation at week 8. Rater and AI reliability are checked before any score is trusted.

This is a feasibility and effect-size pilot, not a confirmatory trial. It tells us whether a bigger study is worth running, which parts of each POV to drop, and whether the measurements can be trusted.

## Who
- **n = 12 completers** (recruit 16, allowing for about 25% dropout).
- **Eligibility:**
  - **18 or over (pilot choice).** Teens are in the target group, but including 13–17-year-olds means parental consent, assent and safeguarding procedures. That is too heavy for a 16-person pilot. If the pilot works, a follow-up should add a teen arm with parental consent.
  - Self-taught or lesson-taught; teaching history is recorded.
  - At least 3 years playing.
  - Can play the major and minor pentatonic in at least 2 positions and basic open and barre chords; a teacher confirms intermediate level from the baseline video.
  - **Plateau screen:** self-reports no clear progress for 2 years or more despite continued practice (a multi-year plateau), and names what they are stuck on.
  - **Determination:** commits to at least 30–45 min/day, 6 days a week, for 8 weeks, and records on a phone.
- **Practice time varies:** Andre, the motivating user, does about 2 h/day; most recruits will do less. Practice minutes are logged and analysed as a covariate.

## Design (within-learner, item-level, 2 × 2)
- **Items.** Each learner gets 8 practice items, matched for difficulty by a teacher before randomisation: short licks or phrases, chord-quality sets (for example maj7 / dom7 / m7) and progressions. Items are randomly assigned, 2 per cell, to:

  | | **Feedback after every take, self-estimate first** (POV B) | **Faded feedback** (conventional: every 3rd take, then every 5th; no self-estimate) |
  |---|---|---|
  | **Ear-gated** (POV A) | 2 items | 2 items |
  | **Conventional drill** (name, look up the shape, drill with metronome) | 2 items | 2 items |

- **Ear-gated items** follow `povs.md` v3:
  - Allowed before the gate: label, compare, hum/sing-while-playing, slow mapping in positions, slow improvisation.
  - Tempo ladders and high-volume repetition open only after a by-ear check (4 of 5 in-context examples played or hummed back) passed on 2 separate days.
- **Feedback** comes from post-take analysis of the phone recording (Basic Pitch transcription plus onset timing). There is never a live display. Metronome and backing tracks are allowed. A take is one full run-through.
- **Why within-learner:** with n = 12, between-person comparisons would be hopeless. Item-level randomisation gives each learner their own control.
  - Known risk: self-estimation and ear habits may carry over to other items. That biases results *toward no difference*, so a positive result is more convincing than a null.
  - The B comparison changes two things at once (frequency and self-estimate). This is pragmatic: it tests the POV as written against the conventional advice. It does not isolate either component.

## Timeline
| Week | What happens |
|---|---|
| 0 | Screen (POV A diagnosis): (1a) same/different + hum-back of 2-bar melodies over a drone; (1b) the same on guitar; (2) rhythm play-back; (3) technique/speed check. Baseline recordings of all 8 items plus a 2-minute improvisation over a backing track. Baseline video for the teacher diagnosis task. |
| 1–6 | Daily practice on the items through the prototype tutor or a scripted protocol (a phone app and a sheet are enough). Log minutes, takes, gate attempts, self-estimates and time spent reviewing feedback. One teacher check-in by video per week (identical across conditions). |
| 7 | No-feedback retention: each item at target tempo. Transfer: each item in a new key, and chord-quality items identified in an unfamiliar song. Improvisation over a new backing track, using the items. |
| 8 | Delayed retention (1 week after week 7, with no practice of the items in between): repeat of the week-7 tests. |

## Measures
**Learning outcomes (per item, weeks 7–8, no feedback)**
1. At-tempo accuracy: machine onset and pitch error, plus panel rating.
2. By-ear transfer: playing in a new key, and identifying in context.
3. Use in improvisation: blind panel rating of how well the item's sound is used.

**Diagnosis and process**
- **Screen profile.** For each learner, is the weakest link hearing (1a/2), fretboard mapping (1b weak but 1a fine), or technique (3)? This gives the first base-rate data for the POV A bet.
- **Gate telemetry:** time-to-pass by item type, and the number of failed attempts.
- **Self-estimate accuracy over weeks:** agreement between learner-marked errors and machine-flagged errors on reliable dimensions.
- **Adherence:** practice minutes, the share of takes recorded and self-estimated, review time as a percentage of practice, dropout, and a short weekly frustration rating (1–5).

**Reliability. No score is trusted until it passes these checks.**
- **Human panel.** Three guitar teachers rate blind (condition and week hidden, order randomised) all week-0/7/8 takes on 3 dimensions: accuracy, time feel, musical use.
  - Report ICC(2,k) by dimension. Bergee's work suggests that panels of 2–3 judges are unstable (E016), so panel averages are used, never single raters.
  - A dimension with an average-measure ICC below .60 is dropped from the outcomes.
- **Machine vs humans.** On 50 takes hand-annotated by one teacher and checked by a second, measure:
  - onset and pitch error detection precision and recall;
  - correlation of machine timing and pitch scores with the panel;
  - the share of sections marked "couldn't assess".
- **Teacher diagnosis agreement (fills a gap in the evidence base).** Each teacher independently names each learner's top limiting factor from the baseline video. Report Fleiss' κ, and the share of named factors that fall within machine-measurable dimensions. This is the streetlight check.

## Success and kill criteria (fixed before data collection)
The analysis is a mixed model with items nested in learners. With n = 12 these are decision rules for go / revise / stop, not significance tests.

**Measurement gates (checked first)**
- **Per-take machine scoring.**
  - Keep a dimension if machine–panel r ≥ .70 and error-detection precision ≥ .60 on home recordings.
  - Otherwise turn off per-take scoring for that dimension. POV B then falls back to self-estimate plus weekly human review.
- **Streetlight check.**
  - If fewer than 50% of teacher-named top limits fall within machine-measurable dimensions, the "one priority" slot must be mainly human or self-review in the next version.
  - If teacher κ is below .40, "bottleneck diagnosis" is treated as unreliable even for humans, and the tutor's screen must stay probe-based.

**POV A**
- **Go:** at week 8, ear-gated items beat conventional items on by-ear transfer and improvisation use by at least 0.3 SD (pooled item-score SD), or at least 9 of 12 learners favour gated items. In addition:
  - at-tempo accuracy on gated items is no more than 5 percentage points worse;
  - at least 75% of gated items pass the gate by week 3.
- **Revise the gate:** transfer improves but more than 25% of gated items stall at the gate past week 3, or weekly frustration averages 4 or higher. Loosen the gate (for example, one day instead of two, or hum-back only).
- **Kill the gate:** gated items are no better on transfer and worse on at-tempo accuracy at week 8. Ear-*coupled* practice is kept, but not as a gate.
- **Kill the "more often a hearing problem" bet:** fewer than a third of screened learners have hearing (1a or 2) as their weakest link. The claim then becomes "ear-couple your drilling" without the diagnosis.

**POV B**
- **Go:** at week 8, items with feedback after every take and self-estimate first are at least as good as faded-feedback items on no-feedback retention and transfer (difference above −0.1 SD). In addition:
  - self-estimate agreement improves from weeks 1–2 to weeks 5–6;
  - review time is at most 15% of practice time;
  - at least 80% of full takes get a self-estimate.
- **Kill / revert to faded feedback:** every-take items are worse at no-feedback retention by 0.3 SD or more, *or* self-estimate accuracy is flat or declining (the dependency signal), *or* fewer than 60% of takes are completed with self-estimates by week 4 (adherence failure).

## What it costs and what it won't tell us
- **Cost:** a phone per learner; Basic Pitch or a similar tool; about 12 hours of rating per teacher (3 teachers); and about 1 hour per learner per week of researcher support.
- **Limits:**
  - Too small for subgroup claims.
  - Item effects are short-term (6 weeks of practice, 1-week delayed retention), so it cannot speak to the two-year plateau.
  - Carry-over biases both POVs toward a null.
  - Learners know their own conditions, so only the raters are blind.
