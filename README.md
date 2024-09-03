# English to Hangul

![sample_output](https://github.com/user-attachments/assets/dc1cfa83-eb2e-4f39-a6ff-da6bf3c954b0)

English sentence to naturally-sounding (augmented) Hangul notation.

## About Augmented Hangul

Augmented Hangul is **Hangul with annotation** to indicate the pronunciation that doesn't exist in Korean but does in English. There is no "standard" annotation, so I just invented it using my limited knowledge of linguistics and, of course, common sense. The purpose is to help native Korean speakers pronounce English better, or at least _recognizable_ to someone non-native in not only Korean but also _English_.

### Annotated Consonants

The annotation was purposefully added to the closest Hangul consonants. The class suggests what needs attention.

| Class  	| Sound 	| Consonant                                                                               	| Example     | Explanation                    |
|--------	|-------	|-----------	                                                                              |-----------	|-------------                   |
| Lip    	| /v/   	| ![image](https://github.com/user-attachments/assets/0cbf93f6-a3b5-4e44-b3cf-4478054edfbc) | ![image](https://github.com/user-attachments/assets/2253aa94-ad86-4bc7-85bb-e8bc9fa09525) (**V**ery) | Softly bite the lower **lip**. |
|        	| /f/   	| ![image](https://github.com/user-attachments/assets/81f56f07-5c2e-41f6-8931-816125a8b8d4) |             | Softly bite the lower **lip**. |
| Tongue 	| /r/   	| ![image](https://github.com/user-attachments/assets/e0d3a86d-8d4b-4d75-b06a-e628912ae4ac) |             | Roll your **tongue**.          |
|        	| /θ/   	| ![image](https://github.com/user-attachments/assets/bcf3ffcb-10be-4147-94e0-7140f6f693f6)	|             | Softly bite your **tongue**.   |
|        	| /ð/   	| ![image](https://github.com/user-attachments/assets/0187de51-973c-4819-986a-b1255a892d63) |             | Softly bite your **tongue**.   |
| Stress 	| /z/   	| ![image](https://github.com/user-attachments/assets/da010c74-3779-4a8a-9b42-4931c52689d2)	|             | **Stress** 'ㅅ'.                |

### Self-consonants

Self-consonants are simply **consonants without a vowel**. If you're unfamiliar with this concept, add 'ㅡ' but speak it very shortly, or don't use your vocal cord unless the consonant requires it.

| Example     | IPA Pronunciation | Regular Hangul Equivalent | Explanation |
|-------------|-------------------|---------------------------|-------------|
|             |                   |                           |             |

<details>
  <summary>If you care to read more...</summary>

### Motivation

The basic philosophy behind this is, "We can only imagine just as much as we can describe." 

Because some pronunciation is lacking in Korean, native Korean speakers are particularly bad at some pronunciation, so much so that non-Koreans may find it difficult to understand. I reckon this is because they cannot "imagine" how to pronounce those lacking pronunciation, especially when combined with other speakable sounds (e.g., consonant clusters). To make matters a little worse, native Koreans tend to use Hangul to "emulate" any sounds because Hangul is excellent at it. The only problem is that some of the pronunciation is lacking in Hangul, which makes Koreans' "imagination" stop there. 

My solution is to introduce **annotations and self-consonants** so that any Hangul user can "imagine" those lacking sounds and speak them better. Specifically, annotations will describe the missing sounds in Hangul (i.e., /f/, /v/, /z/, /r/, /θ/, and /ð/), and self-consonants will describe consonant clusters (e.g., al**ps** or **st**rike). They were deliberately designed to fit in the regular Hangul as seamlessly as possible so that people who had not heard of augmented Hangul could still read it roughly. For example, the annotated 'ㄸ' indicates /θ/, but clueless readers may simply ignore the annotation but still get the closest approximation (i.e., unannotated 'ㄸ').

### My Two-cents
  
The languages that use Latin alphabets (i.e., A to Z) routinely add annotations to the closest alphabets to describe their unique sounds, and for the letters that they _don't_ use, they just simply leave it in the Alphabet set so that they can use them to describe _other_ language pronunciation. I think Hangul can do this the other way around: we add annotations and a new concept (i.e., consonant clusters) to describe other language pronunciation and use regular Hangul letters to describe Korean as it's always been.

[This](https://gwangmu.medium.com/extending-hangul-for-english-70e8be3fc6ef) was written when I first thought about augmented Hangul, though at that point, I thought /z/ doesn't need to be thoroughly described in Hangul so I ruled out /z/ from the annotation list. Full disclosure: it was.

</details>
  
## Installation
 
1. Download or clone this repository.
2. Type `sudo make` in the root directory.
3. (For Ubuntu users) Type `sudo make dep-ubuntu` in the root directory to install dependencies.

## How to Use

 * As a standalone program: `$ eng-to-hangul "<english-sentence-here>"`
 * As a Python package: `import eng_to_hangul`

<details>
  <summary>Options and details</summary>
  
 * For the standalone program
    * `-f <filename>`: Read from `<filename>` and convert it line by line.
    * `-D`: Don't draw the Hangul sentence. Output only in the terminal.
    * `-o <filename>`: Print the output to `<filename>` (if empty, on the screen).
    * `-s`: Print in the regular Hangul.
    * `-A`: Turn off annotations.
    * `-C`: Turn off self consonants. Self-consonants will be assigned with 'ㅡ.'
    * `-r`: Retrieve every possible pronunciation.
 * For the Python package
    * (Details to be added)

</details>

## Notes

 * `eng-to-hangul` uses [`eng-to-ipa`](https://github.com/mphilli/English-to-IPA) from @mphilli for English-to-IPA transliteration.
 * It is not mandatory, but please let me know or leave a link to this repository if you use this.


<details>
  <summary>Technical TODOs</summary>
  
 - Write "What is augmented Hangul?"
 - Translate the whole documentation in Korean.
 - Improve the handling of pronunciation variations.
 - Support the preferred ways of some pronunciations.
 - Package the repository more nicely. (Help needed!)
    - Installing non-`pip` dependencies (e.g., `python3-tk`, `python3-pil.imagetk`, and `UnDotum`)
    - Printing post-install messages after installation. (in `setup.py`)
    - Uploading this repository to a Python package manager.
 - Provide a friendlier interface to non-terminal or non-Linux users.
 - Draw the original English sentence below Hangul.
 - Support drawing regular Hangul sentences.
 - Support annotations for final consonants.

</details>
