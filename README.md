# 영문-한글 음역기

![sample_output](https://github.com/user-attachments/assets/dc1cfa83-eb2e-4f39-a6ff-da6bf3c954b0)

영문장에서 자연스럽게 들리는 (증강) 한글 표기로 음역.

## 증강 한글

증강 한글은 한국어에는 없지만 영어에는 존재하는 발음을 표기하기 위해 증강된 한글입니다. 현 한글에 "표준" 증강 한글은 없는 바, 이 프로젝트는 제한된 언어학과 상식을 동원해 자체 발명된 증강 한글을 이용합니다. 증강 한글은 한국어 원어민이 영어/한국어 **비**원어민이 알아들을 수 있는 발음을 구사하는 데 목적을 두고 있습니다.

### 분음부호 표기된 자음

한국어에 없는 발음을 표기하기 위헤 기존의 **가장 가까운** 자음 옆에 분음부호(예: ö 위의 점)를 붙입니다. 아래 표의 '종류'는 해당 자음에서 어떤 부분에 신경써야 하는 지를 의미합니다.

| 종류   	| Sound 	| Consonant                                                                               	| Example     | Explanation                    |
|--------	|-------	|-----------	                                                                              |-----------	|-------------                   |
| 입술    	| /v/   	| ![image](https://github.com/user-attachments/assets/0cbf93f6-a3b5-4e44-b3cf-4478054edfbc) | ![image](https://github.com/user-attachments/assets/2253aa94-ad86-4bc7-85bb-e8bc9fa09525) (**V**ery)      | 아랫 **입술**을 가볍게 물기. |
|        	| /f/   	| ![image](https://github.com/user-attachments/assets/81f56f07-5c2e-41f6-8931-816125a8b8d4) | ![image](https://github.com/user-attachments/assets/0c88cd99-abeb-4d70-83f1-cd203972ce2d) (Beauti**f**ul) | 아랫 **입술**을 가볍게 물기. |
| 혀    	| /r/   	| ![image](https://github.com/user-attachments/assets/e0d3a86d-8d4b-4d75-b06a-e628912ae4ac) | ![image](https://github.com/user-attachments/assets/2a5f9a45-9019-4c64-91ed-68e58f8c4964) (**R**oom)      | **혀**를 말기.            |
|        	| /θ/   	| ![image](https://github.com/user-attachments/assets/bcf3ffcb-10be-4147-94e0-7140f6f693f6)	| ![image](https://github.com/user-attachments/assets/7941149e-79e2-4c9c-b4b6-720cc393aab3) (**Th**e)       | **혀**를 가볍게 물기.      |
|        	| /ð/   	| ![image](https://github.com/user-attachments/assets/0187de51-973c-4819-986a-b1255a892d63) | ![image](https://github.com/user-attachments/assets/2f56d68b-159b-4e55-8c7d-a0e4f63f354c) (Wi**th**out)   | **혀**를 가볍게 물기.      |
| 강조   	| /z/   	| ![image](https://github.com/user-attachments/assets/da010c74-3779-4a8a-9b42-4931c52689d2)	| ![image](https://github.com/user-attachments/assets/eaba1bce-df31-4c07-a42e-8272b597189d) (**Z**one)      | 'ㅅ' 을 **강조**하기.      |

### 홀자음

홀자음은 **모음이 없는 자음**입니다. 모음 없는 자음에 익숙하지 않은 경우, 모음 'ㅡ'가 있다고 가정하되 최대한 'ㅡ' 발음을 짧게하고, 자음에서 필요로 하지 않는 한 성대를 쓰지 않도록 합니다.

| Example | IPA Pronunciation | Regular Hangul Equivalent |
|---------|-------------------|---------------------------|
| ![image](https://github.com/user-attachments/assets/0c981773-d7bd-4541-9148-55d835bef5e7) | [ðɪs]    | 디스      |
| ![image](https://github.com/user-attachments/assets/0fe76b9d-4ea3-45d9-982f-0efdebbadd58) | [teɪk]   | 테이크    |
| ![image](https://github.com/user-attachments/assets/595ddcc9-1f00-4a7e-9a1c-a3a228f69fda) | [fraɪz]  | 프롸이즈   |
| ![image](https://github.com/user-attachments/assets/cda0479f-c564-424c-9205-bc456c1831ff) | [straɪk] | 스트롸이크 |

<details>
  <summary>If you care to read more...</summary>

### 동기

이 프로젝트의 기본 철학은 "묘사할 수 있는 만큼 상상할 수 있다"입니다.

한국어 원어민이라면 흔히 한국어에는 없는 영어를 발음하는데 어려움을 겪습니다. 심한 경우 이는 한국어 비원어민이 알아듣기 힘든 발음 문제로 이어지는데, 이는 한국인이 해당 발음을 "상상하기 힘들다"는 점에서 비롯됩니다 (예: 자음 클러스터 - 모음 없는 자음들의 묶음). 특히 발음을 "한글"로 상상하는 경향이 있는 한국어 원어민들에게는 한글로 묘사할 수 있는 발음의 한계만큼 발음할 수 있게됩니다.

이 문제에 대한 제 해결책은 기존 한글에 **분음부호와 홀자음**을 추가해 한글 사용자가 한국어에는 없는 발음들을 "상상할 수 있도록" 만들자는 것입니다. 분음부호는 한글에 없는 발음(/f/, /v/, /z/, /r/, /θ/, and /ð/)을 위해, 홀자음은 한국어에 없는 자음 클러스터를 묘사하기 위해 사용될 수 있습니다. 분음부호와 홀자음은 증강된 한글에 익숙하지 않은 한글 사용자들도 쉽게 이해하고 읽을 수 있도록 의도적으로 추가되었습니다. 예를 들어, 분음부호가 붙은 'ㄸ'은 음가 /θ/를 갖지만 분음부호를 무시하고도 /θ/에 가장 근사한 발음인 'ㄸ'으로 해석될 수 있습니다.

### My Two-cents
  
The languages that use Latin alphabets (i.e., A to Z) routinely add diacritic marks to the closest alphabets to describe their unique sounds, and for the letters that they _don't_ use, they just simply leave it in the Alphabet set so that they can use them to describe _other_ language pronunciation. I think Hangul can do this the other way around: we add diacritic marks and a new concept (i.e., consonant clusters) to describe other language pronunciation and use regular Hangul letters to describe Korean as it's always been.

[This](https://gwangmu.medium.com/extending-hangul-for-english-70e8be3fc6ef) was written when I first thought about augmented Hangul, though at that point, I thought /z/ doesn't need to be thoroughly described in Hangul so I ruled out /z/ out of question. Full disclosure: I was wrong.

</details>
  
## 설치
 
1. 이 레포지토리(저장소, repository)를 다운로드 혹은 클론.
2. 터미널에서 레포지토리 디렉토리로 이동한 후 `sudo make`를 입력.
3. (우분투 유저) 의존성 설치를 위해 레포지토리 디렉토리에서 `sudo make dep-ubuntu`를 입력.

## 사용법

 * 자체 프로그램으로: `$ eng-to-hangul "<english-sentence-here>"`
 * Python 패키지로: `import eng_to_hangul`

<details>
  <summary>옵션 및 상세</summary>
  
 * 자체 프로그램 옵션
    * `-f <filename>`: `<filename>` 파일에서 읽은 후 한 줄씩 음역.
    * `-D`: 결과를 GUI에 그리지 않고 터미널에만 출력.
    * `-o <filename>`: 결과를 `<filename>`에 저장 (기본값: 화면).
    * `-s`: 표준 한글 표기로 결과 생성.
    * `-M`: 분음부호 끄기.
    * `-C`: 홀자음에 모음 'ㅡ'을 덧붙임.
    * `-r`: 가능한 모든 발음을 결과로 받기.
 * Python 패키지
    * (향후 추가 예정)

</details>

## Notes

 * 이 프로젝트는 영문에서 IPA 표기로 음역을 위해 @mphilli가 개발한 [`eng-to-ipa`](https://github.com/mphilli/English-to-IPA)을 사용합니다.
 * 이 프로젝트를 사용하시는 경우 프로젝트 개발자에게 귀띔주시거나 프로젝트 링크를 남겨주실 것을 부탁합니다.
 * 제안이나 기여는 언제든 환영합니다. *분노/비방/폭언*은 자연스럽게 무시됨과 동시에 개발자로부터 3대에 걸친 저주를 받을 예정입니다.

<details>
  <summary>Click here for English</summary>

# English to Hangul

![sample_output](https://github.com/user-attachments/assets/dc1cfa83-eb2e-4f39-a6ff-da6bf3c954b0)

English sentence to naturally-sounding (augmented) Hangul notation.

## About Augmented Hangul

Augmented Hangul is an augmented Hangul for pronunciation that doesn't exist in Korean but does exist in English. Since there is no "standard" augmentation, this project invented it using limited knowledge of linguistics and, of course, common sense. The purpose is to help native Korean speakers pronounce English better, or at least _recognizable_ to someone non-native in not only Korean but also _English_.

### Consonants with Diacritical Marks

The diacritical marks were purposefully added to the closest Hangul consonants. The class suggests what needs attention.

| Class  	| Sound 	| Consonant                                                                               	| Example     | Explanation                    |
|--------	|-------	|-----------	                                                                              |-----------	|-------------                   |
| Lip    	| /v/   	| ![image](https://github.com/user-attachments/assets/0cbf93f6-a3b5-4e44-b3cf-4478054edfbc) | ![image](https://github.com/user-attachments/assets/2253aa94-ad86-4bc7-85bb-e8bc9fa09525) (**V**ery)      | Softly bite the lower **lip**. |
|        	| /f/   	| ![image](https://github.com/user-attachments/assets/81f56f07-5c2e-41f6-8931-816125a8b8d4) | ![image](https://github.com/user-attachments/assets/0c88cd99-abeb-4d70-83f1-cd203972ce2d) (Beauti**f**ul) | Softly bite the lower **lip**. |
| Tongue 	| /r/   	| ![image](https://github.com/user-attachments/assets/e0d3a86d-8d4b-4d75-b06a-e628912ae4ac) | ![image](https://github.com/user-attachments/assets/2a5f9a45-9019-4c64-91ed-68e58f8c4964) (**R**oom)      | Roll your **tongue**.          |
|        	| /θ/   	| ![image](https://github.com/user-attachments/assets/bcf3ffcb-10be-4147-94e0-7140f6f693f6)	| ![image](https://github.com/user-attachments/assets/7941149e-79e2-4c9c-b4b6-720cc393aab3) (**Th**e)       | Softly bite your **tongue**.   |
|        	| /ð/   	| ![image](https://github.com/user-attachments/assets/0187de51-973c-4819-986a-b1255a892d63) | ![image](https://github.com/user-attachments/assets/2f56d68b-159b-4e55-8c7d-a0e4f63f354c) (Wi**th**out)   | Softly bite your **tongue**.   |
| Stress 	| /z/   	| ![image](https://github.com/user-attachments/assets/da010c74-3779-4a8a-9b42-4931c52689d2)	| ![image](https://github.com/user-attachments/assets/eaba1bce-df31-4c07-a42e-8272b597189d) (**Z**one)      | **Stress** 'ㅅ'.                |

### Self-consonants

Self-consonants are simply **consonants without a vowel**. If you're unfamiliar with this concept, add 'ㅡ' but speak it very shortly, or don't use your vocal cord unless the consonant requires it.

| Example | IPA Pronunciation | Regular Hangul Equivalent |
|---------|-------------------|---------------------------|
| ![image](https://github.com/user-attachments/assets/0c981773-d7bd-4541-9148-55d835bef5e7) | [ðɪs]    | 디스      |
| ![image](https://github.com/user-attachments/assets/0fe76b9d-4ea3-45d9-982f-0efdebbadd58) | [teɪk]   | 테이크    |
| ![image](https://github.com/user-attachments/assets/595ddcc9-1f00-4a7e-9a1c-a3a228f69fda) | [fraɪz]  | 프롸이즈   |
| ![image](https://github.com/user-attachments/assets/cda0479f-c564-424c-9205-bc456c1831ff) | [straɪk] | 스트롸이크 |

<details>
  <summary>If you care to read more...</summary>

### Motivation

The basic philosophy behind this is, "We can only imagine just as much as we can describe." 

Because some pronunciation is lacking in Korean, native Korean speakers are particularly bad at some pronunciation, so much so that non-Koreans may find it difficult to understand. I reckon this is because they cannot "imagine" how to pronounce those lacking pronunciation, such as consonant clusters. To make matters a little worse, native Koreans tend to use Hangul to "emulate" any sounds because Hangul is excellent at it. The only problem is that some of the pronunciation is lacking in Hangul, which makes Koreans' "imagination" stop there. 

My solution is introducing **diacritical marks and self-consonants** so that any Hangul user can "imagine" those lacking sounds and speak them better. Specifically, diacritical marks will describe the missing sounds in Hangul (i.e., /f/, /v/, /z/, /r/, /θ/, and /ð/), and self-consonants will describe consonant clusters (e.g., al**ps** or **st**rike). They were deliberately designed to fit in the regular Hangul as seamlessly as possible so that people who had not heard of augmented Hangul could still read it roughly. For example, the 'ㄸ' with a diacritical mark indicates /θ/, but clueless readers may simply ignore the diacritical marks but still get the closest approximation (i.e., 'ㄸ').

### My Two-cents
  
The languages that use Latin alphabets (i.e., A to Z) routinely add diacritical marks to the closest alphabets to describe their unique sounds, and for the letters that they _don't_ use, they just simply leave it in the Alphabet set so that they can use them to describe _other_ language pronunciation. I think Hangul can do this the other way around: we add diacritical marks and a new concept (i.e., consonant clusters) to describe other language pronunciation and use regular Hangul letters to describe Korean as it's always been.

[This](https://gwangmu.medium.com/extending-hangul-for-english-70e8be3fc6ef) was written when I first thought about augmented Hangul, though at that point, I thought /z/ doesn't need to be thoroughly described in Hangul so I ruled out /z/ from the list. Full disclosure: I was wrong.

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
    * `-A`: Turn off diacritical marks.
    * `-C`: Turn off self consonants. Self-consonants will be assigned with 'ㅡ.'
    * `-r`: Retrieve every possible pronunciation.
 * For the Python package
    * (Details to be added)

</details>

## Notes

 * `eng-to-hangul` uses [`eng-to-ipa`](https://github.com/mphilli/English-to-IPA) from @mphilli for English-to-IPA transliteration.
 * It is not mandatory, but please let me know or leave a link to this repository if you use this.
 * Contributions and suggestions are always welcome 🙂, but please try to be *constructive*. Ranters will get cursed for the next three generations.

</details>
<details>
  <summary>Technical TODOs</summary>
  
 - Translate the whole documentation in Korean.
 - Improve the handling of pronunciation variations.
 - Support the preferred ways of some pronunciations.
 - Package the repository more nicely. (Help needed!)
    - Installing non-`pip` dependencies (e.g., `python3-tk`, `python3-pil.imagetk`, and `UnDotum`)
    - Printing post-install messages after installation. (in `setup.py`)
    - Uploading this repository to a Python package manager.
 - Provide a friendlier interface to non-terminal or non-Linux users.
 - Support drawing regular Hangul sentences.

</details>
