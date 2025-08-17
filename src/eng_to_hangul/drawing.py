#!/usr/bin/python3

import logging as log
from . import hclasses as hcl
from . import tables

UNI_OFFSET = 44032

# letter, tongue diacritic, lip diacritic, stress discritic, iotation diacritic
table = {
    "initial": [
        hcl.HangulConsonant("ㄱ", False),
        hcl.HangulConsonant("ㄴ", False),
        hcl.HangulConsonant("ㄷ", False),
        hcl.HangulConsonant("ㄹ", False),
        hcl.HangulConsonant("ㅁ", False),
        hcl.HangulConsonant("ㅂ", False),
        hcl.HangulConsonant("ㅅ", False),
        hcl.HangulConsonant("ㅇ", False),
        hcl.HangulConsonant("ㅈ", False),
        hcl.HangulConsonant("ㅊ", False),
        hcl.HangulConsonant("ㅋ", False),
        hcl.HangulConsonant("ㅌ", False),
        hcl.HangulConsonant("ㅍ", False),
        hcl.HangulConsonant("ㅎ", False),
        hcl.HangulConsonant("ㄹ", True ),
        hcl.HangulConsonant("ㄷ", True ),
        hcl.HangulConsonant("ㄸ", True ),
        hcl.HangulConsonant("ㅂ", True ),
        hcl.HangulConsonant("ㅍ", True ),
        hcl.HangulConsonant("ㅈ", True ),
    ],
    "vowel": [
        hcl.HangulVowel("ㅏ", False),
        hcl.HangulVowel("ㅑ", False),
        hcl.HangulVowel("ㅓ", False),
        hcl.HangulVowel("ㅕ", False),
        hcl.HangulVowel("ㅗ", False),
        hcl.HangulVowel("ㅛ", False),
        hcl.HangulVowel("ㅜ", False),
        hcl.HangulVowel("ㅠ", False),
        hcl.HangulVowel("ㅡ", False),
        hcl.HangulVowel("ㅣ", False),
        hcl.HangulVowel("ㅐ", False),
        hcl.HangulVowel("ㅒ", False),
        hcl.HangulVowel("ㅔ", False),
        hcl.HangulVowel("ㅖ", False),
        hcl.HangulVowel("ㅘ", False),
        hcl.HangulVowel("ㅙ", False),
        hcl.HangulVowel("ㅚ", False),
        hcl.HangulVowel("ㅝ", False),
        hcl.HangulVowel("ㅞ", False),
        hcl.HangulVowel("ㅟ", False),
        hcl.HangulVowel("ㅣ", True ),
    ],
    "final": [
        hcl.HangulConsonant(None, False),
        hcl.HangulConsonant("ㄱ", False),
        hcl.HangulConsonant("ㄴ", False),
        hcl.HangulConsonant("ㄷ", False),
        hcl.HangulConsonant("ㄹ", False),
        hcl.HangulConsonant("ㅁ", False),
        hcl.HangulConsonant("ㅂ", False),
        hcl.HangulConsonant("ㅅ", False),
        hcl.HangulConsonant("ㅇ", False),
        hcl.HangulConsonant("ㅈ", False),
        hcl.HangulConsonant("ㅊ", False),
        hcl.HangulConsonant("ㅋ", False),
        hcl.HangulConsonant("ㅌ", False),
        hcl.HangulConsonant("ㅍ", False),
        hcl.HangulConsonant("ㅎ", False),
    ]
}

def get_ahan_sentence(sent_hcl):
    sent_ahan = ""
    for hclass in sent_hcl:
        if (isinstance(hclass, hcl.HangulLetter)):
            if (hclass.is_self_consonant()):
                c = 0xc49c + table["initial"].index(hclass.initial)
            else:
                c = UNI_OFFSET + table["initial"].index(hclass.initial) * len(table["vowel"]) * len(table["final"]) + \
                        table["vowel"].index(hclass.vowel) * len(table["final"]) + \
                        table["final"].index(hclass.final)
        else:
            c = ord(hclass.get_str_wo_anno())
        sent_ahan += chr(c)
    return sent_ahan
