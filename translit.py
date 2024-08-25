#!/usr/bin/python3

import eng_to_ipa as ipa
import logging as log

import hclasses as hcl
import tables
import util

def ipa_to_loose_han(sent_ipa, options):
    log.debug("## Tranliterate to loose Hangul")
    sent_han = ""

    while (sent_ipa):
        # Ignore stresses for now.
        if (sent_ipa[0:1] == "ˈ" or sent_ipa[0:1] == "ˌ"):
            sent_ipa = sent_ipa[1:]
            continue

        # Transliterate IPA symbols, longer symbol sets first.
        ipa_found=False
        for ipa, han in tables.ipa_to_han.items():
            if (sent_ipa[0:len(ipa)] == ipa):
                sent_han = sent_han + han 
                sent_ipa = sent_ipa[len(ipa):]
                ipa_found=True
                break
        if (not ipa_found):
            sent_han = sent_han + sent_ipa[0:1]
            sent_ipa = sent_ipa[1:]

        log.debug(sent_ipa + " --> " + sent_han)

    return sent_han

class HanPacker():
    def __init__(self, sent_han, options):
        self.sent_hcl = [hcl.HangulLetter()]
        self.cur_han = ""
        self.next_han = ""
        self.sent_han = sent_han
        self.has_anno = False
        self.options = options

    def push_empty(self):
        self.sent_hcl = self.sent_hcl + [hcl.HangulLetter()]

    def top(self):
        return (self.sent_hcl[-1])

    def next(self):
        if (not self.is_empty()):
            if (type(self.top()) is hcl.NonHangulLetter or \
                (self.top().is_full() and (util.is_whole_hangul_letter(self.next_han) or \
                    util.is_hangul_jamo(self.next_han)))):
                self.sent_hcl = self.sent_hcl + [hcl.HangulLetter()]

        self.cur_han = self.sent_han[0]
        self.next_han = self.sent_han[1:2]
        self.sent_han = self.sent_han[1:]
        self.has_anno = False

    def is_empty(self):
        return (not self.sent_han)

    def get(self):
        return (self.sent_hcl)

    def pack(self):
        while (not self.is_empty()):
            self.next()

            if (self.cur_han == '`'):
                self.next()
                if (not self.options["no_annotation"]):
                    self.has_anno = True

            if (util.is_whole_hangul_letter(self.cur_han)):
                if (self.top().is_empty()):
                    self.sent_hcl = self.sent_hcl[:-1]
                self.sent_hcl = self.sent_hcl + [hcl.HangulLetter(whole=self.cur_han)]
            elif (util.is_hangul_jamo(self.cur_han)):
                if (self.top().initial.is_none()):
                    if (util.is_hangul_initial(self.cur_han)):
                        log.debug('jamo.initial.initial')
                        self.top().set_initial(self.cur_han, anno=self.has_anno)
                    elif (util.is_hangul_vowel(self.cur_han)):
                        log.debug('jamo.initial.vowel')
                        self.top().set_initial('ㅇ')
                        self.top().set_vowel(self.cur_han)
                    else:
                        log.debug('jamo.initial.wtf')
                        assert(false)
                elif (self.top().vowel.is_none()):
                    if (util.is_hangul_initial(self.cur_han)):
                        if (util.is_hangul_initfin(self.cur_han)):
                            log.debug('jamo.vowel.initial.initfin')
                            self.top().set_vowel('ㅡ')
                            self.top().set_final(self.cur_han, anno=self.has_anno)
                        else:
                            log.debug('jamo.vowel.initial.!initfin')
                            self.sent_hcl = self.sent_hcl + [hcl.HangulLetter(initial=self.cur_han, initial_anno=self.has_anno)]
                    elif (util.is_hangul_vowel(self.cur_han)):
                        log.debug('jamo.vowel.vowel')
                        self.top().set_vowel(self.cur_han)
                elif (self.top().final.is_none()):
                    if (util.is_hangul_initial(self.cur_han)):
                        if (util.is_hangul_initfin(self.cur_han)):
                            if (util.is_hangul_vowel(self.next_han)):
                                log.debug('jamo.final.initial.initfin.vowel')
                                self.sent_hcl = self.sent_hcl + [hcl.HangulLetter(initial=self.cur_han, initial_anno=self.has_anno)]
                            else:
                                log.debug('jamo.final.initial.initfin.!vowel')
                                self.top().set_final(self.cur_han, anno=self.has_anno)
                        else:
                            log.debug('jamo.final.initial.!initfin')
                            self.sent_hcl = self.sent_hcl + [hcl.HangulLetter(initial=self.cur_han, initial_anno=self.has_anno)]
                    elif (util.is_hangul_vowel(self.cur_han)):
                        log.debug('jamo.final.vowel')
                        self.sent_hcl = self.sent_hcl + [hcl.HangulLetter(initial='ㅇ', vowel=self.cur_han)]
            else:
                log.debug('!jamo')
                self.sent_hcl = self.sent_hcl + [hcl.NonHangulLetter(self.cur_han)]
            
            log.debug(self.sent_han)
            log.debug(self.sent_hcl)
            log.debug("")

        if (self.options["no_self_consonants"]):
            for cur_hcl in self.sent_hcl:
                if (type(cur_hcl) is hcl.HangulLetter and cur_hcl.is_self_consonant()):
                    cur_hcl.set_vowel('ㅡ')

def loose_han_to_hcl(sent_han, options):
    log.debug("## Pack loose Hangul letters")
    packer = HanPacker(sent_han, options)
    packer.pack()
    return packer.get()

def eng_to_ipa(sent_eng, options):
    return ipa.convert(sent_eng)

def hcl_to_han(sent_hcl, options):
    return ''.join(str(x) for x in sent_hcl)

def ipa_to_hcl(sent_ipa, options):
    sent_han = ipa_to_loose_han(sent_ipa, options)
    sent_hcl = loose_han_to_hcl(sent_han, options)
    return sent_hcl
