# English to Hangul

English sentence to naturally-sounding (modified) Hangul notation.

## Requirement

 - Linux
 - Python 3.x
 - `eng-to-ipa` Python package

## TODO

 - Collect loose Hangul symbols into a complete letter.
    - 'ㅁ' should be the final consonant.
    - Any other consonants should be vowelless consonant letters.
 - Assign 'ㅇ' in front of vowel Hangul symbols without the first consonant.
 - Define context-dependent IPA symbols (e.g., 'ʃ' or 'w') with multi-symbol
   transcriptions.
 - Replace added Hangul symbols to the transcription.
    - See Wikipedia documents on 'Hangul Jamo' and 'Hangul Syllables'.
    - Idea: construct a 'HangulConsonant' class that consists of;
        - Original consonant letter
        - Lip annotation?
        - Tongue annotation?
        - Other annotation?
    - Idea: construct a 'HangulLetter' class that consists of;
        - HangulConsonant initial
        - HangulVowel
        - HangulConsonant final
    - Idea: write a 'printHangulLetter' function that;
        - Maps consonants and a vowel to a Unicode syllable.
        - Assigns annotations at a proper coordiate.
 - Write GUI to visualize transcripted modified Hangul.
    - Initially, just use pyplot.
