# English to Hangul

English sentence to naturally-sounding (augmented) Hangul notation.

  
## Installation
 
1. Download or clone this repository.
2. Type `make` in the root directory. (`sudo` required)

## How to Use

 * As a standalone program: `$ eng-to-hangul "<english-sentence-here>"`
 * As a Python package: `import eng_to_hangul`

## About Augmented Hangul

Augmented Hangul is **Hangul with annotation** to indicate the pronunciation that doesn't exist in Korean but does in English. There is no "standard" annotation, so I just invented it using my limited knowledge of linguistics and, of course, common sense. The purpose is to help native Korean speakers pronounce English better, or at least _recognizable_ to non-native Korean, _non-native English_ speakers.

<details>
  <summary>If you care to read more...</summary>
  
The basic philosophy behind this is, "We can only imagine just as much as we can describe." Because some sounds are lacking in Korean, native Korean speakers are particularly bad at some pronunciation to the point that non-Koreans may find it difficult to understand. This is (I think) because native Korean speakers cannot easily imagine how to pronounce those missing sounds, especially when combined with other speakable sounds (e.g., confusing 'v' with 'b' in the middle of words). We already have IPA symbols for that, but Koreans have a native toolset to "emulate" this function comfortably: Hangul. But this is also bad because many Koreans' "imagination" is limited to what Hangul can describe. By annotating some Hangul letters that are the closest Hangul could possibly have offered, any Hangul users may be able to "imagine" those lacking sounds and speak them better.

(TODO: what are those annotations?)
(TODO: what is a self-consonant?)

</details>

## TODO

 - Write "What is augmented Hangul?"
 - Translate the whole documentation in Korean.
 - Improve the handling of pronunciation variations.
 - Support the preferred ways of some pronunciations.
 - Package the repository more nicely. (Help needed!)
    - Installing non-`pip` dependencies (e.g., `python3-tk`, `python3-pil.imagetk`, and `UnDotum`)
    - Printing post-install messages after installation. (in `setup.py`)
    - Uploading this repository to a Python package manager.
