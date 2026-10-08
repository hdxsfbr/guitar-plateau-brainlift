<!--
url: https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists
title: Fretwork: An Open-Source Music Intelligence Platform for Guitarists
query: Spotify Basic Pitch GuitarSet transcription accuracy study
fetched: 2026-10-08T02:23:35.314Z
-->

[Skip to main content](https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists#main-content)

*   [](https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists#)
    [About](https://www.ischool.berkeley.edu/about)
     ►
*   [](https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists#)
    [Programs](https://www.ischool.berkeley.edu/programs)
     ►
*   [](https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists#)
    [Courses](https://www.ischool.berkeley.edu/courses)
     ►
*   [](https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists#)
    [People](https://www.ischool.berkeley.edu/people)
     ►
*   [](https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists#)
    [Research](https://www.ischool.berkeley.edu/research)
     ►
*   [](https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists#)
    [Careers](https://www.ischool.berkeley.edu/careers)
     ►
*   [](https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists#)
    [News](https://www.ischool.berkeley.edu/news)
     ►
*   [](https://www.ischool.berkeley.edu/programs/mids/capstone/2026b-summer/fretwork-open-source-music-intelligence-platform-guitarists#)
    [Events](https://www.ischool.berkeley.edu/events)
     ►
*    
    
     Submit
    
*   [UC Berkeley](http://www.berkeley.edu/)
    
*   [Give](https://www.ischool.berkeley.edu/give)
    
*   [Volunteer](https://www.ischool.berkeley.edu/volunteer)
    
*   [Contact Us](https://www.ischool.berkeley.edu/about/contactus)
    
*   [Alumni](https://www.ischool.berkeley.edu/alumni)
    
*   [Log in](https://www.ischool.berkeley.edu/user/login)
    

MIDS Capstone Project Summer 2026

Fretwork: An Open-Source Music Intelligence Platform for Guitarists
===================================================================

Team members

[Ani Sreekumar](https://www.ischool.berkeley.edu/people/ani-sreekumar)

[Zev Rosen](https://www.ischool.berkeley.edu/people/zev-rosen)

[Aaron Luong](https://www.ischool.berkeley.edu/people/aaron-luong)

[Kobby Hanson](https://www.ischool.berkeley.edu/people/kobby-hanson)

### Problem & Motivation

Existing AI music transcription tools fail to translate audio into playable patterns on the guitar. _Fretwork_ produces output that you could actually hand to a musician.

Guitarists place their fingers on different _frets,_ spaces between metal dividers on each guitar string, to play notes. There are many different finger placements which produce the same note, but some finger placements are more efficient and easy to play, while some are overly complicated and don't make sense in the context of the song or prior finger placements. _Tablature ("tab") is_ a music notation format that specifies exactly which string to play and which positions to fret . Existing AI music transcription tools produce tabs which guitarists say don't make sense. _Fretwork_ changes that by producing playable _tablature_ which guitarists can actually use to learn a song.

_Fretwork_ produces an end-to-end solution that works: given any guitar audio recording, it produces accurate, guitarist-friendly tablature through a user-friendly web UI.

### Data Sources & Data Science Approach

We use two complementary datasets:

*   **GuitarSet** (360 recordings, 6 players): paired guitar audio with ground-truth string/fret assignments. Used to evaluate our model.
*   **DadaGP** (26,000 songs, 42 million notes in tab format): a large reference of guitar tablature unconnected to audio. This dataset supplements our base model to give it a more expansive library of common finger patterns across genres and difficulty levels.

The data science pipeline involves four steps, which all run in parallel to produce tablature from raw audio files:

1.  **Pitch Detection** — Spotify's Basic Pitch model converts audio to musical notes. We tuned detection thresholds and applied post-processing techniques to correct the most common pitch error type: notes that are one semitone off from the detected key.
2.  **Context Detection** — Relies on existing Python libraries to determine the key, tempo, and chords which make up the song. These serve as additional inputs which inform fret assignment.
3.  **Fretboard Algorithm** — Goes from notes and context to strings and frets — this step separates our product from other tools. Our algorithm involves several elements which we combine to produce playable tablature:
    1.  _Viterbi decoder_\-a method used to find the most likely sequence of events, applied to fret assignments 
    2.  _CAGED-box space_\-guitarists use a box on the fretboard to identify the common C, A, G, E, and D open chords anywhere on the fretboard. Our fret output falls within this space.
    3.  A cost for physical distance travelled on the fretboard
    4.  Tendency towards a set of manually inputted common chord shapes and fret patterns found in DadaGP.
    5.  A transformer model that predicts each note's placement given the previous 64 notes' pitches, fingerings, and chord boundaries.
4.  **Output Rendering** — Results are shown to the user as standard musical notation + tablature, with options to switch formats to interactive HTML or raw ASCII.

### Evaluation

We evaluate using leave-one-player-out cross-validation (LOOCV) on GuitarSet, ensuring no player appears in both training and test data on two metrics:

1.  **F1 Score**: combines precision and recall into a single value which measures model performance. A correct fret output is defined as the pitch, string, and fret all matching GuitarSet.
2.  **Adjusted F1 Score**: Allows a fret to be considered correct when the pitch is within one semitone.

Starting from a baseline of ~0.42 full-pipeline F1 with a greedy algorithm that evaluates each note independently, our CAGED + voicing algorithm reached 0.54. Adding the DadaGP position prior pushed this to 0.72, and a transformer sequence model trained on DadaGP brought the final result to 0.77. The near-match F1 of 0.78 reveals that the fretboard assignment itself is largely correct; the main bottleneck is pitch detection, not our algorithm.

### Key Learnings & Impact

The key learning was that combining information from multiple datasets and techniques was critical to algorithm performance. Adding DadaGP to give our model a reference of common tabs improved our model's performance beyond what was previously possible on GuitarSet. The GuitarSet data only consisted of 6 players, who tended to play low frets, which biased our algorithm. The success of our transformer model showed the musical context matters when determining fretboard assignment: knowing previous positions helps determine the next position.

Additionally, we learned that there are several limitations to fretboard algorithm performance which are not easily solved. The main factor which limits our model's performance is the pitch detection, for which we are constrained by Spotify's Basic Pitch pitch detection algorithm. We tried several manual techniques to try to eliminate falsely detected notes, which often backfired and worsened our algorithm's performance.

Fretwork produces output that existing tools can't: playable, physically comfortable tab that guitarists can actually use to learn a song.

### Acknowledgements

We would like to thank our instructors, Puya Vahabi and Fred Nugen, as well as our classmates, for their invaluable support and guidance throughout our project. We use Spotify's Basic Pitch for audio-to-MIDI transcription, the GuitarSet for model training and evaluation, and DadaGP dataset to teach our model common tabs. Standard notation rendering is powered by AlphaTab.

Course
------

[Data Science 210. Capstone](https://www.ischool.berkeley.edu/courses/datasci/210) , Summer 2026

[Class Project Gallery](https://www.ischool.berkeley.edu/courses/project-gallery/284/2/2026)

More Information
----------------

[Project Website](https://guitar-capstone.kobbyhanson.workers.dev/)

[GitHub Repository](https://github.com/kxnghans/guitar-capstone)

[Project Slides](https://docs.google.com/presentation/d/1gO9UxpEttxY1NtAMq2saIJ5KK9FaZ-er/edit?slide=id.p1#slide=id.p1)

[![Interactive Music-Intelligence Platform](https://www.ischool.berkeley.edu/sites/default/files/styles/sidebar/public/2026-07/screenshot-2026-06-01-at-9.37.53-pm.png?itok=H_-95O1K)](https://www.ischool.berkeley.edu/sites/default/files/styles/fullscreen/public/2026-07/screenshot-2026-06-01-at-9.37.53-pm.png?itok=TlYN7W38 "Interactive Music-Intelligence Platform")

Video
-----

Remote video URL

Last updated: August 9, 2026