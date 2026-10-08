EF='empirical finding'; TH='theory'; EA='expert advice'; INF='inference'; PH='product hypothesis'
E=[]
def e(src,claim,ft,quote,loc,qs,rel,br,pop='',instr='',lvl='',n='',design='',comp='',dur='',outcome='',num='',unc='',notes=''):
    E.append(dict(source_id=src,claim=claim,finding_type=ft,population=pop,instrument=instr,skill_level=lvl,n=n,design=design,comparator=comp,duration=dur,outcome_and_timing=outcome,result_numeric=num,uncertainty_limits=unc,supporting_quote=quote,location=loc,relevance_to_learner_group=rel,knowledge_tree_branch=br,notes=notes,_qs=qs))
X='extrapolated'; A='adjacent'; D='direct'

# ===================== ALTERNATIVES: adaptive vs fixed instruction (Part A) =====================
e('vanlehn2011','Step-based intelligent tutoring systems produced learning gains nearly as large as human tutoring relative to no tutoring (d = 0.76 vs d = 0.79), far below the widely believed d = 2.0 for human tutors.',EF,
  'it found that the effect size of human tutoring was much lower: d = 0.79. Moreover, the effect size of intelligent tutoring systems was 0.76, so they are nearly as effective as human tutoring.','Abstract (ERIC EJ946764)',('abs','vanlehn2011'),X,'alternatives',
  pop='K-12/college learners, mostly STEM',instr='none',lvl='mixed',design='review of controlled experiments',comp='no tutoring (same content without tutoring)',outcome='post-test learning gains (various)',num='ITS d=0.76; human tutoring d=0.79',
  notes='Extrapolated: non-music, mostly well-defined STEM domains with checkable steps, short interventions. Author table (full text) also reports substep-based d=0.40 and answer-based d=0.31; not quoted here.')
e('kulikfletcher2016','Across 50 controlled evaluations, intelligent tutoring raised test scores by a median 0.66 SD, but the size of the gain depended heavily on whether outcomes were locally developed or standardized tests.',EF,
  'The median effect of intelligent tutoring in the 50 evaluations was to raise test scores 0.66 standard deviations over conventional levels, or from the 50th to the 75th percentile. However, the amount of improvement found in an evaluation depended to a great extent on whether improvement was measured on locally developed or standardized tests','Abstract (ERIC EJ1090502)',('abs','kulikfletcher2016'),X,'alternatives',
  pop='students in ITS evaluations',instr='none',lvl='mixed',n='50 evaluations',design='meta-analysis',comp='conventional instruction',outcome='test scores (local vs standardized)',num='median ES 0.66 SD',
  notes='Same abstract: evaluations with nonconventional controls or flawed implementations showed small effects. Implies outcome alignment inflates ITS effects; any guitar tutor needs an outcome not built by the tutor itself.')
e('ma2014','ITS outperformed teacher-led large-group instruction, non-ITS computer instruction and textbooks/workbooks.',EF,
  'The use of ITS was associated with greater achievement in comparison with teacher-led, large-group instruction (g = .42), non-ITS computer-based instruction (g = .57), and textbooks or workbooks (g = .35).','Abstract (journal PDF p. 901)',('raw','ma2014'),X,'alternatives',
  pop='14,321 participants, all education levels',instr='none',lvl='mixed',n='107 effect sizes',design='meta-analysis',comp='large-group teaching; non-ITS CBI; textbooks',outcome='achievement',num='g=0.42 / 0.57 / 0.35',
  notes='PDF typesets “=” as a special glyph; quote normalized. ERIC abstract gives the same values as 0.42/0.57/0.35.')
e('ma2014','ITS were not better than individualized human tutoring or small-group instruction.',EF,
  'There was no significant difference between learning from ITS and learning from individualized human tutoring (g = –.11) or small-group instruction (g = .05).','Abstract (journal PDF p. 901)',('raw','ma2014'),X,'alternatives',
  pop='14,321 participants',instr='none',lvl='mixed',n='107 effect sizes',design='meta-analysis',comp='individual human tutoring; small-group instruction',outcome='achievement',num='g=-0.11 (vs human tutor); g=0.05 (vs small group)',
  notes='Directly relevant to the comparator question: a well-run individual teacher is a strong baseline; adaptivity gains are largest against weak comparators.')
e('kulik1990','Mastery-learning programs raised examination performance (average ES 0.52 across 103 studies), with stronger effects for weaker students.',EF,
  'The average effect size in the 103 studies was 0.52','Full text (results section)',('raw','kulik1990'),X,'alternatives',
  pop='college, high-school, upper-elementary students',instr='none',lvl='mixed',n='108 evaluations (103 with exam ES)',design='meta-analysis',comp='conventional instruction',outcome='examination performance',num='ES=0.52',
  notes='Abstract also: “The effects appear to be stronger on the weaker students in a class”. Mastery gating is a fixed-criterion form of adaptation, not diagnosis-driven sequencing.')
e('kulik1990','Self-paced mastery programs often reduced completion rates in college classes and may increase time on task — a cost relevant to adult self-paced learners.',EF,
  'self-paced mastery programs often reduce the completion rates in college classes','Abstract',('abs','kulik1990'),X,'feasibility',
  pop='college students',instr='none',lvl='mixed',design='meta-analysis',outcome='course completion',
  notes='Full-text PDF renders “selfpaced”; abstract text used. Adherence cost of mastery gating — relevant to 2-year adult retention.')
e('elsadat2026','In a small adaptive (multi-armed-bandit) vs fixed-sequence interval ear-training study, accuracy and response-time differences favored the adaptive tutor but were not statistically significant.',EF,
  'However, one-tailed independent t-tests show these differences are not statistically significant (accuracy t = 0.993, p = 0.167, response time t = −0.627, p = 0.270).','§4.2 Human User Study',('raw','elsadat2026'),A,'alternatives',
  pop='mostly non-musicians/novices (84.2% no ear training)',instr='none (aural intervals)',lvl='novice',n='19 (9 adaptive, 10 fixed)',design='between-subjects user study',comp='fixed instructional sequence',dur='single study period, ≥200 trials',outcome='accuracy, response time, phases mastered (end of study)',num='accuracy 76.0% vs 72.4%; phases mastered 2.22±0.44 vs 2.10±0.32 (p=0.251)',unc='underpowered; one-tailed tests',
  notes='Only music-specific adaptive-sequencing comparison found. Adjacent: aural skill, novices, short. Survey ratings favored adaptive but were not significant.')
e('elsadat2026','The adaptive tutor needed several hundred mastered items before confirming mastery, which the authors judge possibly too conservative for real-world use — diagnosis cost is high even in a narrow skill.',INF,
  'the tutor requires several hundred successfully mastered practice items before confirming the student\'s skills with sufficient certainty, which may be excessively conservative and impractical in real-world learning scenarios.','§5 Discussion',('raw','elsadat2026'),A,'measurement',
  pop='simulated + human learners',instr='none (aural intervals)',lvl='novice',design='simulation + user study',num='simulated time-to-recognize mastery 84.80±54.93 to 410.14±371.34 questions across profiles',
  notes='Authors’ interpretation. Numbers from §4.1 simulation.')
e('hattie2025','Across four meta-analyses testing the matching (aptitude-treatment) hypothesis for learning styles, the pooled effect of matching instruction to learner style was near zero.',EF,
  'These meta-analyses capture findings from 143 studies and summarize 401 effects with an overall effect size of d = 0.04 (se = 0.21).','Section “Matching Studies Overview”',('raw','hattie2025'),X,'alternatives',
  pop='general education',instr='none',lvl='mixed',n='143 studies / 401 effects',design='meta-synthesis of 4 meta-analyses',comp='mismatched / regular instruction',outcome='achievement',num='d=0.04 (se 0.21)',
  notes='Caveat: learning-style matching is a weak form of adaptation; it does not test skill-state-based adaptation (which ITS do).')
e('pashler2008','A valid test of adaptation-to-learner-type requires a crossover interaction; the learning-styles literature lacks such evidence.',TH,
  'A key conclusion of Pashler et al. was that there is “no adequate evidence base to justify incorporating learning style assessments into general educational practice” (p. 105).','Hattie & O’Leary 2025, section “The Controversial Challenge of Learning Styles”, quoting Pashler et al. 2008 p. 105',('raw','hattie2025'),X,'alternatives',
  pop='general education',design='critical review',notes='Secondary quote — verified against the 2025 review, not the 2008 original.')
e('cronbach1977','Classic aptitude-treatment-interaction research concluded that robust ATI findings are scarce.',TH,
  '“well-substantiated findings regarding ATI are scarce” (p. 6)','Hattie & O’Leary 2025, “Confound 2”, quoting Cronbach & Snow 1977 p. 6',('raw','hattie2025'),X,'alternatives',
  pop='general education',design='handbook review',notes='Secondary quote only.')
e('wong2021','For novice interval identification without reference songs or singing, interleaved practice produced better classification of new interval instances than blocked practice.',EF,
  'interleaving (M = .32, SD = .12) produced significantly better test performance than blocking (M = .24, SD = .14), F(1, 43) = 12.40','Experiment 2, Results',('raw','wong2021'),A,'learning-evidence',
  pop='Singapore university students, interval novices',instr='none (aural, melodic ascending intervals)',lvl='novice',n='44 analysed (Exp 2)',design='within-subjects, interleaved vs blocked',comp='blocked schedule',dur='single session',outcome='identification of novel interval instances, same session',num='.32 vs .24 proportion correct; p=.001; ηp²=.22',
  notes='Exp 1 (with reference songs + singing) found no difference (.27 vs .28). Benefit is context-dependent. Low absolute accuracy (~1/3).')
e('wong2021','Most learners misjudged blocking as at least as effective as interleaving, even when their own results showed the opposite.',EF,
  'Overall, 73% (32 out of 44) of participants had better or comparable performance in the interleaved than blocked condition, but 75% (33 out of 44) of participants','Experiment 2, metacognitive judgments (p. 1039)',('raw','wong2021'),A,'learning-evidence',
  pop='university novices',lvl='novice',n='44',design='within-subjects + judgment questionnaire',outcome='perceived effectiveness vs actual',num='73% better/comparable with interleaving; 75% judged blocking as good or better',
  notes='Quote continues: “thought that blocking was as good as or better than interleaving”. Supports not leaving schedule choice purely to learner preference.')

# ===================== MEASUREMENT: diagnosis reliability (Part A) =====================
e('liu2017','Learner-model estimates of student ability were reliable and valid, but individual learning-rate estimates were reliable in only one of two datasets.',EF,
  'Estimates of student ability were reliable and valid: they were consistent across both models and across both datasets, and they significantly predicted out-of-tutor pretest data. In one of the datasets, estimates of student learning rate were reliable and valid','Abstract',('raw','liu2017'),X,'measurement',
  pop='high-school geometry students',instr='none',lvl='school',n='196 students',design='secondary analysis of tutor logs (iAFM, iBKT)',comp='two models x two datasets',outcome='consistency across models; prediction of external pre/post tests',
  notes='For the Chapter 3 dataset: “we did not find strong evidence of reliability and validity of the student-specific parameter estimates.” Extrapolated: well-defined domain, many observations per skill.')
e('liu2017','Reliable individual estimates require many observations per skill per student (“deep” data), not just many students.',INF,
  'Key to expecting reliable, valid estimates of student-level constructs is not just big data in the','Introduction',('raw','liu2017'),X,'measurement',
  notes='Sentence continues “…‘long’ sense, but big data in the ‘deep’ sense.” (quote truncated at a line break in the PDF text). Implication: per-learner bottleneck diagnosis in guitar needs many scored attempts per sub-skill.')
e('bergee2003','Faculty juries showed good full-panel inter-judge reliability, but 2–3-judge panels were more variable; the author recommends at least five adjudicators.',EF,
  'Permutations of two and three evaluators, however, tended on average to exhibit more variability, greater range, and less uniformity than did groups of four and five.','Abstract',('abs','bergee2003'),A,'measurement',
  pop='university applied-music juries',instr='brass, percussion, woodwind, voice, piano, strings',lvl='university students',n='24 judges',design='inter-judge reliability across panel permutations',outcome='rating-scale totals, subscales, letter grade',
  notes='Abstract also: “Use of a minimum of five adjudicators for performance evaluation in this context was recommended.” Benchmark implication: a single teacher’s judgment is a noisy gold standard.')
e('thompson2003','Experienced evaluators agreed only moderately on conservatoire performances and showed bias linked to their own instrument.',EF,
  'Correlations between evaluators were only moderate, and some evidence of bias according to the evaluators\' own instrumental experience was found.','Abstract',('abs','thompson2003'),A,'measurement',
  pop='Royal College of Music students',instr='mixed',lvl='conservatoire',n='3 evaluators',design='inter-rater reliability',outcome='ABRSM-style marks',
  notes='Search summary cited r≈.33–.65 between evaluators; not verified from full text, so not entered as numeric.')
e('thompson2003','Sub-scores on a multi-criterion performance scheme were so highly inter-correlated that the scheme barely discriminated between categories (halo effect).',EF,
  'Strong positive correlations were found between items on the assessment scheme, indicating an extremely limited range of discrimination between categories.','Abstract',('abs','thompson2003'),A,'measurement',
  pop='conservatoire students',n='3 evaluators',design='inter-rater reliability',
  notes='Relevant to “grade only validated dimensions”: human sub-scores may not be separable dimensions.')
e('wesolowski2016','Expert judges differed significantly in severity, and even in how they used the rating-scale categories.',EF,
  'The data suggest that raters significantly vary in severity, items significantly vary in difficulty, and rating scale category structure significantly varies across raters.','Abstract',('abs','wesolowski2016'),A,'measurement',
  pop='jazz big bands (middle school to professional)',instr='jazz ensemble',n='23 judges, 24 performances',design='many-facet Rasch partial-credit model',outcome='rater severity, item difficulty, scale structure')
e('wesolowski2015','Expert raters’ severity was not invariant across ensemble levels; 10 of 24 raters showed differential severity.',EF,
  'Of the 92 potential pairwise interactions examined, 14 (15.2%) interactions were found to be statistically significant, indicating that 10 individual raters demonstrated differential severity across at least one school level.','Abstract',('abs','wesolowski2015'),A,'measurement',
  pop='large ensembles, 4 school levels',instr='ensembles',n='24 raters',design='many-facet Rasch differential rater functioning',num='14/92 interactions significant (15.2%)')
e('wesolowski2016cog','Raters clustered into three types (syntactical, expressive, mental-representation), suggesting raters attend to different dimensions.',EF,
  'The results provided three distinct rater-types: (a) the syntactical rater; (b) the expressive rater; and (c) the mental representation rater.','Abstract',('abs','wesolowski2016cog'),A,'measurement',
  pop='large-ensemble assessment',design='Rasch + clustering',notes='Exploratory typology (caution).')
e('moura2024','Published solo-performance assessment systems mostly target high-school/university students and do not differentiate criteria by learning stage.',EF,
  'No differentiation was found in assessment criteria based on students\' learning stages, suggesting an area for improvement in refining these assessment methods.','Abstract',('abs','moura2024'),A,'measurement',
  pop='20 papers, 26 assessment systems',instr='mixed solo',lvl='high school / university',design='PRISMA systematic review',
  notes='No validated rubric targets adult intermediate self-learners; a tutor would need its own level-appropriate criteria.')

# ===================== LEARNING-EVIDENCE: feedback (Part A) =====================
e('winstein1990','In lab motor tasks, KR that was faded across practice (lower average frequency) enhanced delayed retention compared with 100% KR — the classic support for the guidance hypothesis.',EF,
  'when the scheduling of KR was manipulated so that the number of KR trials was systematically lowered across practice, a reduced average relative frequency enhanced learning as measured by a delayed no-KR retention (Exp. 2) test','Abstract (BISp record)',('raw','winstein1990'),X,'learning-evidence',
  pop='adult lab participants',instr='none (lab movement task)',lvl='novice',design='3 lab experiments',comp='100% KR',dur='single acquisition session + delayed retention',outcome='delayed no-KR retention',
  notes='Abstract continues: “Empirical support is provided for the KR guidance hypothesis”. Extrapolated: simple lab task.')
e('wulf1998','For a complex ski-simulator skill, the 100% concurrent-feedback group outperformed no-feedback controls at retention, with the 50% group intermediate — reduced feedback showed no advantage, contrary to the simple-task guidance result.',EF,
  'The 100% feedback group demonstrated later relative force onsets than the control group in retention; the 50% feedback group showed intermediate performance.','Abstract',('abs','wulf1998'),X,'learning-evidence',
  pop='adult novices',instr='none (ski simulator)',lvl='novice',n='27 (Exp 2)',design='3-group experiment',comp='50% feedback; no feedback',dur='2 practice days, retention day 3',outcome='relative force onset at retention',
  notes='Authors: high feedback frequencies beneficial “at least until a certain level of expertise is achieved”. Small n. Corrected 2026-10-08: earlier wording said 100% beat 50%. The abstract reports 100% > no-feedback control with 50% intermediate, and gives no 100%-vs-50% test. Feedback was CONCURRENT (during the movement), not post-trial.')
e('wulfshea2002','Practice principles derived from simple lab tasks (including reduced feedback) do not reliably generalize to complex skills; high-load tasks benefit from load-reducing conditions.',TH,
  'The findings reviewed here call into question the generalizability of results from studies using simple laboratory tasks to the learning of complex motor skills.','Abstract',('abs','wulfshea2002'),X,'learning-evidence',
  design='narrative review',notes='Guitar technique and musical performance are complex skills — the simple-task feedback rules are an extrapolation.')
e('mckay2022ff','A meta-analysis of reduced-feedback-frequency experiments found no significant effect at any time point and no evidence of the predicted acquisition→retention reversal; studies were severely underpowered.',EF,
  'Results revealed substantial heterogeneity but no significant moderators, high levels of uncertainty, and no significant effect of reduced feedback frequency at any time point.','Abstract (PsyArXiv preprint)',('abs','mckay2022ff'),X,'learning-evidence',
  pop='motor-learning experiments',instr='none',lvl='mostly novice',n='61 papers, k=75, N=2,228',design='multilevel meta-analysis, z-curve',comp='100% / higher feedback frequency',outcome='acquisition, immediate and delayed retention',
  unc='z-curve: severely underpowered literature',notes='Published as Psychology of Sport and Exercise 61:102165 (paywalled). Search summary reported delayed-retention g≈.19 (CI −.05 to .43) — not verified from full text, so not entered as numeric.')
e('chiviacowsky2002','Learners who could request feedback (self-control) learned a timing task better on delayed transfer than yoked learners, and tended to request feedback after good trials.',EF,
  'The self-control group showed learning benefits on a delayed transfer test.','Abstract',('abs','chiviacowsky2002'),X,'learning-evidence',
  pop='adult lab participants',instr='none (sequential timing task)',lvl='novice',design='self-control vs yoked',comp='yoked feedback schedule',outcome='delayed transfer',
  notes='Single early study; see McKay et al. 2022 for bias-corrected meta-analysis of this literature.')
e('mckay2022sc','The apparent moderate benefit of self-controlled practice (g = .44) shrinks to a small, not-distinguishable-from-zero effect after correcting for publication bias and selective reporting.',EF,
  'a moderate benefit of self-controlled practice, g = .44 (k = 52, N = 2061, 95% CI [.31, .56]), was found … Overall, our results suggest the benefit of self-controlled practice on motor learning is small and not currently distinguishable from zero.','Abstract',('abs','mckay2022sc'),X,'learning-evidence',
  pop='self-controlled vs yoked experiments',instr='none',lvl='mostly novice',n='k=52, N=2,061',design='meta-analysis with weight-function selection model, p-curve',comp='yoked practice',outcome='retention tests',num='naive g=.44 [.31,.56]; selection-adjusted g=.107 [.047,.18]',unc='published vs unpublished studies differed; p-curve: no evidential value',
  notes='Two exact abstract segments joined by “…”.')
e('sigrist2013','Augmented-feedback research has mostly used simple or artificial tasks with visual feedback; how best to give feedback for complex real tasks remains controversial.',TH,
  'Related studies have focused primarily on simple or artificial tasks enhanced by visual feedback.','Abstract',('abs','sigrist2013'),X,'learning-evidence',design='narrative review')
e('wulfmornell2008','A motor-learning review aimed at music pedagogy recommends sparing feedback, variable task orders, observational practice, external focus and learner self-control.',EA,
  'The findings suggest that the effectiveness of practice in music may be enhanced if feedback is given sparingly, variable task orders and observational practice are incorporated, instructions and feedback are used to induce an ex-ternal focus of attention, and practice conditions allow for self-control.','Abstract (Elicit export)',('elicit',17),A,'current-practice',
  pop='motor-learning literature applied to musicians',instr='music (general)',design='narrative review',
  notes='This is the conventional advice that later meta-analyses (McKay et al. 2022 ×2) and the music focus-of-attention review (Hohagen & Immerz 2024) undercut. Elicit record lacked author/venue; verified as Wulf & Mornell 2008, Music Performance Research 2:1–25.')
e('hohagen2024','In music-specific experiments, neither external nor internal (or other) attentional focus showed consistent superiority for performance.',EF,
  'Finally, studies show no consistent results of superiority of either external or internal or otherwise different FOA considering positive effects on musical performance.','Abstract',('abs','hohagen2024'),A,'learning-evidence',
  pop='musicians in 15 experiments',instr='mixed',lvl='mixed',n='15 studies, 401 participants',design='systematic review',outcome='musical performance (expert ratings 27%, acoustic analysis 22% of outcome measures)',
  notes='Contradicts direct transfer of the sports external-focus rule to music.')
e('blanco2021','Real-time visual feedback on bowing improved kinematics during practice but impaired sound quality while active; after feedback was removed, the feedback group had better sound quality (dynamics control).',EF,
  'At the practice phase, the experimental group improved their bowing kinematics in comparison to the control group, but this was at the expense of impairing the sound quality of their performance. At the retention phase, the experimental group showed better results in sound quality, especially concerning control of sound dynamics.','Abstract (saved page, pass4)',('page','pass4#03'),A,'learning-evidence',
  pop='adults with no violin experience',instr='violin',lvl='novice',n='50 (24 RTVF, 26 control) + 15 experts',design='randomized controlled trial',comp='practice without external help',dur='single practice session',outcome='kinematics & sound quality during practice; retention/transfer without feedback (same session)',
  notes='Pass4#03. Only music RCT of real-time technology feedback found. Novices, very short; “retention” was a same-session no-feedback phase.')
e('blanco2021','More than half of the learners receiving real-time visual feedback reported they could not play while watching it.',EF,
  'More than half of the participants who received RTVF (55.2%) answered "Agree" or "Strongly Agree" in equal proportions to the statement which said "Cannot play while watching the feedback."','Results, questionnaire (saved page, pass4)',('page','pass4#05'),A,'feasibility',
  pop='violin novices',instr='violin',lvl='novice',n='RTVF group (24)',design='post-practice questionnaire',num='55.2% agree/strongly agree',notes='Pass4#05. Attentional cost of concurrent visual feedback.')
e('deja2022','A systematic review of augmented-piano prototypes found work concentrated on movement synchronisation, with gaps for sight-reading, motivation and improvisation, and no clear evidence that augmentation supports learning.',EF,
  'However, it is still unclear whether these solutions support the learning process.','Abstract',('abs','deja2022'),A,'alternatives',
  instr='piano',design='systematic review of prototypes',notes='Abstract: “prototypes are saturated on the synchronisation themes”.')

# ===================== FEASIBILITY / CURRENT PRACTICE: SRL & adherence (Part A) =====================
e('varela2016','Self-regulation processes show only weak positive relationships with music-learning outcomes; explicit self-regulation instruction was the most strongly related variable.',EF,
  'Findings indicate weak, positive relationships with the variables of interest, but suggest self-regulation instruction is the most strongly related variable.','Abstract',('abs','varela2016'),A,'learning-evidence',
  pop='music learners (mostly students)',instr='mixed',design='systematic review',notes='Authors call for research across “a broader spectrum of musicians” — adult amateurs under-represented.')
e('lubert2024','Self-regulation interventions for musicians show mixed evidence (mostly positive or non-significant effects on expert-rated performance); feedback, external focus, imagery+practice and some biofeedback can help.',EF,
  'The results show mixed evidence with mostly positive or non-significant effects, indicating that expressive writing, external focus, feedback, combined electromyographic (EMG) and electroencephalographic (EEG) biofeedback, and imagery combined with physical practice can increase expert-rated music performance quality.','Abstract',('abs','lubert2024'),A,'learning-evidence',
  pop='musicians in intervention studies',instr='mixed',n='89 studies',design='PRISMA systematic review',outcome='expert-rated performance quality',notes='Methodological quality flagged by authors.')
e('wang2025','A systematic review of metacognition/SRL interventions in music education reported a significant positive medium overall effect (meta-analysis of 7 studies), with weaker evidence outside secondary/university settings.',EF,
  'The meta-analysis revealed a significant positive medium effect overall.','Abstract (Elicit export)',('elicit',29),A,'learning-evidence',
  pop='preschool to university music students',instr='mixed',n='31 studies (7 meta-analysed)',design='systematic review + meta-analysis',
  notes='Authors call for “Extending samples to informal and professional music learners” — adult amateurs not covered. Effect size not given in abstract.')
e('krause2019','Among people who stopped making music, reasons clustered into access/opportunity, activity experience, obligations and difficulty with practicing.',EF,
  'An exploratory factor analysis of the quantitative responses identified 4 components relating to cessation: "access and opportunity," "activity experience," "obligations," and "difficulty with practicing."','Abstract',('abs','krause2019'),A,'problem',
  pop='Australian residents who ceased musical participation (M age 26.87)',instr='mixed',lvl='lapsed participants',n='190',design='online survey, EFA + grounded theory',outcome='self-reported reasons for cessation',
  notes='Retrospective self-report; not specific to intermediate guitarists.')
e('ritchie2018','In adult beginner string learners, a self-regulation worksheet increased self-regulatory behaviours but did not improve self-efficacy and was not seen by learners as helping.',EF,
  'the intervention was successful in promoting self-regulatory behaviours, the worksheet element had no impact on self-efficacy for learning and was not recognised by participants as directly influencing their learning.','Abstract',('abs','ritchie2018'),D,'feasibility',
  pop='adult beginners in semester string lessons',instr='strings',lvl='adult beginner',design='pilot intervention vs listening control',comp='listening to music, no practice structure',dur='one semester',outcome='SRL behaviours, self-efficacy',
  notes='Adult population (direct on age), but beginners not intermediates; pilot.')
e('leahy2021','Adult instrumentalists welcomed more teacher direction when facing technical difficulty or an unfamiliar style; more advanced adults reported higher self-direction.',EF,
  'Even in cases of teacher–student mismatch, more direction from the teacher was welcomed when they encountered technical difficulty or an unfamiliar style.','Abstract',('abs','leahy2021'),D,'current-practice',
  pop='adult instrumentalists and their teachers',instr='mixed',lvl='adult, beginner to advanced',n='6 students',design='qualitative (Grow SSDL)',
  notes='Abstract: “more advanced players reported intermediate to high levels of self-direction.” Supports adjustable directiveness rather than full self-control.')
e('wieser2024','Autonomous motivation was associated with lower, and controlled motivation with higher, dropout tendency in music-school students.',EF,
  'Autonomous motivation in lessons is negatively associated and controlled motivation is positively associated with the tendency to drop out of music schools.','Abstract',('abs','wieser2024'),X,'problem',
  pop='Austrian music-school students',instr='mixed',n='140',design='cross-sectional survey, SEM',outcome='dropout tendency (self-report)',notes='Youth music-school population; extrapolated to adults.')

# ===================== PROBLEM: practice-performance relationship =====================
e('platz2014','Accumulated task-relevant practice correlates strongly with musical achievement (corrected r = .61).',EF,
  'We identified an aggregated effect size ofr c =0.61; 95% CI [0.54, 0.67] for the relationship between task-relevant practice (which by definition includes DP) and musical achievement.','Abstract (saved page, pass2)',('page','pass2#16'),A,'problem',
  pop='musicians in 13 studies',instr='mixed (mostly classical)',lvl='mixed',n='13 studies, N=788',design='meta-analysis of correlational studies',outcome='objectively assessed achievement',num='rc=0.61',unc='95% CI [0.54, 0.67]',notes='Also Elicit row 0. Correlational; quote reproduces page spacing artefact “ofr c”.')
e('macnamara2014','Across domains, deliberate practice explained about 21% of performance variance in music.',EF,
  'We found that deliberate practice explained 26% of the variance in performance for games, 21% for music, 18% for sports, 4% for education, and less than 1% for professions.','Abstract (Elicit export)',('elicit',11),A,'problem',
  pop='88 studies across domains',instr='music among others',design='meta-analysis',num='music: 21% variance',notes='Elicit rows 11 and 13 are the same paper.')
e('hambrick2020','After psychometric correction, deliberate practice explained about 29.9% of reliable variance in music expertise (8 music studies; raw r = .43).',EF,
  'We identified six studies of chess and eight studies of music that reported a correlation between a measure of deliberate practice and performance. The average correlation wasr= 0.49 for chess andr= 0.43 for music before applying the standard psychometric correction for measurement error variance (unreliability) of the constituent measures. … The average amount of reliable variance in expertise explained by deliberate practice was 34% for chess and 29.9% for music.','Main text (saved page, pass2)',('page','pass2#04'),A,'problem',
  pop='music studies in reanalysis',instr='mixed',n='8 music studies',design='review with psychometric reanalysis',num='music r=0.43 raw; 29.9% reliable variance',
  notes='Pass2#04 (near-miss) — both segments are exact on the page; joined by “…”. Spacing artefacts “wasr=” are on the page.')
e('ericsson2019','The originator of deliberate-practice theory argues that under stricter study criteria practice explains far more variance (29%, 61% after attenuation correction).',EF,
  'A reanalysis of the remaining effects estimated that accumulated duration of practice explained considerably more variance in performance (29 and 61% after attenuation correction).','Abstract (saved page, pass2)',('page','pass2#05'),A,'problem',
  design='critical reanalysis',num='29% raw; 61% corrected',notes='Contested; see Hambrick et al. 2020 reply. Pass2#05.')
e('ericsson2021','Deliberate practice is defined by five criteria, including individualized guidance by a qualified teacher; practice meeting only the first four is “purposeful practice”.',TH,
  'Moxley et al. (2017) did not change any definitions, but used the name, purposeful practice, for those practice activities that met the first four criteria, but not the fifth criterion involving individualized guidance by a qualified teacher.','p. 1115–1116 (saved page, pass2)',('page','pass2#03'),A,'current-practice',
  design='theoretical commentary',notes='Pass2#03 near-miss fixed to the exact page text (PDF line-break hyphen “indi- vidualized”). Product implication: whether an AI tutor can supply the fifth criterion is an open question.')
e('mosing2014','In 10,500 twins, practice–ability associations were mostly genetic; within identical-twin pairs, the twin who practised more did not have better music-perception ability.',EF,
  'There was no difference in ability within monozygotic twin pairs differing in their amount of practice, so that when genetic predisposition was controlled for, more practice was no longer associated with better music skills.','Abstract (Elicit export)',('elicit',12),X,'problem',
  pop='Swedish twins',instr='n/a',lvl='general population',n='10,500',design='twin co-control',outcome='rhythm, melody, pitch discrimination tests',num='practice–ability rs=.18–.36; practice heritability 40–70%',
  notes='Outcome is perceptual discrimination, not instrumental performance — extrapolated.')
e('mosing2024','Heritability of musical auditory discrimination increased (rather than decreased) with more practice hours, contrary to deliberate-practice predictions.',EF,
  'Consequently, the relative genetic contribution (heritability) increased with more practice hours.','Abstract (Elicit export)',('elicit',1),X,'problem',
  pop='Swedish twins',n='6,471 twins (1,302 complete pairs)',design='twin moderation model',outcome='musical auditory discrimination',notes='Perceptual outcome.')
e('musicahodie_jazz','Longitudinal monitoring of vocal jazz-improvisation development showed rapid early gains followed by plateau phases and secondary acceleration.',EF,
  'The longitudinal monitoring of improvisational skill development revealed logarithmic progression curves, characterized by initial rapid advancement followed by plateau phases and secondary acceleration.','Abstract (saved page, pass2)',('page','pass2#12'),A,'problem',
  pop='vocal students',instr='voice (jazz)',design='longitudinal monitoring (details unclear)',
  notes='Only direct plateau-trajectory evidence found; quality uncertain (caution).')
e('hartz2016','Little research has examined how adult amateurs trained mainly in notation respond to ear-playing/improvisation instruction.',TH,
  'However, little attention has been focused on how adult musicians whose prior experience has been primarily limited to notation-based performance might respond to opportunities to learn by ear and to improvise.','Introduction (Elicit export)',('elicit',4),D,'problem',
  pop='adult amateur wind instrumentalists',instr='wind',lvl='adult amateur',notes='Gap statement from the paper’s introduction; the study’s results were not captured (Elicit exported intro text). Elicit rows 4–5 duplicate.')

# ===================== PROBLEM: playing-related health =====================
e('castillo2025','Playing-related problems are common in guitarists: pooled prevalence 51.8% any problem, 64.5% self-reported musculoskeletal symptoms, 42.2% clinically diagnosed disorders.',EF,
  'Twenty-two cross-sectional studies were included (n = 2,119). Pooled prevalence was 51.8% for any PRP, 64.5% for PRMS, 42.2% for PRMD, and 14.5% for PRND.','Abstract, Results (saved page, pass2)',('page','pass2#06'),D,'problem',
  pop='guitarists',instr='guitar',lvl='mixed',n='22 studies, n=2,119',design='meta-analysis of cross-sectional prevalence',num='PRP 51.8%; PRMS 64.5%; PRMD 42.2%; PRND 14.5%',
  notes='Preprint (not peer reviewed). Pass2#06 near-miss: medRxiv line numbers are interleaved in the saved text; quote is verbatim apart from those. Pass2#25 duplicate.')
e('rotter2020','Evidence that professional musicians are a distinct risk group for musculoskeletal complaints, and for causal risk factors, remains low because studies are heterogeneous and poorly controlled.',EF,
  'Therefore, evidence that being a professional musician is a risk factor for MCD as well as the causal relationship between these factors remains low despite the fact that a large number of studies have been performed.','Abstract (saved page, pass2)',('page','pass2#22'),A,'problem',
  pop='professional musicians',instr='mixed',lvl='professional',n='109 studies',design='systematic review',notes='Pass2#07/#22/#24 same study.')
e('chan2014','Clinical guidance recommends regular short practice breaks (about 5 min per 25 min of playing) to protect against recurrent playing-related disorders.',EA,
  'As a general recommendation, a 5-min rest break should be taken for every 25 min of playing (Zaza, 1994; Robinson and Zander, 2002; Ackermann, 2010).','Main text (saved page, pass2)',('page','pass2#21'),A,'feasibility',
  pop='musicians',instr='mixed',notes='Expert recommendation citing older observational work. Relevant to a 2 h/day plan.')
e('lund_guitar','For classical guitar, no study has tested playing position as a disorder risk factor; evidence quality is low.',EF,
  'The search yielded a total of thirteen articles concerning classical guitar and PRMD, none of which specifically address playing position as a risk factor.','Abstract (saved page, pass2)',('page','pass2#08'),D,'problem',
  instr='classical guitar',n='13 papers',design='systematic review (student thesis)')
e('laseur2023','Preventive interventions (especially strength training) reported benefits for playing-related musculoskeletal problems in at least 12 of 20 studies in professional musicians.',EF,
  'A significant beneficial effect of the evaluated intervention on either playing-related musculoskeletal disorders (PRMD) frequency or severity or (playing-related) pain frequency and intensity was reported in at least 12 of the 20 studies.','Abstract (Elicit export)',('elicit',21),A,'feasibility',
  pop='professional musicians',instr='mixed',lvl='professional',n='20 studies',design='systematic review')
e('dossantos2024','In a Portuguese guitarist survey, 53.3% reported a playing injury; not warming up was associated with injury.',EF,
  'Fifty-six (53.30%) guitar players had injuries throughout their musical practice, totaling 132 injuries','Abstract (Elicit export)',('elicit',22),D,'problem',
  pop='guitar players in Portugal (98% men, 30–75 y)',instr='guitar',n='105',design='cross-sectional survey',num='lifetime injury 53.3%; injury rate 0.42 per 1,000 h',notes='Convenience sample.')

# ===================== CURRENT PRACTICE / LEARNING EVIDENCE: practice schedules & pedagogy =====================
e('carter2016','Advanced clarinetists’ pieces practised in an interleaved schedule were rated better than blocked pieces when ratings differed, but results varied across raters.',EF,
  'Overall, whenever there was a ratings difference between the conditions, pieces practiced in the interleaved schedule were rated better than those in the blocked schedule, although results varied across raters.','Abstract (saved page, pass3)',('page','pass3#19'),A,'learning-evidence',
  pop='advanced clarinetists',instr='clarinet',lvl='advanced',n='10',design='within-subjects blocked vs interleaved',comp='blocked schedule',dur='12 min practice per piece',outcome='expert ratings end of practice and 1 day later',notes='Elicit row 15 same study. Very small n; rater disagreement.')
e('uwo_pianists','In proficient pianists, blocked vs interleaved practice schedules showed no significant differences.',EF,
  'A two-way repeated measures ANOVA analysis revealed no significant main effect of day on practice schedule, (F(1,20) = .15, p = 0.70, ηp2 = .01), or schedule on day, (F(1,20) = 1.03, p = .32, ηp2 = .05), with no significant interaction between the two variables (F(1,20) = 3.20, p = .77).','Abstract (saved page, pass3)',('page','pass3#20'),A,'learning-evidence',
  pop='proficient pianists',instr='piano',lvl='proficient',n='21',design='within-subjects, two days',comp='blocked schedule',num='F(1,20)=1.03, p=.32',notes='Thesis. Reported p=.77 for F=3.20 looks inconsistent (as printed).')
e('bangert2013','Pianists trained with variable leap distances improved by the next day while fixed-distance trainees did not.',EF,
  'In the VAR group significant improvement was seen on the next day. This was not the case in the FIX group.','Abstract (Elicit export)',('elicit',14),A,'learning-evidence',
  pop='pianists',instr='piano',lvl='trained',design='fixed vs variable practice',comp='fixed (target interval only)',dur='30-min training, 24-h retest',outcome='leap distance error / execution time',notes='n not in abstract.')
e('rose2006','University musicians learning a percussion sticking pattern showed the contextual-interference cost in acquisition but no retention/transfer advantage for varied practice.',EF,
  'Evidence of a contextual interference effect resided in the acquisition phase, where varied participants experienced more error than blocked counterparts; however, in subsequent retention and transfer tasks, the rhythm and pattern accuracy for both groups was equivalent.','Abstract (Elicit export)',('elicit',16),A,'learning-evidence',
  pop='university musicians',instr='percussion sticking task',lvl='university',n='120',design='blocked vs varied vs control',outcome='retention (5 min to 24 h) and transfer',notes='Dissertation. Abstract also notes most participants’ self-structured practice was “simplistic with regard to problem solving”.')
e('schorn2021','Interleaved practice improved retention and transfer of fine-motor sequences even when learning was implicit.',EF,
  'Even for participants who reported no awareness of the sequences, interleaving led to a benefit for both retention and transfer compared to participants who practiced blocked sequences.','Abstract (saved page, pass3)',('page','pass3#05'),X,'learning-evidence',
  pop='adult lab participants',instr='none (serial reaction time)',lvl='novice',design='lab experiment',comp='blocked practice',outcome='retention and transfer',notes='Non-music task.')
e('rohrer2021','Interleaved physics homework improved recall and problem solving on surprise tests compared with blocked homework.',EF,
  'students recalled more relevant information and more frequently produced correct solutions after having engaged in interleaved practice (with observed median improvements of 50% on test 1 and 125% on test 2).','Abstract (saved page, pass3)',('page','pass3#06'),X,'learning-evidence',
  pop='undergraduate physics students',instr='none',lvl='novice',design='classroom intervention',comp='blocked homework',outcome='surprise criterial tests',num='median +50% (test 1), +125% (test 2)',notes='Authors are Samani & Pan (pass record said Rohrer et al.). Non-music.')
e('chen2021','Spacing and interleaving work through different mechanisms: spacing via working-memory recovery, interleaving via discriminative contrast between similar categories.',TH,
  'We suggest that spaced practice is a cognitive load effect that can be explained by working memory resource depletion during cognitive effort with recovery during rest-from-deliberate-learning, while interleaved practice can be explained by the discriminative-contrast hypothesis positing that interleaving assists learners to discriminate between topic areas.','Abstract (saved page, pass3)',('page','pass3#07'),X,'learning-evidence',
  design='systematic review',notes='Pass3#07 near-miss fixed: the model had dropped “with recovery during rest-from-deliberate-learning”.')
e('brumbach2022','High-school jazz students taught with a practice-based approach gained more in improvisation over four weeks than those taught with a theory-based approach.',EF,
  'A comparison of scores using a between-subjects repeated-measures ANOVA showed that the practice-based group achieved significantly greater gains in improvisation than the theory-based group.','Abstract (Elicit export)',('elicit',2),A,'alternatives',
  pop='high-school jazz musicians',instr='jazz band',lvl='high school',n='191 (13 vs 21 soloists)',design='randomized by band, pre/post',comp='theory-based instruction',dur='4 weeks',outcome='improvisation scores by 3 judges at post-test',notes='Small soloist subsample: the improvisation comparison rests on 13 vs 21 soloists. Corrected 2026-10-08: earlier wording said "(aural)"; the abstract does not describe the content of the practice-based condition. In the jazz-pedagogy literature (Prouty 2012, as summarised by Bjerstedt 2016), practice-based means learning from recordings, transcription and imitation; whether Brumbach followed that is not confirmed from the full text.')
e('marino2023','In a 12-week middle-school improvisation environment, learners improved on all outcomes, and the order of modal vs blues tasks made no difference.',EF,
  '(d) no significant effect according to instructional sequence of harmonic form (i.e., modal/blues vs. blues/modal).','Abstract (Elicit export)',('elicit',3),X,'alternatives',
  pop='5th–8th-grade instrumentalists',lvl='beginner (children)',n='43',design='12-week design study, two sequences',comp='alternative task order',dur='12 weeks',notes='Sequence order did not matter — weak case for fine-grained sequencing.')
e('laughlin2001','Beginning jazz improvisers taught with aural exercises improved more in harmonic accuracy than those taught with notated exercises.',EF,
  'students who received the aural method of pedagogy produced greater improvement for all measurement items.','Abstract (Elicit export)',('elicit',10),A,'alternatives',
  pop='student volunteers',lvl='beginning improvisers',n='20',design='two-method comparison, 6 judges',comp='notated exercises',outcome='harmonic accuracy pre/post',notes='Dissertation; small n.')
e('palmer2016','Aural imitation ability and technical facility were fundamental correlates of jazz improvisation achievement.',EF,
  'Results indicate that aural imitation ability and technical facility are fundamental skills supporting jazz improvisation achievement.','Abstract (Elicit export)',('elicit',8),A,'measurement',
  pop='high-school and college instrumentalists',lvl='novice to advanced',n='70',design='exploratory correlational',notes='Proposes developmental levels by musical category — candidate skill dimensions.')
e('boucher2019','College-level classical guitarists who used video feedback changed how they self-evaluated during practice, more so in higher performers.',EF,
  'Our results indicate that musicians who used video feedback modified the way they formulated their self-evaluative comments while practicing, and that these changes were more marked with higher-performing musicians.','Abstract (Elicit export)',('elicit',6),D,'learning-evidence',
  pop='college-level classical guitarists',instr='classical guitar',lvl='intermediate-advanced',n='16 (8 vs 8)',design='quasi-experimental',comp='no video feedback',dur='10 practice sessions',outcome='coded self-evaluative comments',notes='Closest population match found (guitar, intermediate+). Process outcome, not performance.')
e('uwo_video_guitar','Adult beginner classical guitarists who practised with weekly video recording outperformed controls on performance measures; self-regulation did not change.',EF,
  'Results from the performance measures indicated statistically significant (p = .037) group differences, suggesting that the experimental group performed more musically, with better tone, greater rhythmic precision, and with a more secure technical foundation than the control group.','Abstract (saved page, pass2)',('page','pass2#18'),D,'learning-evidence',
  pop='adult beginner classical guitarists',instr='classical guitar',lvl='adult beginner',design='experimental vs control',comp='no video recording',outcome='performance ratings; SRL; self-efficacy',num='p=.037',notes='Thesis; n not captured. Same abstract: self-regulation measures not significant.')
e('wopereis2015','Elite vs semi-elite jazz improvisers differed in the intensity and quality of individual practice, group practice (jam sessions) and network activities.',EF,
  'Findings on learning during pre-conservatory, conservatory, and post-conservatory phases revealed group differences in intensity and quality of individual practice, group practice (e.g., participation in jam sessions), network activities that create further opportunities for development and work','Abstract (Elicit export)',('elicit',9),A,'current-practice',
  pop='elite vs semi-elite jazz improvisers',lvl='expert',n='11 (6 vs 5)',design='retrospective multiple-case study')
e('solstad2020','Expert jazz guitarists’ improvisation is explained through chunking, schemas and templates, with strong dependence on context and interplay.',TH,
  'By linking practical context to a cognitive framework using chunking (grouping), schema (context) and template theory (domain specific knowledge), this is also a study of expertise.','Introduction chapter (saved page, pass2)',('page','pass2#02'),A,'current-practice',
  pop='5 world-class jazz guitarists',instr='jazz guitar',lvl='expert',design='practice-based qualitative',notes='Pass2#00/#01/#02/#09/#11 and Elicit row 7 = one study.')
e('karpinski2021','Aural-skills theory: tonic inference is the first and most fundamental process when listening to tonal pitches (argument for tonic-based solmization).',TH,
  'it concludes that the first and most fundamental process listeners carry out while attending to the pitches of tonal music is tonic inference.','Article abstract (saved page, pass1)',('page','pass1#13'),A,'current-practice',
  design='theoretical article',notes='No learner data.')
e('stthomas_kodaly','Kodály-inspired teachers described a consistent modality sequence for teaching musical elements: aural, kinesthetic, oral, visual.',EA,
  'Further, the following modalities sequence was identified as a result of the collected data: aural, kinesthetic, oral, and visual.','Abstract (saved page, pass1)',('page','pass1#23'),X,'current-practice',
  pop='Kodály-inspired teachers',design='qualitative',notes='Teacher perceptions, children’s classes.')
e('shareok_gordon','A randomized test of Gordon learning-sequence instruction found only an interaction between private lessons and group on the tonal post-test.',EF,
  'a significant interaction existed between private lessons and group assignment in the post-test tonal dimension, F(1,72) = 4.61, p. < .04.','Abstract (saved page, pass1)',('page','pass1#26'),X,'alternatives',
  pop='school students',n='73',design='randomized pre/post, MANCOVA',num='F(1,72)=4.61, p<.04',notes='Pass1#26 near-miss fixed to exact abstract text (main effects were non-significant).')
e('russell2017','Tertiary jazz students in an a-cappella ear-training program came to recognize theory concepts in practice (qualitative, author-evaluated).',EF,
  'Analysis of the data confirmed that AET enabled the development of a theoretically informed practice whereby the participating students came to recognize concepts in practice and performance.','Abstract (Elicit export)',('elicit',23),A,'alternatives',
  pop='tertiary jazz students',design='qualitative participant observation',notes='Author evaluating own method.')
e('hu2026','Undergraduate jazz students’ views of chord-scale theory and transcription depended on external, interpersonal and intrapersonal factors.',EF,
  'The dynamic interplay between these factors greatly affected student perceptions of the viability and relevance of chord-scale theory and transcription to their own development.','Abstract (Elicit export)',('elicit',27),A,'current-practice',
  pop='undergraduate jazz majors',design='qualitative survey + interviews')
e('moore2016','A collegiate jazz-improvisation rubric was built from content analysis with dimensions for technique, expression, rhythm, melody, harmony, interaction and overall.',EF,
  'A rubric was created using these concepts and included the following dimensions: technique, expression, rhythm, melody, harmony, rhythmic interaction, melodic interaction, harmonic interaction, and overall improvisation.','Abstract (Elicit export)',('elicit',26),A,'measurement',
  pop='collegiate improvisers',design='rubric development',notes='Reliability/validity not reported in captured text.')
e('how2021','Music-practice research is dominated by quantitative designs and by deliberate practice, practice strategies, mental practice, metacognition and self-regulation topics.',EF,
  'Quantitative research designs were most prevalent, accounting for two-thirds of all studies reviewed (66.2%), with questionnaires and recordings being the most common methods of data collection.','Abstract (Elicit export)',('elicit',28),A,'current-practice',
  n='296 publications',design='PRISMA review')
e('zorn1995','College students found an interactive computer program for jazz improvisation motivating and non-threatening (self-report only).',EF,
  'The data indicated that the students found the program motivating and comprehensive in content, whether or not they had had previous formal improvisation instruction.','Abstract (Elicit export)',('elicit',18),A,'feasibility',
  pop='college volunteers',design='interviews',notes='Attitudes only; 1995 technology.')
e('minnich2014','Fourth-grade string students learning a bowing technique through improvisation transferred it about as well as those learning through repertoire.',EF,
  'Participants in both groups seemed to transfer their technique to both familiar and unfamiliar contexts to approximately the same degree.','Abstract (Elicit export)',('elicit',30),X,'alternatives',
  pop='4th-grade string students',instr='strings',lvl='beginner (children)',n='9',design='quasi-experiment',notes='Tiny n, children.')

# ===================== FEASIBILITY / MEASUREMENT: technology (pass4 etc.) =====================
e('bittner2022','A lightweight instrument-agnostic transcription model reached state-of-the-art note transcription on GuitarSet.',EF,
  'When compared with instrument-specific models, we see that NMP achieves state-of-the-art results on GuitarSet.','§5 Conclusions (saved page, pass4)',('page','pass4#00'),D,'feasibility',
  instr='guitar (GuitarSet) and others',design='benchmark evaluation',notes='Pass4#00 near-miss fixed: quote trimmed before a PDF line-break hyphen. Same paper: not better than instrument-specific models for piano and vocals. Transcription accuracy ≠ pedagogical assessment validity.')
e('bittner2022','The transcription model is very small (16,782 parameters), making on-device use plausible.',EF,
  'is a fully convolutional model taking audio as input and produces three posteriorgram outputs, with a total of only 16,782 parameters.','§2 Model (saved page, pass4 HTML)',('page','pass4#09'),D,'feasibility',design='model description',num='16,782 parameters')
e('basicpitch','Spotify’s open-source Basic Pitch library provides lightweight polyphonic audio-to-MIDI transcription usable across instruments.',EA,
  'Basic Pitch is a Python library for Automatic Music Transcription (AMT), using lightweight neural network developed by [Spotify\'s Audio Intelligence Lab].','README (saved page, pass4)',('page','pass4#01'),D,'feasibility',
  instr='multi (incl. guitar)',design='software documentation',notes='Vendor self-description.')
e('fretwork2026','A student guitar transcription-to-tab pipeline reached full-pipeline F1 0.77 on GuitarSet; the authors identify pitch detection, not fret assignment, as the bottleneck.',EF,
  'The near-match F1 of 0.78 reveals that the fretboard assignment itself is largely correct; the main bottleneck is pitch detection, not our algorithm.','Project page (saved page, pass4)',('page','pass4#22'),D,'feasibility',
  instr='guitar',design='benchmark (LOOCV)',num='F1 0.42 → 0.54 → 0.72 → 0.77; near-match 0.78',notes='Not peer reviewed. Pass4#02 quote had an invented clause (“for which we are constrained by Spotify’s Basic Pitch…”); not on page — replaced by pass4#22 verbatim text.')
e('pianoeval2026','A multi-task deep model predicted expert piano technique ratings with correlations of .74–.91 across five dimensions.',EF,
  'On our newly constructed PianoEval dataset of 1,012 expert-annotated performances, the model attains Pearson correlations of 0.91, 0.89, 0.85, 0.80 and 0.74 on the five dimensions respectively (averaging 0.838), with mean squared error of 0.024 and three-tier classification accuracy of 81.7%, beating five baselines on every dimension.','Abstract (saved page, pass4)',('page','pass4#19'),A,'measurement',
  instr='piano',n='1,012 performances',design='model development / benchmark',num='r=0.91/0.89/0.85/0.80/0.74 (mean 0.838); 81.7% 3-tier accuracy',
  notes='Agreement with the same annotators used for training; inter-human reliability not given here. Weakest dimension r=.74.')
e('erhu2026','A pilot AI erhu practice system agreed closely with expert raters on pitch and rhythm (r = .93, .83) but problem-note detection F1 was only .705.',EF,
  'Thirty-six valid recordings from 18 conservatory students were blindly rated by two experts (ICC = 0.92). System scores correlated strongly with expert ratings for pitch (r = 0.93, 95% CI [0.82, 0.97]) and rhythm (r = 0.83, 95% CI [0.60, 0.94]); problem-note F1 was 0.705 and problem-measure F1 was 0.763.','Abstract (saved page, pass4)',('page','pass4#21'),A,'measurement',
  instr='erhu',lvl='conservatory',n='36 recordings / 18 students',design='pilot validation',num='expert ICC 0.92; pitch r=0.93; rhythm r=0.83; problem-note F1 0.705',unc='pitch 95% CI [0.82, 0.97]; rhythm [0.60, 0.94]',notes='Preprint. Score-level agreement high, but locating specific problems (diagnosis) much weaker.')
e('ej1483320','Automated creativity scores for children’s music programs correlated moderately (r = .48) to strongly (LLM, r = .68) with human ratings.',EF,
  'Results revealed moderate to strong correlations with human evaluations (ECD-based:r=0.48; LLM-based:r=0.68), with the LLM-based approach demonstrating greater consistency across varying learning examples ( r=0.82).','Abstract (saved page, pass4)',('page','pass4#20'),X,'measurement',
  pop='primary students',lvl='children',n='383 programs / 194 students',design='automated vs human consensual ratings',num='r=0.48 (ECD); r=0.68 (LLM)',notes='Programming artefacts, not performance.')
e('pmc12953392','Assessment-oriented AI in music learning most consistently strengthened ability beliefs via objective visual feedback; adaptive AI more often supported sustained engagement.',EF,
  'Assessment-oriented AI most consistently strengthened ability beliefs via objectified, visualized feedback and positioned cognitive agency around self-monitoring, self-reactiveness, and self-reflectiveness.','Results/abstract (saved page, pass4)',('page','pass4#14'),A,'feasibility',
  design='systematic review',notes='Psychological outcomes, not skill outcomes. Title frames a dependency risk.')
e('ijim2024','AI-in-music-education research is early-stage and concentrated on university instruction (largely in China).',EF,
  'A key finding is that the implementation of bibliometric analyses suggests that AI research in music education is still in its infancy.','Abstract (saved page, pass4)',('page','pass4#16'),A,'feasibility',
  n='31 articles',design='systematic review / bibliometric',notes='Pass4#16 near-miss: page has PDF line-break hyphens (“develop- ment”); quote shortened to an exact span.')
e('sciltp2026','A narrative review claims CNN+RNN music models achieve near-human performance in instrument recognition, onset detection and chord recognition.',EA,
  'The combination of Convolutional Neural Networks (CNNs) [23,41] and Recurrent Neural Networks (RNNs) [42,43] effectively processes the time-frequency characteristics of musical audio, achieving near-human performance in tasks such as instrument recognition, onset detection, and chord recognition.','§ on deep learning (saved page, pass4)',('page','pass4#15'),A,'feasibility',
  design='narrative review',notes='Low-profile venue; “near-human” is a summary claim.')
e('passalenti2019','In a virtual guitar, combined vibrotactile + force feedback felt most realistic and reduced accidental string hits.',EF,
  'The results indicate that the combination of vibrotactile and force feedback elicits the most realistic experience, and during this condition, participants were less likely to inadvertently hit strings.','Abstract (saved page, pass4)',('page','pass4#18'),X,'feasibility',
  instr='virtual guitar',design='within-subjects haptic conditions',notes='Realism outcome; no learning outcome.')
e('aismfc2025','An adaptive “fuzzy control” music-instruction system reported gains on self-defined adaptability/efficiency metrics, not on learning outcomes.',EF,
  'Thus, compared to other methods, the system improves adaptability by 13.9%, efficiency analysis by 9.02%, and constraint detection by 10.26%.','Conclusion (saved page, pass3)',('page','pass3#00'),X,'alternatives',
  design='system proposal with simulated metrics',num='+13.9% / +9.02% / +10.26% (self-defined metrics)',notes='Example of adaptive-music-instruction claims without learner outcomes.')

e('bjerstedt2016','A jazz-education scholar characterises the main tendency of formal jazz education as theory-based pedagogy, quoting Monson (2002) that the chord–scale approach has dominated jazz pedagogy since the 1960s.',EA,
  'Notwithstanding, one main tendency in jazz education has been directed towards theory-based pedagogies. … Since the 1960s, jazz pedagogy has been dominated by the chord–scale approach to jazz harmony.','Section "Learning Jazz"',('raw','bjerstedt2016'),A,'current-practice',
  pop='formal jazz education (scholarly characterisation)',design='conceptual article drawing on an interview study',notes='Scholarly characterisation of the field, not an outcome study. Used as a citation for the "theory-first" consensus that POV A opposes. Monson quote is secondary.')
e('bjerstedt2016','Interviewed Swedish professional jazz musicians thought formal jazz education leans on chord/scale methods because they are easy to teach and measure; one argued technical practice should get less focus and listening and playing together more.',EA,
  'Several informants agree that jazz education is probably marked by what is easy to teach. They believe that the chord/scale formulaic methods are likely to remain a popular approach in jazz pedagogy for several reasons: it is comparatively easy to verbalize and communicate, it is measurable to some degree, and it has come to be perceived as a stepping stone in improvisational instruction.','Section "Landscape of Learning"',('raw','bjerstedt2016'),A,'current-practice',
  pop='15 Swedish professional jazz musicians (interviews, Bjerstedt 2014)',lvl='professional',n='15',design='qualitative interviews (reported secondarily)',notes='Expert opinion. The Kullhammar recommendation ("technical practice ought to be less focused on") is on the same page. Supports the claim that the consensus exists and is partly convenience-driven; it is not evidence that ear-first works better.')
e('lahav2007','After non-musicians learned to play a piece by ear, listening to it activated motor-related brain areas; equally familiar music they had not learned to play did not — hearing and doing become coupled through playing.',EF,
  'Although subjects listened to the music without performing any movements, activation was found bilaterally in the frontoparietal motor-related network','Abstract',('abs','lahav2007'),X,'learning-evidence',
  pop='non-musicians',instr='piano (lab)',lvl='novice',design='training + fMRI',outcome='brain activation while listening',notes='Neural outcome, not a learning or performance outcome. Same abstract: "listening to an equally familiar but motorically unknown music did not activate this network." Introduced by a pressure-test model; the abstract was verified before use.')
e('lappe2008','Two weeks of learning to play a sequence enhanced auditory-cortex representations of the music more than two weeks of listening-only training (non-musicians).',EF,
  'the SA group showed significant enlargement of MMNm after training compared with the A group, reflecting greater enhancement of musical representations in auditory cortex after sensorimotor-auditory training compared with after mere auditory training','Abstract',('abs','lappe2008'),X,'learning-evidence',
  pop='non-musicians',instr='piano (lab)',lvl='novice',design='two-group training study (MEG)',comp='listening-only training',dur='2 weeks',outcome='mismatch negativity (MMNm) pre/post',notes='Neural outcome; small lab study. Suggests playing can build hearing, which argues against a hard ear-before-play gate. Introduced by a pressure-test model; the abstract was verified before use.')
e('guadagnoli2001','With 100% knowledge of results, learners who first estimated their own error retained best, while those who did not estimate retained worst; 20% KR fell in between.',EF,
  'The group that received 100% KR and was required to error estimate during acquisition performed the best during retention. The 2 groups that received 20% KR performed less well. Finally, the group that received 100% KR and was not required to error estimate during acquisition performed the poorest during retention.','Abstract',('abs','guadagnoli2001'),X,'learning-evidence',
  pop='adults',instr='none (force-production task)',lvl='novice',n='64',design='2x2 factorial',comp='20% KR; no error estimation',outcome='no-KR retention',notes='Simple lab task. Key moderator for POV B: 100% feedback helped only when learners self-estimated first. Introduced by a pressure-test model; the abstract was verified before use.')
