# POV pressure tests

**Prompt (exact assignment wording; the POV text is substituted for `[insert POV]`):**

> Evaluate this education POV: [insert POV]. Where is it weak or unlikely to work? Identify the strongest objection, the specific constraint behind it, and the evidence needed to resolve it. Give an honest assessment; do not agree or disagree just because I asked.

**Scope note (2026-10-08).** These runs used the earlier learner context ("adult intermediate guitarists who practise about 2 hours a day for 2 years"). The learner group has since been broadened to intermediate guitarists of any age on a multi-year plateau. The strongest objections (hearing and playing co-develop; the gate conflates hearing with fretboard mapping; outsourced self-evaluation; the streetlight problem) do not depend on age or practice hours. Points about two-year adherence and adult dropout apply to the motivating user and may differ for teens. The raw outputs are left unchanged as a historical record.

**How it was run**
- Script: `scripts/pressure-test.py`, via OpenRouter on hdx-lab. The key was read from `~/.config/agentforge/openrouter_api_key` at run time and never printed or saved. Settings: one user message, `max_tokens` 8000, default temperature.
- The POV text inserted for each run is in `research/pressure-tests/inputs/`. The raw output for each run is saved verbatim in `research/pressure-tests/`: `.md` holds the prompt and response, `.json` the full API response including usage.
- Dates: 2026-10-08, 12:15–12:19 AM CT. The file headers show lab-local PDT (Oct 7, 10:15–10:19 PM).

| Run | POV version | Model (exact slug) | Tokens in/out | Cost (USD, OpenRouter usage) |
|---|---|---|---|---|
| `povA-v1-anthropic_claude-opus-5.5` | A v1 (Andre's wording) | `anthropic/claude-opus-5.5` | 320 / 3,782 | 0.0769 |
| `povA-v1-openai_gpt-5.5` | A v1 | `openai/gpt-5.5` (contrast) | 200 / 3,113 | 0.0944 |
| `povB-v1-anthropic_claude-opus-5.5` | B v1 (Andre's wording) | `anthropic/claude-opus-5.5` | 286 / 4,479 | 0.0907 |
| `povB-v1-openai_gpt-5.5` | B v1 | `openai/gpt-5.5` (contrast) | 175 / 3,250 | 0.0984 |
| `povA-v2-anthropic_claude-opus-5.5` | A v2 (after round-1 revision) | `anthropic/claude-opus-5.5` | 422 / 3,958 | 0.0808 |
| `povB-v2-anthropic_claude-opus-5.5` | B v2 (after round-1 revision) | `anthropic/claude-opus-5.5` | 346 / 4,366 | 0.0887 |
| **Total** | | | | **≈ $0.53** |

**Handling model claims.** Model outputs are critiques, not evidence.
- **Verified and added.** Three studies the models cited were checked against their Europe PMC abstracts before use, then added to the register and evidence table: Lahav et al. 2007 (E095), Lappe et al. 2008 (E096) and Guadagnoli & Kohl 2001 (E097).
- **Misstatements, not relied on:**
  - Claude (B v1) said that after bias correction the McKay 2022 *feedback-frequency* meta-analysis shrinks toward zero. That shrinkage result belongs to McKay's *self-controlled practice* meta-analysis (E028). The frequency meta-analysis simply found no effect (E026).
  - Claude (B v1) said real-time visual feedback "degrades retention once it's removed". In the only music RCT we have (E032), the feedback group's sound was *better* in the same-session no-feedback phase.
  - Other cited works were not verified and are not used: the challenge-point framework (Guadagnoli & Lee 2004), Suzuki and Gordon as general precedent.

---

## POV A — Hear it before you drill it

### Round 1 (v1, Andre's wording; both models)
- **Strongest objection (both models agreed):** hearing and playing develop *together*. A strict "no drilling until you can hear it" gate cuts off one of the main routes by which hearing improves, which is playing the material. Learners could stall at gates they would pass faster by playing.
- **Constraint:** auditory–motor coupling (playing builds the auditory representation; E095, E096, neural evidence in non-musicians). Adult acquisition of harmonic and modal hearing is slow and varies a lot, and two-hour-a-day adults are a dropout risk if gated for weeks.
- **Other points raised:**
  - "Usually a hearing bottleneck" is asserted, not measured.
  - Plateaus can be rhythmic, technical or about practice design.
  - Singing confounds voice control with hearing.
  - Theory labels can *train* perception (expose → label → compare → play → drill).
- **Evidence needed:** base rates of ear, timing and technique deficits in plateaued intermediates, plus whether ear deficits predict blind-rated playing. A three-arm trial (strict ear-gate / ear-coupled ungated / conventional), measuring transfer, retention and dropout. Gate telemetry (time-to-pass by concept type). Criterion validity of the gate.
- **Revision → v2:**
  - "Usually" became an explicit bet plus a per-learner screen.
  - The gate now covers only high-volume drilling, tempo ladders and use in improvisation. Labelling, comparison, slow sing- or hum-while-playing and call-and-response are allowed before it.
  - Singing is optional.

### Round 2 (v2; Claude)
- **Strongest objection:** the gate and the screen both use *guitar playback*, which measures hearing **plus ear-to-fretboard mapping plus execution**. Mapping is partly built by the repetition the gate withholds. So an ear-strong, map-weak learner would be misdiagnosed and blocked from the practice that fixes their actual bottleneck.
- **Constraint:** the gate's measuring instrument cannot separate an auditory deficit from an auditory–motor mapping deficit, which makes the policy self-defeating for that subgroup.
- **Evidence needed:**
  - A dissociation study: discrimination vs sing-back vs guitar playback on the same items.
  - A check of whether time-to-pass is predicted by ungated practice volume on the same material.
  - A matched-time, stratified trial: ear-gated vs ungated.
- **Revision → v3 (final):**
  - The screen and gate include a non-instrument response (same/different discrimination or hum-back).
  - Mapping repetition and slow, low-stakes improvisation are ungated.
  - The gate covers pitch and rhythm vocabulary, not pure motor drills.
  - Passing requires two separate days, because a single 4-of-5 test is noisy.
  - The gate applies to everyone, while the screen decides time allocation.
- **Not changed:** the core claim. Ear decides *when* drilling ramps up, and theory and scales stay. Neither model argued for theory-first. Both said the ear-first direction is defensible and that the *gate mechanism* carries the evidence burden. We agree, so the next test targets the gate (`next-test.md`).

---

## POV B — Feedback after every take, never during

### Round 1 (v1, Andre's wording; both models)
- **Strongest objection:**
  - *Claude:* per-take machine error detection outsources the learner's self-evaluation, which is the skill they need when the tutor is absent.
  - *GPT-5.5:* more error information than the learner can act on. They chase surface metrics, practice flow breaks, self-monitoring stays underdeveloped, and they optimise for what the tutor measures (credit assignment and actionability).
- **Constraint:**
  - The transfer condition: success has to be shown on delayed no-feedback retention and on new material, which is exactly where heavy feedback looks worst.
  - The learner's limited bandwidth to act on the next attempt.
- **Other points raised:**
  - "No benefit of reducing" ≠ "100% is optimal".
  - The guidance hypothesis was about *post*-trial feedback too, so "after the take" doesn't escape it.
  - Plateaued players may not be on "complex" material.
  - Machine false positives add up at 100%.
  - What's measurable may not be what's limiting.
- **Evidence needed:** an RCT in adult intermediates comparing 100% vs bandwidth vs faded feedback vs 100%-with-self-estimation. Outcomes: ≥1-week no-feedback retention, transfer, self-estimation accuracy, time lost to review, expert-rated quality, and analyser error rate on real home recordings.
- **Revision → v2:**
  - The claim is reduced to "withholding doesn't help" (E026). We do not claim "100% is better".
  - E024 was corrected: 100% beat *no* feedback, 50% was intermediate, and the feedback was concurrent.
  - A **self-estimate-before-reveal** step was added. Guadagnoli & Kohl 2001 (E097, verified): with 100% feedback, estimating first gave the best retention and not estimating gave the worst.
  - Feedback is limited to reliable dimensions, with one priority per take and low-confidence detections suppressed.

### Round 2 (v2; Claude)
- **Strongest objection: the "streetlight" problem.** If only machine-reliable dimensions can fill the single priority slot, hundreds of steering decisions over two years all point at timing and pitch. The real limits of plateaued players are often tension, time feel, tone and practice strategy. This invites a Goodhart effect: cleaner but no better.
- **Constraint:** the scope of measurable dimensions interacts with the one-priority rule.
- **Evidence needed:**
  - A diagnostic-mismatch study: what fraction of teachers' top limiting factors fall within the machine-reliable dimensions.
  - Whether machine-metric gains predict blind expert-rated quality.
  - An audit of priorities over time.
- **Other points:**
  - Suppression makes the tutor silent on the hardest passages, so show "couldn't assess".
  - Define "take" (per run-through, not per micro-repetition).
  - Adherence decays over two years.
  - Scope "no live feedback" so it doesn't ban metronomes and backing tracks.
- **Revision → v3 (final):**
  - The priority slot can hold a self-review target or a technique point from weekly human or video review.
  - Take = one full run-through.
  - "Couldn't assess" is shown and kept distinct from "no error".
  - Metronome, drone and backing tracks stay.
  - Self-vs-machine agreement and weekly no-feedback takes are tracked.
  - The pilot tests whether metric gains track blind expert ratings.
- **Not changed:** every full take gets feedback, and none is shown live. The round-2 critic called the timing and frequency half "reasonable to ship and refine". The open risk is scope (measurable ≠ limiting), which the pilot measures directly.
