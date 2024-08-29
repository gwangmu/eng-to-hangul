#!/usr/bin/python3

import eng_to_ipa as ipa
import logging as log

import hclasses as hcl
import tables
import util

def ipa_to_loose_han(sent_ipa, options):
    log.debug("## Tranliterate to loose Hangul")
    sent_han = ""
    first_iter = True

    while (sent_ipa):
        if (first_iter or sent_ipa[0:1] == " "):
            cur_idx = 0
            str_buf=""
            while (sent_ipa[cur_idx:cur_idx+1] != '' and sent_ipa[cur_idx:cur_idx+1] != ' '):
                if (sent_ipa[cur_idx:cur_idx+1] == '*'):
                    sent_han = sent_han + str_buf
                    sent_ipa = sent_ipa[cur_idx+1:]
                    break
                str_buf = str_buf + sent_ipa[cur_idx:cur_idx+1]
                cur_idx = cur_idx + 1

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
                        if (util.is_hangul_initfin(self.cur_han) and not self.has_anno):
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
                if (self.top().is_empty()):
                    self.sent_hcl = self.sent_hcl[:-1]
                self.sent_hcl = self.sent_hcl + [hcl.NonHangulLetter(self.cur_han)]
            
            log.debug(self.sent_han)
            log.debug(self.sent_hcl)
            log.debug("")

        # Make it more natural
        for i, cur_hcl in enumerate(self.sent_hcl):
            if (i+1 < len(self.sent_hcl)):
                next_hcl = self.sent_hcl[i+1]
                if (type(cur_hcl) is hcl.HangulLetter and type(next_hcl) is hcl.HangulLetter and \
                    not cur_hcl.final.is_none() and next_hcl.initial.value == 'ㅇ'):
                    next_hcl.set_initial(cur_hcl.final.value)
                    cur_hcl.unset_final()

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
    # Correct some peculiar punctuations.
    list_eng = list(sent_eng)
    for i, ch in enumerate(list_eng):
        if (ch == '’'):
            list_eng[i] = "'"
    sent_eng = ''.join(list_eng)

    if (options["retrieve_all"]):
        sent_ipa = ipa.convert(sent_eng, retrieve_all=True)
    else:
        # Convert
        sent_ipa = ipa.convert(sent_eng)

        # Correct some words to Korean-friendly versions.
        sent_ipa = " " + sent_ipa + " "
        adjs = {
            " tɪ ": " tu "
            }
        for adj_from, adj_to in adjs.items():
            sent_ipa = sent_ipa.replace(adj_from, adj_to)
        sent_ipa = sent_ipa[1:-2]

    return sent_ipa

def hcl_to_han(sent_hcl, options):
    if (not isinstance(sent_hcl, list)):
        return ""
    if (len(sent_hcl) != 0 and isinstance(sent_hcl[0], list)):
        return [''.join(str(x) for x in h) for h in sent_hcl]
    else:
        return ''.join(str(x) for x in sent_hcl)

def ipa_to_hcl(sent_ipa, options):
    is_list_input = isinstance(sent_ipa, list)

    if (is_list_input):
        sent_ipa_list = sent_ipa
    else:
        sent_ipa_list = [sent_ipa]

    sent_hcl_list = []
    for sent_ipa in sent_ipa_list:
        sent_han = ipa_to_loose_han(sent_ipa, options)
        sent_hcl = loose_han_to_hcl(sent_han, options)
        sent_hcl_list = sent_hcl_list + [sent_hcl]

    if (is_list_input):
        return sent_hcl_list
    else:
        return sent_hcl_list[0]
