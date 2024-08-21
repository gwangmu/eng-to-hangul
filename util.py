import tables

def is_hangul_initial(han):
    return (han in tables.han_initial)

def is_hangul_vowel(han):
    return (han in tables.han_vowel)

def is_hangul_final(han):
    return (han in tables.han_final)

def is_hangul_initfin(han):
    return (han in tables.han_initfin)

def is_whole_hangul_letter(han):
    return (0xac00 <= ord(han) and ord(han) <= 0xd7a4)

def is_hangul_jamo(han):
    return (0x3130 <= ord(han) and ord(han) <= 0x318f)
