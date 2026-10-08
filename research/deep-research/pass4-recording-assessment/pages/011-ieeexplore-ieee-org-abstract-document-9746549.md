<!--
url: https://ieeexplore.ieee.org/abstract/document/9746549/
title: A lightweight instrument-agnostic model for polyphonic note transcription and multipitch estimation
query: NMP Basic Pitch GuitarSet F-measure
fetched: 2026-10-08T02:24:08.773Z
-->

Opens in a new window Opens an external website Opens an external website in a new window

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. [Privacy Policy](https://www.ieee.org/security-privacy.html)

Accept Deny Non-Essential

Storage Preferences

Loading \[MathJax\]/extensions/TeX/noUndefined.js

Skip to main content

   A Lightweight Instrument-Agnostic Model for Polyphonic Note Transcription and Multipitch Estimation | IEEE Conference Publication | IEEE Xplore      

[](https://ieeexplore.ieee.org/abstract/document/)

[](https://ieeexplore.ieee.org/rest/api/hpdata)

  

Skip to Main Content

A Lightweight Instrument-Agnostic Model for Polyphonic Note Transcription and Multipitch Estimation
===================================================================================================

Publisher: IEEE

Cite This

[PDF](javascript:void() "You do not have access to this PDF")

[Rachel M. Bittner](https://ieeexplore.ieee.org/author/37085587390)
; [Juan José Bosch](https://ieeexplore.ieee.org/author/37086772346)
; [David Rubinstein](https://ieeexplore.ieee.org/author/37089469117)
; [Gabriel Meseguer-Brocal](https://ieeexplore.ieee.org/author/37089471631)
; [Sebastian Ewert](https://ieeexplore.ieee.org/author/37395527500)

[All Authors](javascript:void())

Sign In or Purchase

48

Cites in

Papers

1

Cites in

Patent

1885

Full

Text Views

*   [](javascript:void())
    
*   [](javascript:void())
    
*   [](javascript:void())
    
*   [Alerts](javascript:void())
    
    [Manage Content Alerts](https://ieeexplore.ieee.org/alerts/citation)
    
    [Add to Citation Alerts](javascript:void())
    

* * *

*   Download PDF
*   [Download References](javascript:void())
    
*   Request Permissions
*   Save to
*   Alerts

Abstract:
---------

Automatic Music Transcription (AMT) has been recognized as a key enabling technology with a wide range of applications. Given the task’s complexity, best results have typ...Show More

Metadata
--------

Abstract:
---------

Automatic Music Transcription (AMT) has been recognized as a key enabling technology with a wide range of applications. Given the task’s complexity, best results have typically been reported for systems focusing on specific settings, e.g. instrument-specific systems tend to yield improved results over instrument-agnostic methods. Similarly, higher accuracy can be obtained when only estimating frame-wise f0 values and neglecting the harder note event detection. Despite their high accuracy, such specialized systems often cannot be deployed in the real-world. Storage and network constraints prohibit the use of multiple specialized models, while memory and run-time constraints limit their complexity. In this paper, we propose a lightweight neural network for musical instrument transcription, which supports polyphonic outputs and generalizes to a wide variety of instruments (including vocals). Our model is trained to jointly predict frame-wise onsets, multipitch and note activations, and we experimentally show that this multi-output structure improves the resulting frame-level note accuracy. Despite its simplicity, benchmark results show our system’s note estimation to be substantially better than a comparable baseline, and its frame-level accuracy to be only marginally below those of specialized state-of-the-art AMT systems. With this work we hope to encourage the community to further investigate low-resource, instrument-agnostic AMT systems.

**Published in:** [ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)](https://ieeexplore.ieee.org/xpl/conhome/9745891/proceeding)

**Date of Conference:** 23-27 May 2022

**Date Added to IEEE _Xplore_:** 27 April 2022

ISBN Information:

ISSN Information:

**DOI:** [10.1109/ICASSP43922.2022.9746549](https://doi.org/10.1109/ICASSP43922.2022.9746549)

Publisher: IEEE

**Conference Location:** Singapore, Singapore

 ![](https://ieeexplore.ieee.org/assets/img/document/toc-icon.png) Contents

* * *

### 1\. Introduction

The automatic transcription of music has been studied for more than four decades \[1\]. During this time, systems have considerably improved, in particular since the rise of deep learning. Yet, the task remains unsolved, partially due to various intrinsic challenges \[1\] but also due to a lack of an objective ground truth on which humans consistently agree \[2\]. Because of the intrinsic difficulty of the task, AMT systems are usually designed with a limited scope, and focus on a sub-task. There are a number of common sub-tasks in AMT which branch along three dimensions: (1) the degree of output polyphony (monophonic, polyphonic) (2) the types of output to be estimated (notes, f0), and (3) the type of input audio (pop songs, solo piano, solo guitar, jazz ensembles, etc.). For example, specializing for a specific instrument class allows models to exploit instrument-specific characteristics to increase the transcription accuracy, e.g. piano \[3\]–\[5\], guitar \[6\],\[7\] or singing voice \[8\],\[9\]. Similarly, models built to estimate a particular output type, or which are restricted to monophonic settings \[10\] can further increase accuracy in these scenarios. In many real-world applications, deploying a number of specialized systems becomes intractable, for example because of storage, network and maintenance constraints. Further, for many instruments it is challenging to create a dataset large enough to train modern methods. Applications can also add additional restrictions w.r.t. the size of the model, its (peak) memory consumption and run-time. Therefore, there is often a gap between the latest published state of the art and models that can practically be deployed in a range of settings.

Sign in to Continue Reading

Authors


-----------

Figures


-----------

References


--------------

Citations


-------------

Keywords


------------

Metrics


-----------

Footnotes


-------------

[![Contact IEEE to Subscribe](https://ieeexplore.ieee.org/assets/img/document/ads/ft-subscription.png)](https://innovate.ieee.org/interested-in-a-subscription-for-your-organization/?LT=XPLLG_XPL_2020_SUB_Conferences300x250_Sub-NFT)

More Like This
--------------

[Signal Processing of Images for Convective Boundary Layer Height Estimation From Radar (SPICER) and Multi-Instrument Verification](https://ieeexplore.ieee.org/document/10839448/)

IEEE Transactions on Geoscience and Remote Sensing

Published: 2025

[Fundamental frequency estimation for music signals with modified Hilbert-Huang transform (HHT)](https://ieeexplore.ieee.org/document/5202503/)

2009 IEEE International Conference on Multimedia and Expo

Published: 2009

[Show More](javascript:void())

**References is not available for this document.**

### IEEE Account

*   [Change Username/Password](https://www.ieee.org/profile/changeusrpwd/showChangeUsrPwdPage.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
    
*   [Update Address](https://www.ieee.org/profile/address/getAddrInfoPage.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
    

### Purchase Details

*   [Payment Options](https://www.ieee.org/profile/payment/showPaymentHome.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
    
*   [Order History](https://www.ieee.org/profile/vieworder/showOrderHistory.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
    
*   [View Purchased Documents](https://ieeexplore.ieee.org/articleSale/purchaseHistory.jsp)
    

### Profile Information

*   [Communications Preferences](https://www.ieee.org/ieee-privacyportal/app/ibp?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
    
*   [Profession and Education](https://www.ieee.org/profile/profedu/getProfEduInformation.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
    
*   [Technical Interests](https://www.ieee.org/profile/tips/getTipsInfo.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore)
    

### Need Help?

*   **US & Canada:** +1 800 678 4333
*   **Worldwide:** +1 732 981 0060  
    
*   [Contact & Support](https://ieeexplore.ieee.org/xpl/contact)
    

*   [About IEEE _Xplore_](https://ieeexplore.ieee.org/Xplorehelp/overview-of-ieee-xplore/about-ieee-xplore)
    
*   [Contact Us](https://ieeexplore.ieee.org/xpl/contact)
    
*   [Help](https://ieeexplore.ieee.org/Xplorehelp)
    
*   [Accessibility](https://ieeexplore.ieee.org/Xplorehelp/overview-of-ieee-xplore/accessibility-statement)
    
*   [Terms of Use](https://ieeexplore.ieee.org/Xplorehelp/overview-of-ieee-xplore/terms-of-use)
    
*   [Nondiscrimination Policy](http://www.ieee.org/web/aboutus/whatis/policies/p9-26.html)
    
*   [Sitemap](https://ieeexplore.ieee.org/xpl/sitemap.jsp)
    
*   [Privacy & Opting Out of Cookies](http://www.ieee.org/about/help/security_privacy.html)
    

A not-for-profit organization, IEEE is the world's largest technical professional organization dedicated to advancing technology for the benefit of humanity.  
© Copyright 2026 IEEE - All rights reserved. Use of this web site signifies your agreement to the terms and conditions.