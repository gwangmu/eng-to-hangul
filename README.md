# English to Hangul

![sample_output](https://github.com/user-attachments/assets/dc1cfa83-eb2e-4f39-a6ff-da6bf3c954b0)

English sentence to naturally-sounding (augmented) Hangul notation.
  
## Installation
 
1. Download or clone this repository.
2. Type `make` in the root directory. (`sudo` required)

## How to Use

 * As a standalone program: `$ eng-to-hangul "<english-sentence-here>"`
 * As a Python package: `import eng_to_hangul`

## About Augmented Hangul

Augmented Hangul is **Hangul with annotation** to indicate the pronunciation that doesn't exist in Korean but does in English. There is no "standard" annotation, so I just invented it using my limited knowledge of linguistics and, of course, common sense. The purpose is to help native Korean speakers pronounce English better, or at least _recognizable_ to someone non-native in not only Korean but also _English_.

(TODO: what are those annotations? https://gwangmu.medium.com/extending-hangul-for-english-70e8be3fc6ef)

(TODO: what is a self-consonant?)

<details>
  <summary>If you care to read more...</summary>
  
The basic philosophy behind this is, "We can only imagine just as much as we can describe." Because some sounds are lacking in Korean, native Korean speakers are particularly bad at some pronunciation to the point that non-Koreans may find it difficult to understand. I imagine this is because they cannot "imagine" how to pronounce those missing sounds, especially when combined with other speakable sounds (e.g., consonant clusters). We already have IPA symbols to describe pronunciation, but Koreans have a native toolset to "emulate" this comfortably: Hangul. However, this is also why many Koreans' "imagination" stops in what Hangul can describe. 

My solution is to introduce **annotations and self-consonants** so that any Hangul user can "imagine" those lacking sounds and speak them better. Specifically, annotations will describe the missing sounds in Hangul (i.e., /f/, /v/, /z/, /r/, /θ/, and /ð/), and self-consonants will describe consonant clusters (e.g., al**ps** or **st**rike). They were deliberately designed to fit in the regular Hangul as seamlessly as possible so that people who had not heard of augmented Hangul could still read it roughly. For example, the annotated 'ㄸ' indicates /θ/, but clueless readers may simply ignore the annotation but still get the closest approximation (i.e., unannotated 'ㄸ').

<details>
  <summary>My two cents</summary>
  
The languages that use Latin alphabets (i.e., A to Z) routinely add annotations to the closest alphabets to describe their unique sounds, and for the letters that they _don't_ use, they just simply leave it in the Alphabet set so that they can use them to describe _other_ language pronunciation. I think Hangul can do this the other way around: we add annotations and a new concept (i.e., consonant clusters) to describe other language pronunciation and use regular Hangul letters to describe Korean as it's always been.

</details>

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
