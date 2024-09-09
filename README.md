
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

| Example | IPA Pronunciation | Standard Hangul Equivalent |
|---------|-------------------|----------------------------|
| ![image](https://github.com/user-attachments/assets/0c981773-d7bd-4541-9148-55d835bef5e7) | [ðɪs]    | 디스      |
| ![image](https://github.com/user-attachments/assets/0fe76b9d-4ea3-45d9-982f-0efdebbadd58) | [teɪk]   | 테이크    |
| ![image](https://github.com/user-attachments/assets/595ddcc9-1f00-4a7e-9a1c-a3a228f69fda) | [fraɪz]  | 프롸이즈   |
| ![image](https://github.com/user-attachments/assets/cda0479f-c564-424c-9205-bc456c1831ff) | [straɪk] | 스트롸이크 |

### Example Sentences

| Example | English Sentence | Standard Hangul Equivalent  |
|---------|------------------|-----------------------------|
| ![image](https://github.com/user-attachments/assets/70e64f4f-59fd-49cd-9c7c-080f22cb376c) | If you go there, you will find him.    | 이프 유 고우 데얼, 유 윌 파인드 임.     |
| ![image](https://github.com/user-attachments/assets/3c5eefe9-9b5a-421d-95bb-ec050e691620) | I'll do it immediately.                | 아일 두 이트 이미티어틀리.             |
| ![image](https://github.com/user-attachments/assets/2f0215c9-7321-41dc-8e2d-82d6580bdbfb) | I have too much work to do.            | 아이 해브 투 머츠 월크 투 두.          |
| ![image](https://github.com/user-attachments/assets/91fbdcd2-2322-4d91-9274-362d04b342dd) | He wanted very badly to survive.       | 히 원티드 베뤼 배들리 투 설바이브.      |
| ![image](https://github.com/user-attachments/assets/984a763e-7652-4ba3-ac35-02b184071e0b) | I don't want a birthday party.         | 아이 도운트 원트 어 벌뜨데이 팔티.      |

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
 * Contributions and suggestions are always welcome, but please try to be *constructive*. Rants will be ignored.

</details>

# 영문-한글 음역기

![sample_output](https://github.com/user-attachments/assets/dc1cfa83-eb2e-4f39-a6ff-da6bf3c954b0)

영문장에서 자연스럽게 들리는 (증강) 한글 표기로 음역.

## 증강 한글

증강 한글은 한국어에는 없지만 영어에는 존재하는 발음을 표기하기 위해 증강된 한글입니다. 현 한글에 "표준" 증강 한글은 없는 바, 이 프로젝트는 제한된 언어학과 상식을 동원해 자체 발명된 증강 한글을 이용합니다. 증강 한글은 한국어 원어민이 영어/한국어 **비**원어민이 알아들을 수 있는 발음을 구사하는 데 목적을 두고 있습니다.

### 분음부호 표기된 자음

한국어에 없는 발음을 표기하기 위헤 기존의 **가장 가까운** 자음 옆에 분음부호(예: ö 위의 점)를 붙입니다. 아래 표의 '종류'는 해당 자음에서 어떤 부분에 신경써야 하는 지를 의미합니다.

| 종류   	| 발음   	| 자음                                                                                     	| 예          | 설명                            |
|--------	|-------	|-----------	                                                                              |-----------	|-------------                   |
| 입술    	| /v/   	| ![image](https://github.com/user-attachments/assets/0cbf93f6-a3b5-4e44-b3cf-4478054edfbc) | ![image](https://github.com/user-attachments/assets/2253aa94-ad86-4bc7-85bb-e8bc9fa09525) (**V**ery)      | 아랫 **입술**을 가볍게 물기. |
|        	| /f/   	| ![image](https://github.com/user-attachments/assets/81f56f07-5c2e-41f6-8931-816125a8b8d4) | ![image](https://github.com/user-attachments/assets/0c88cd99-abeb-4d70-83f1-cd203972ce2d) (Beauti**f**ul) | 아랫 **입술**을 가볍게 물기. |
| 혀    	| /r/   	| ![image](https://github.com/user-attachments/assets/e0d3a86d-8d4b-4d75-b06a-e628912ae4ac) | ![image](https://github.com/user-attachments/assets/2a5f9a45-9019-4c64-91ed-68e58f8c4964) (**R**oom)      | **혀**를 말기.            |
|        	| /θ/   	| ![image](https://github.com/user-attachments/assets/bcf3ffcb-10be-4147-94e0-7140f6f693f6)	| ![image](https://github.com/user-attachments/assets/7941149e-79e2-4c9c-b4b6-720cc393aab3) (**Th**e)       | **혀**를 가볍게 물기.      |
|        	| /ð/   	| ![image](https://github.com/user-attachments/assets/0187de51-973c-4819-986a-b1255a892d63) | ![image](https://github.com/user-attachments/assets/2f56d68b-159b-4e55-8c7d-a0e4f63f354c) (Wi**th**out)   | **혀**를 가볍게 물기.      |
| 강조   	| /z/   	| ![image](https://github.com/user-attachments/assets/da010c74-3779-4a8a-9b42-4931c52689d2)	| ![image](https://github.com/user-attachments/assets/eaba1bce-df31-4c07-a42e-8272b597189d) (**Z**one)      | 'ㅅ' 을 **강조**하기.      |

### 홀자음

홀자음은 **모음이 없는 자음**입니다. 모음 없는 자음에 익숙하지 않은 경우, 모음 'ㅡ'가 있다고 가정하되 최대한 'ㅡ' 발음을 짧게하고, 자음에서 필요로 하지 않는 한 성대를 쓰지 않도록 합니다.

| 예      | IPA 표기           | 표준 한글 표기               |
|---------|-------------------|---------------------------|
| ![image](https://github.com/user-attachments/assets/0c981773-d7bd-4541-9148-55d835bef5e7) | [ðɪs]    | 디스      |
| ![image](https://github.com/user-attachments/assets/0fe76b9d-4ea3-45d9-982f-0efdebbadd58) | [teɪk]   | 테이크    |
| ![image](https://github.com/user-attachments/assets/595ddcc9-1f00-4a7e-9a1c-a3a228f69fda) | [fraɪz]  | 프롸이즈   |
| ![image](https://github.com/user-attachments/assets/cda0479f-c564-424c-9205-bc456c1831ff) | [straɪk] | 스트롸이크 |

### 예문

| 예      | 영문장             | 표준 한글 표기               |
|---------|------------------|----------------------------|
| ![image](https://github.com/user-attachments/assets/70e64f4f-59fd-49cd-9c7c-080f22cb376c) | If you go there, you will find him.    | 이프 유 고우 데얼, 유 윌 파인드 임.     |
| ![image](https://github.com/user-attachments/assets/3c5eefe9-9b5a-421d-95bb-ec050e691620) | I'll do it immediately.                | 아일 두 이트 이미티어틀리.             |
| ![image](https://github.com/user-attachments/assets/2f0215c9-7321-41dc-8e2d-82d6580bdbfb) | I have too much work to do.            | 아이 해브 투 머츠 월크 투 두.          |
| ![image](https://github.com/user-attachments/assets/91fbdcd2-2322-4d91-9274-362d04b342dd) | He wanted very badly to survive.       | 히 원티드 베뤼 배들리 투 설바이브.      |
| ![image](https://github.com/user-attachments/assets/984a763e-7652-4ba3-ac35-02b184071e0b) | I don't want a birthday party.         | 아이 도운트 원트 어 벌뜨데이 팔티.      |

<details>
  <summary>더 읽을거리</summary>

### 동기

이 프로젝트의 기본 철학은 "묘사할 수 있는 만큼 상상할 수 있다"입니다.

한국어 원어민이라면 흔히 한국어에는 없는 영어를 발음하는데 어려움을 겪는데, 심한 경우 이는 한국어 비원어민이 알아듣기 힘든 발음 문제로 이어집니다. 이는 한국인이 해당 발음을 "상상하기 힘들다"는 점에서 비롯되는 것으로 (예: 자음 클러스터 - 모음 없는 자음들의 묶음), 특히 발음을 "한글"로 상상하는 경향이 있는 한국어 원어민들에게는 한글로 묘사할 수 있는 발음의 한계가 사용자 스스로의 발음 한계로 이어지기 쉽습니다.

이 문제에 대한 이 프로젝트의 해결책은 기존 한글에 **분음부호와 홀자음**을 추가해 한글 사용자로 하여금 해당 발음들을 "상상할 수 있도록" 만들자는 것입니다. 분음부호는 한글에 없는 발음(/f/, /v/, /z/, /r/, /θ/, /ð/)을 위해, 홀자음은 한국어에 없는 자음 클러스터를 묘사하기 위해 사용됩니다. 분음부호와 홀자음으로 증강된 한글은 이에 익숙하지 않은 한글 사용자들도 쉽게 이해하고 읽을 수 있도록 의도적으로 설계되었습니다. 예를 들어, 분음부호가 붙은 'ㄸ'은 음가 /θ/를 갖지만 분음부호를 무시하고도 /θ/에 가장 근사한 발음인 'ㄸ'으로 해석될 수 있습니다.

### 개인적 사색

영문 알파벳을 이용하는 대다수의 언어들은 자체 언어에 적절한 발음을 표기하기 위해 흔히 분음부호를 활용합니다 (예: /œ/("외") 발음을 위해 가장 가까운 알파벳인 "o" 에 분음부호 움라우트(Unlaut)를 붙여 "ö"). 더 나아가, 반대로 혹 사용하지 *않는* 알파벳이 생기더라도 이를 외국어 발음을 묘사하는 데 이용하는데 (예: 이탈리아어 자체에는 k나 y가 없지만 외국어 표기를 위해 사용), 개인적 소견은 한글은 이와 정반대로 분음부호를 활용할 수 있다는 것입니다. 즉, 한글은 *외국어를 위해* 분음부호를 사용하고, 분음부호가 없는 글자를 통상적 한국어 표기를 위해 사용할 수 있을 것입니다. 

([블로그 포스트 (영문)](https://gwangmu.medium.com/extending-hangul-for-english-70e8be3fc6ef): 증강 한글에 대한 초창기 구상)

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

## 주석

 * 이 프로젝트는 영문에서 IPA 표기로 음역을 위해 @mphilli가 개발한 [`eng-to-ipa`](https://github.com/mphilli/English-to-IPA)을 사용합니다.
 * 이 프로젝트를 사용하시는 경우 프로젝트 개발자에게 귀띔주시거나 프로젝트 링크를 남겨주실 것을 부탁합니다.
 * 제안이나 기여는 언제든 환영합니다. *분노/비방/폭언*은 자연스럽게 무시될 예정입니다.

<details>
  <summary>Technical TODOs</summary>
  
 - (Important) Provide a friendlier interface to non-terminal or non-Linux users.
 - (Important) Package the repository more nicely. (Help needed!)
    - Installing non-`pip` dependencies (e.g., `python3-tk`, `python3-pil.imagetk`, and `UnDotum`)
    - Printing post-install messages after installation. (in `setup.py`)
    - Uploading this repository to a Python package manager.
 - Improve handling of the variations of pronunciation.
 - Support pronunciation preference.
 - Support drawing regular Hangul sentences.

</details>
