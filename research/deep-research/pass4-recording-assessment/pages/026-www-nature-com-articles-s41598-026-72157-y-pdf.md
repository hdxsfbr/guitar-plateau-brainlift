<!--
url: https://www.nature.com/articles/s41598-026-72157-y.pdf
title: Multi-dimensional piano performance technique assessment and ...
query: automated music performance assessment ICC study
fetched: 2026-10-08T02:24:47.290Z
-->

Your privacy, your choice
-------------------------

We use essential cookies to make sure the site can function. We also use optional cookies for advertising, personalisation of content, usage analysis, and social media, as well as to allow video information to be shared for both marketing, analytics and editorial purposes.

By accepting optional cookies, you consent to the processing of your personal data - including transfers to third parties. Some third parties are outside of the European Economic Area, with varying standards of data protection.

See our [privacy policy](https://www.nature.com/info/privacy)
 for more information on the use of your personal data.

Manage preferences for further information and to change your choices.

Accept all cookies Reject optional cookies

[Skip to main content](https://www.nature.com/articles/s41598-026-72157-y#content)

Thank you for visiting nature.com. You are using a browser version with limited support for CSS. To obtain the best experience, we recommend you use a more up to date browser (or turn off compatibility mode in Internet Explorer). In the meantime, to ensure continued support, we are displaying the site without styles and JavaScript.

Multi-dimensional piano performance technique assessment and personalized teaching strategy generation based on deep learning

[Download PDF](https://www.nature.com/articles/s41598-026-72157-y_reference.pdf)

[Download PDF](https://www.nature.com/articles/s41598-026-72157-y_reference.pdf)

Abstract
--------

Automated assessment of piano performance technique, together with the delivery of personalized pedagogical feedback, remains a stubborn problem in intelligent music education. In this work we develop an integrated system that couples multi-dimensional technique evaluation with adaptive teaching-path planning inside a unified multi-task learning framework. Three design choices motivate the novelty here: a multi-granularity Constant-Q Transform feature encoder paired with cross-dimension channel attention; a four-layer Transformer that supplies a shared temporal representation to five dimension-specific projection heads — each scoring pitch accuracy, rhythmic stability, dynamics control, coherence, or expressiveness; and a reinforcement-learning curriculum sequencer that consumes the assessment vector together with a gated knowledge-tracing profile and then produces individualized exercise sequences. On our newly constructed PianoEval dataset of 1,012 expert-annotated performances, the model attains Pearson correlations of 0.91, 0.89, 0.85, 0.80 and 0.74 on the five dimensions respectively (averaging 0.838), with mean squared error of 0.024 and three-tier classification accuracy of 81.7%, beating five baselines on every dimension. In an eight-week controlled study with 45 participants, the full system delivered an absolute mean technique gain of 0.156, compared with 0.112 for assessment-only feedback and 0.086 for teacher-led instruction. The relative gain over traditional instruction therefore reached 81.4% (Cohen’s d = 1.12, 95% CI \[0.40, 1.84\]), and improvements were statistically significant on every dimension. We read these findings as evidence that tightly coupling fine-grained assessment with closed-loop personalized instruction can yield measurable pedagogical value.

### Similar content being viewed by others

![](https://media.springernature.com/w215h120/springer-static/image/art%3A10.1038%2Fs41598-026-44473-w/MediaObjects/41598_2026_44473_Fig1_HTML.png)

### [Multimodal generative adversarial networks for piano fingering correction and performance expressiveness modeling through audio-visual feature fusion](https://www.nature.com/articles/s41598-026-44473-w?fromPaywallRec=false)

Article Open access 26 March 2026

![](https://media.springernature.com/w215h120/springer-static/image/art%3A10.1038%2Fs41598-024-73810-0/MediaObjects/41598_2024_73810_Fig1_HTML.png)

### [Piano performance evaluation dataset with multilevel perceptual features](https://www.nature.com/articles/s41598-024-73810-0?fromPaywallRec=false)

Article Open access 03 October 2024

![](https://media.springernature.com/w215h120/springer-static/image/art%3Aplaceholder%2Fimages/placeholder-figure-nature.png)

### [Deep learning-based adaptive recommendation algorithm for personalized music teaching](https://www.nature.com/articles/s41598-026-63186-8?fromPaywallRec=false)

Article Open access 25 July 2026

### Explore related subjects

Discover the latest articles and news in related subjects.

*   [Engineering](https://www.nature.com/subjects/engineering)
    
*   [Mathematics and computing](https://www.nature.com/subjects/mathematics-and-computing)
    
*   [AI-Driven Music Generation Systems](https://www.nature.com/subjects/ai-driven-music-generation-systems)
    

Abbreviations
-------------

STFT:

Short-time fourier transform

CQT:

Constant-Q transform

MFCC:

Mel-frequency cepstral coefficients

CNN:

Convolutional neural network

LSTM:

Long short-term memory

GRU:

Gated recurrent unit

MSE:

Mean squared error

PCC:

Pearson correlation coefficient

SVR:

Support vector regression

BKT:

Bayesian knowledge tracing

DKT:

Deep knowledge tracing

IRT:

Item response theory

RL:

Reinforcement learning

PPO:

Proximal policy optimization

MFP:

Multi-granularity feature pyramid

CDA:

Cross-dimension attention

MTL:

Multi-task learning

MIDI:

Musical instrument digital interface

FFN:

Feed-forward network

ANOVA:

Analysis of variance

HSD:

Honestly significant difference

ICC:

Intra-class correlation coefficient

Funding
-------

This work was supported by 2024 Shanxi Provincial Higher Education Philosophy and Social Science Research Project, titled "Survey on the Current Status of Courses in Vocational Colleges and Research on Teaching Content".

Author information
------------------

### Authors and Affiliations

1.  Department of Music, Jinzhong Normal Junior College, Jinzhong, 030600, ShanXi, China
    
    Dongkui Wang
    
2.  College of Music, Myongji University, Yongin, Gyeonggi Province, 17092, Republic of Korea
    
    Yuqi Li
    

Authors

1.  Dongkui Wang
    
    [View author publications](https://www.nature.com/search?author=Dongkui%20Wang)
    
    Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Dongkui%20Wang)
     [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Dongkui%20Wang%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)
    
2.  Yuqi Li
    
    [View author publications](https://www.nature.com/search?author=Yuqi%20Li)
    
    Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Yuqi%20Li)
     [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Yuqi%20Li%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)
    

### Corresponding author

Correspondence to [Dongkui Wang](mailto:DK19303510011@163.com)
.

Ethics declarations
-------------------

### Competing interests

The authors declare no competing interests.

### Ethics approval and consent to participate

This study was approved by the Research Ethics Committee of Jinzhong Normal Junior College (Reference Number: IRB-2024-08173). The ethics committee reviewed the study protocol and classified the research as a minimal-risk educational technology evaluation rather than a clinical trial, as it involves no health-related intervention, no medical procedures, and no measurement of health outcomes. All 45 participants in the teaching experiment provided written informed consent prior to enrollment, which included clear descriptions of the study purpose, procedures, voluntary nature of participation, and the right to withdraw at any time without consequence. The study was conducted in accordance with the Declaration of Helsinki and relevant national regulations governing research involving human participants.

### Consent for publication

All authors have reviewed the manuscript and consent to its publication. No identifiable information regarding participants has been included.

Additional information
----------------------

### Publisher’s note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Rights and permissions
----------------------

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by-nc-nd/4.0/](http://creativecommons.org/licenses/by-nc-nd/4.0/)
.

[Reprints and permissions](https://s100.copyright.com/AppDispatchServlet?title=Multi-dimensional%20piano%20performance%20technique%20assessment%20and%20personalized%20teaching%20strategy%20generation%20based%20on%20deep%20learning&author=Dongkui%20Wang%20et%20al&contentID=10.1038%2Fs41598-026-72157-y&copyright=The%20Author%28s%29&publication=2045-2322&publicationDate=2026-09-30&publisherName=SpringerNature&orderBeanReset=true&oa=CC%20BY-NC-ND)

About this article
------------------

[![Check for updates. Verify currency and authenticity via CrossMark](<Base64-Image-Removed>)](https://crossmark.crossref.org/dialog/?doi=10.1038/s41598-026-72157-y)

### Cite this article

Wang, D., Li, Y. Multi-dimensional piano performance technique assessment and personalized teaching strategy generation based on deep learning. _Sci Rep_ (2026). https://doi.org/10.1038/s41598-026-72157-y

[Download citation](https://citation-needed.springer.com/v2/references/10.1038/s41598-026-72157-y?format=refman&flavour=citation)

*   Received: 26 February 2026
    
*   Accepted: 15 September 2026
    
*   Published: 30 September 2026
    
*   DOI: https://doi.org/10.1038/s41598-026-72157-y
    

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

*   [Piano performance assessment](https://www.nature.com/search?q=Piano%20performance%20assessment)
    
*   [Deep learning](https://www.nature.com/search?q=Deep%20learning)
    
*   [Multi-task learning](https://www.nature.com/search?q=Multi-task%20learning)
    
*   [Personalized teaching](https://www.nature.com/search?q=Personalized%20teaching)
    
*   [Adaptive learning path planning](https://www.nature.com/search?q=Adaptive%20learning%20path%20planning)
    
*   [Music education technology](https://www.nature.com/search?q=Music%20education%20technology)
    

Close banner Close

![Nature Briefing AI and Robotics](https://www.nature.com/static/images/logos/nature-briefing-ai-and-robotics-logo-2a1193ada7.svg)

Sign up for the _Nature Briefing: AI and Robotics_ newsletter — what matters in AI and robotics research, free to your inbox weekly.

      Email address

  Sign up

 I agree my information will be processed in accordance with the _Nature_ and Springer Nature Limited [Privacy Policy](https://www.nature.com/info/privacy)
.

Close banner Close

Get the most important science stories of the day, free in your inbox. [Sign up for Nature Briefing: AI and Robotics](https://www.nature.com/briefing/ai-and-robotics/?brieferEntryPoint=AIAndRoboticsBriefingBanner)