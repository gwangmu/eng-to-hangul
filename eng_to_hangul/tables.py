#!/usr/bin/python3

# IPA to hangul transcription
ipa_to_han = {
    "ts": "ㅊ",
    "wa": "와",
    "wɑ": "와",
    "wə": "워",
    "wɔ": "워", 
    "wɪ": "위",
    "wi": "위",
    "we": "웨",
    "wɛ": "웨",
    "wʊ": "우",
    "ʊə": "워",
    "ʃə": "셔",
    "ʃe": "쉐",
    "ʃɑ": "샤",
    "ʃʊ": "슈",
    "ju": "ㅠ",
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
    "w": "ㅝ",
    "x": "ㅋㅅ",
    "z": "`ㅈ",
    "ə": "ㅓ",
    "ɑ": "ㅏ",
    "ɔ": "ㅗ",
    "ð": "`ㄷ",
    "ɛ": "ㅔ",
    "h": "ㅎ",
    "ɪ": "ㅣ",
    "ŋ": "ㅇ",
    "ʃ": "쉬",
    "θ": "`ㄸ",
    "ʊ": "ㅜ",
    "u": "ㅜ",
    "ʒ": "ㅈ",
    "i": "ㅣ",
    "j": "ㅠ",
    }

# Hangul initial consonants
han_initial = [
    'ㄱ',
    'ㄲ',
    'ㄴ',
    'ㄷ',
    'ㄸ',
    'ㄹ',
    'ㅁ',
    'ㅂ',
    'ㅃ',
    'ㅅ',
    'ㅆ',
    'ㅇ',
    'ㅈ',
    'ㅉ',
    'ㅊ',
    'ㅋ',
    'ㅌ',
    'ㅍ',
    'ㅎ',
    ]

# Hangul vowels
han_vowel = [
    'ㅏ',
    'ㅐ',
    'ㅑ',
    'ㅒ',
    'ㅓ',
    'ㅔ',
    'ㅕ',
    'ㅖ',
    'ㅗ',
    'ㅘ',
    'ㅙ',
    'ㅚ',
    'ㅛ',
    'ㅜ',
    'ㅝ',
    'ㅞ',
    'ㅟ',
    'ㅠ',
    'ㅡ',
    'ㅢ',
    'ㅣ',
    ]

# Hangul final consonants
han_final = [
    None,
    'ㄱ',
    'ㄲ',
    'ㄳ',
    'ㄴ',
    'ㄵ',
    'ㄶ',
    'ㄷ',
    'ㄹ',
    'ㄺ',
    'ㄻ',
    'ㄼ',
    'ㄽ',
    'ㄾ',
    'ㄿ',
    'ㅀ',
    'ㅁ',
    'ㅂ',
    'ㅄ',
    'ㅅ',
    'ㅆ',
    'ㅇ',
    'ㅈ',
    'ㅊ',
    'ㅋ',
    'ㅌ',
    'ㅍ',
    'ㅎ',
    ]

# Hangul initial consonants, which can also naturally be final
han_initfin = [
    'ㅁ',
    'ㄴ',
    'ㄹ',
    'ㅇ',
    ]

# Hangul explosive consonants (파열음)
han_explosive_consonants = [
    "ㅂ",
    "ㅃ",
    "ㅍ",
    "ㄷ",
    "ㄸ",
    "ㅌ",
    "ㄱ",
    "ㄲ",
    "ㅋ",
    ]

# Utility methods
def is_hangul_initial(han):
    return (han in han_initial)

def is_hangul_vowel(han):
    return (han in han_vowel)

def is_hangul_final(han):
    return (han in han_final)

def is_hangul_initfin(han):
    return (han in han_initfin)

def is_whole_hangul_letter(han):
    return (0xac00 <= ord(han) and ord(han) <= 0xd7a4)

def is_hangul_jamo(han):
    return (0x3130 <= ord(han) and ord(han) <= 0x318f)

def is_hangul(han):
    return (is_whole_hangul_letter(han) or is_hangul_jamo(han))
