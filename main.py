#!/usr/bin/python3

import eng_to_ipa as ipa
import argparse

ipa_to_han = {
    # Two-symbol transcription
    2: {
        "eɪ": "ㅔ이", 
        "aʊ": "ㅏ우",
        "aɪ": "ㅏ이", 
        "ər": "ㅓ얼", 
        "oʊ": "ㅗ우", 
        "ɔɪ": "ㅗ이", 
        "əʊ": "ㅓ우",
        "ts": "ㅊ",
        "wɑ": "와",
        "wə": "워",
        "ʃə": "셔",
    },
    # Singul-symbol transcription
    1: {
        "ʤ": "ㅈ", 
        "ʧ": "ㅊ",
        "æ": "ㅐ", 
        "a": "ㅏ",
        "b": "ㅂ",
        "d": "ㄷ",
        "e": "ㅔ",
        "f": "`ㅍ",
        "g": "ㄱ",
        "i": "ㅣ",
        "k": "ㅋ",
        "l": "ㄹ",
        "m": "ㅁ",
        "n": "ㄴ",
        "o": "ㅗ",
        "p": "ㅍ",
        "q": "ㅋ",
        "r": "`ㄹ",
        "s": "ㅅ",
        "t": "ㅌ",
        "v": "`ㅂ",
        "w": "ㅜ",
        "x": "ㅋㅅ",
        "z": "`ㅈ",
        "ə": "ㅓ",
        "ɑ": "ㅏ",
        "ɔ": "ㅗ",
        "ð": "`ㄷ",
        "ɛ": "ㅔ",
        "h": "ㅎ",
        "ɪ": "ㅣ",
        "ŋ": "ㅇ응",
        "ʃ": "쉬",
        "θ": "`ㄸ",
        "ʊ": "ㅜ",
        "u": "ㅜ",
        "ʒ": "ㅈ",
        "i": "ㅣ",
        "j": "ㅠ",
    }}

han_initial = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ',
        'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
han_vowel = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
        'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
        'ㅣ']
han_final = [None, 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ',
        'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
        'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
han_initfin = ['ㅁ', 'ㄴ', 'ㄹ', 'ㅇ']

class HangulConsonant:
    def __init__(self, value, 
            lip_anno=False, tongue_anno=False, other_anno=False):
        self.value = value
        self.lip_anno = lip_anno
        self.tongue_anno = tongue_anno
        self.other_anno = other_anno

    def IsNone(self):
        return self.value == None

class HangulVowel:
    def __init__(self, value):
        self.value = value

    def IsNone(self):
        return self.value == None

def IsHangulInitial(han):
    return (han in han_initial)

def IsHangulVowel(han):
    return (han in han_vowel)

def IsHangulFinal(han):
    return (han in han_final)

def IsHangulInitFin(han):
    return (han in han_initfin)

def IsWholeHangulLetter(han):
    return (0xac00 <= ord(han) and ord(han) <= 0xd7a4)

def IsHangulJamo(han):
    return (0x3130 <= ord(han) and ord(han) <= 0x318f)

def ParseWholeHangulLetter(whole):
    whole_int = ord(whole)
    whole_int = whole_int - 44032
    idx_final = int(whole_int % 28)
    whole_int = whole_int - idx_final
    print(idx_final)
    whole_int = whole_int / 28
    idx_vowel = int(whole_int % 21)
    whole_int = whole_int - idx_vowel
    print(idx_vowel)
    whole_int = whole_int / 21
    idx_initial = int(whole_int)
    print(idx_initial)
    return (HangulConsonant(han_initial[idx_initial]), 
            HangulVowel(han_vowel[idx_vowel]),
            HangulConsonant(han_final[idx_final]))

class NonHangulLetter:
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return self.value

class HangulLetter:
    def __init__(self, initial=HangulConsonant(None),
            vowel=HangulVowel(None), final=HangulConsonant(None),
            whole=None):
        if (whole):
            (self.initial, self.vowel, self.final) = \
                ParseWholeHangulLetter(whole)
        else:
            self.initial = initial
            self.vowel = vowel
            self.final = final

    def IsEmpty(self):
        return (self.initial.IsNone() and self.vowel.IsNone() and
                self.final.IsNone())

    def IsDefined(self):
        return (not self.initial.IsNone() and not self.vowel.IsNone())

    def IsFull(self):
        return (not self.initial.IsNone() and not self.vowel.IsNone() and
                not self.final.IsNone())

    def Fuse(self):
        no_initial = han_initial.index(self.initial.value)
        no_vowel = han_vowel.index(self.vowel.value)
        no_final = han_final.index(self.final.value)

        return chr((no_initial * 588 + no_vowel * 28 + no_final) + 44032)

    def __repr__(self):
        if (not self.IsDefined()):
            if (self.initial.IsNone()):
                return '□ '
            else:
                return self.initial.value
        else:
            return self.Fuse()
        

ipa_nums = sorted(ipa_to_han.keys(), reverse=True)

parser = argparse.ArgumentParser()
parser.add_argument('sent_eng', type=str, help="Sentence in English")
args = parser.parse_args()

sent_eng = args.sent_eng
sent_ipa = ipa.convert(sent_eng, keep_punct=False)
sent_ipa_org = sent_ipa

trans_steps = []
sent_han = ""
while (sent_ipa):
    # Carry over spaces.
    if (sent_ipa[0:1] == " "):
        sent_han = sent_han + " "
        sent_ipa = sent_ipa[1:]

    # Ignore stresses for now.
    if (sent_ipa[0:1] == "ˈ" or sent_ipa[0:1] == "ˌ"):
        sent_ipa = sent_ipa[1:]

    # Transcribe IPA symbols, longer symbol sets first.
    for ipa_num in ipa_nums + [-1]:
        if (ipa_num == -1): 
            print("error: unrecognized IPA symbol '{}'".format(sent_ipa[0:1]))
            print("error: transcription steps;")
            for i, trans_step in enumerate(trans_steps):
                print("{}: {}".format(i, trans_step))
            exit
        if (sent_ipa[0:ipa_num] in ipa_to_han[ipa_num].keys()):
            sent_han = sent_han + ipa_to_han[ipa_num][sent_ipa[0:ipa_num]]
            sent_ipa = sent_ipa[ipa_num:]
            break

    trans_steps = trans_steps + [sent_ipa, sent_han]

sent_han_org = sent_han

# Pack loose Hangul letters.
sent_hcls = [HangulLetter()]
while (sent_han):
    cur_hcl = sent_hcls[-1]
    cur_han = sent_han[0]
    next_han = sent_han[1:2]
    sent_han = sent_han[1:]
    has_anno = False

    if (cur_han == '`'):
        cur_han = sent_han[0]
        next_han = sent_han[1:2]
        sent_han = sent_han[1:]
        has_anno = True

    if (IsWholeHangulLetter(cur_han)):
        if (cur_hcl.IsEmpty()):
            sent_hcls = sent_hcls[:-1]
        sent_hcls = sent_hcls + [HangulLetter(whole=cur_han)]
    elif (IsHangulJamo(cur_han)):
        if (cur_hcl.initial.IsNone()):
            if (IsHangulInitial(cur_han)):
                print('jamo.initial.initial')
                cur_hcl.initial = HangulConsonant(cur_han)
            elif (IsHangulVowel(cur_han)):
                print('jamo.initial.vowel')
                cur_hcl.initial = HangulConsonant('ㅇ')
                cur_hcl.vowel = HangulVowel(cur_han)
            else:
                print('jamo.initial.wtf')
                assert(false)
        elif (cur_hcl.vowel.IsNone()):
            if (IsHangulInitial(cur_han)):
                if (IsHangulInitFin(cur_han)):
                    print('jamo.vowel.initial.initfin')
                    cur_hcl.vowel = HangulVowel('ㅡ')
                    cur_hcl.final = HangulConsonant(cur_han)
                else:
                    print('jamo.vowel.initial.!initfin')
                    sent_hcls = sent_hcls + \
                        [HangulLetter(initial=HangulConsonant(cur_han))]
            elif (IsHangulVowel(cur_han)):
                print('jamo.vowel.vowel')
                cur_hcl.vowel = HangulVowel(cur_han)
        elif (cur_hcl.final.IsNone()):
            if (IsHangulInitial(cur_han)):
                if (IsHangulInitFin(cur_han)):
                    if (IsHangulVowel(next_han)):
                        print('jamo.final.initial.initfin.vowel')
                        sent_hcls = sent_hcls + \
                            [HangulLetter(initial=HangulConsonant(cur_han))]
                    else:
                        print('jamo.final.initial.initfin.!vowel')
                        cur_hcl.final = HangulConsonant(cur_han)
                else:
                    print('jamo.final.initial.!initfin')
                    sent_hcls = sent_hcls + \
                        [HangulLetter(initial=HangulConsonant(cur_han))]
            elif (IsHangulVowel(cur_han)):
                print('jamo.final.vowel')
                sent_hcls = sent_hcls + \
                    [HangulLetter(initial=HangulConsonant('ㅇ'),
                        vowel=HangulVowel(cur_han))]
    else:
        print('!jamo')
        sent_hcls = sent_hcls + [NonHangulLetter(cur_han)]

    if (next_han):
        cur_hcl = sent_hcls[-1]
        if (type(cur_hcl) is NonHangulLetter or \
            (cur_hcl.IsFull() and (IsWholeHangulLetter(next_han) or \
                IsHangulJamo(next_han)))):
            sent_hcls = sent_hcls + [HangulLetter()]
    
    print(sent_han)
    print(sent_hcls)
    print()
    input()

print("IPA: {}".format(sent_ipa_org))
print("Han: {}".format(sent_han_org))
print("Hcl: {}".format(sent_hcls))
