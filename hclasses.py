#!/usr/bin/python3

import tables
import logging as log

class HangulConsonant:
    def __init__(self, value, anno=False):
        self.value = value
        self.anno = anno

    def is_none(self):
        return self.value == None

    def has_anno(self):
        return self.anno

class HangulVowel:
    def __init__(self, value):
        self.value = value

    def is_none(self):
        return self.value == None

class Letter:
    pass

class NonHangulLetter(Letter):
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return self.value
    
    def __str__(self):
        return self.value

    def get_str_wo_anno(self):
        return self.value

class HangulLetter(Letter):
    def __init__(self, initial=None, vowel=None, final=None, whole=None,
            initial_anno=False, final_anno=False):
        if (whole):
            whole_int = ord(whole)
            whole_int = whole_int - 44032
            idx_final = int(whole_int % 28)
            whole_int = whole_int - idx_final
            log.debug("idx (final): " + str(idx_final))
            whole_int = whole_int / 28
            idx_vowel = int(whole_int % 21)
            whole_int = whole_int - idx_vowel
            log.debug("idx (vowel): " + str(idx_vowel))
            whole_int = whole_int / 21
            idx_initial = int(whole_int)
            log.debug("idx (initial): " + str(idx_initial))
            
            initial = tables.han_initial[idx_initial]
            vowel = tables.han_vowel[idx_vowel]
            final = tables.han_final[idx_final]

        self.initial = HangulConsonant(initial, anno=initial_anno) 
        self.vowel = HangulVowel(vowel)
        self.final = HangulConsonant(final, anno=final_anno)

    def is_empty(self):
        return (self.initial.is_none() and self.vowel.is_none() and
                self.final.is_none())

    def is_defined(self):
        return (not self.initial.is_none() and not self.vowel.is_none())

    def is_full(self):
        return (not self.initial.is_none() and not self.vowel.is_none() and
                not self.final.is_none())

    def set_initial(self, han, anno=False):
        self.initial = HangulConsonant(han, anno=anno)

    def set_vowel(self, han):
        self.vowel = HangulVowel(han)

    def set_final(self, han, anno=False):
        self.final = HangulConsonant(han, anno=anno)

    def fuse(self):
        no_initial = tables.han_initial.index(self.initial.value)
        no_vowel = tables.han_vowel.index(self.vowel.value)
        no_final = tables.han_final.index(self.final.value)

        return chr((no_initial * 588 + no_vowel * 28 + no_final) + 44032)

    def get_str_wo_anno(self):
        if (not self.is_defined()):
            if (self.initial.is_none()):
                return '□ '
            else:
                return self.initial.value
        else:
            return self.fuse()

    def __str__(self):
        if (not self.is_defined()):
            if (self.initial.is_none()):
                return '□ '
            else:
                return ("`" if (self.initial.has_anno()) else "") + self.initial.value
        else:
            anno = ""
            if (self.initial.has_anno() or (self.final and self.final.has_anno())):
                anno = "`"
            return anno + self.fuse()

    def __repr__(self):
        return str(self)
