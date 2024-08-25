#!/usr/bin/python3

import eng_to_ipa as ipa
import logging as log

import hclasses as hcl
import tables
import util

def eng_to_ipa(sent_eng, options):
    return ipa.convert(sent_eng)

def hcl_to_han(sent_hcl, options):
    return ''.join(x.get_str_wo_anno() for x in sent_hcl)

# TODO: polish this
def ipa_to_hcl(sent_ipa, options):
    # Tranliterate to loose Hangul
    log.debug("# Tranliterate to loose Hangul")

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

    # Pack loose Hangul letters.
    log.debug("## Pack loose Hangul letters")

    sent_han_org = sent_han
    sent_hcl = [hcl.HangulLetter()]
    while (sent_han):
        cur_hcl = sent_hcl[-1]
        cur_han = sent_han[0]
        next_han = sent_han[1:2]
        sent_han = sent_han[1:]
        has_anno = False

        if (cur_han == '`'):
            cur_han = sent_han[0]
            next_han = sent_han[1:2]
            sent_han = sent_han[1:]
            has_anno = True

        if (util.is_whole_hangul_letter(cur_han)):
            if (cur_hcl.is_empty()):
                sent_hcl = sent_hcl[:-1]
            sent_hcl = sent_hcl + [hcl.HangulLetter(whole=cur_han)]
        elif (util.is_hangul_jamo(cur_han)):
            if (cur_hcl.initial.is_none()):
                if (util.is_hangul_initial(cur_han)):
                    log.debug('jamo.initial.initial')
                    cur_hcl.set_initial(cur_han, anno=has_anno)
                elif (util.is_hangul_vowel(cur_han)):
                    log.debug('jamo.initial.vowel')
                    cur_hcl.set_initial('ㅇ')
                    cur_hcl.set_vowel(cur_han)
                else:
                    log.debug('jamo.initial.wtf')
                    assert(false)
            elif (cur_hcl.vowel.is_none()):
                if (util.is_hangul_initial(cur_han)):
                    if (util.is_hangul_initfin(cur_han)):
                        log.debug('jamo.vowel.initial.initfin')
                        cur_hcl.set_vowel('ㅡ')
                        cur_hcl.set_final(cur_han, anno=has_anno)
                    else:
                        log.debug('jamo.vowel.initial.!initfin')
                        sent_hcl = sent_hcl + [hcl.HangulLetter(initial=cur_han, initial_anno=has_anno)]
                elif (util.is_hangul_vowel(cur_han)):
                    log.debug('jamo.vowel.vowel')
                    cur_hcl.set_vowel(cur_han)
            elif (cur_hcl.final.is_none()):
                if (util.is_hangul_initial(cur_han)):
                    if (util.is_hangul_initfin(cur_han)):
                        if (util.is_hangul_vowel(next_han)):
                            log.debug('jamo.final.initial.initfin.vowel')
                            sent_hcl = sent_hcl + [hcl.HangulLetter(initial=cur_han, initial_anno=has_anno)]
                        else:
                            log.debug('jamo.final.initial.initfin.!vowel')
                            cur_hcl.set_final(cur_han, anno=has_anno)
                    else:
                        log.debug('jamo.final.initial.!initfin')
                        sent_hcl = sent_hcl + [hcl.HangulLetter(initial=cur_han, initial_anno=has_anno)]
                elif (util.is_hangul_vowel(cur_han)):
                    log.debug('jamo.final.vowel')
                    sent_hcl = sent_hcl + [hcl.HangulLetter(initial='ㅇ', vowel=cur_han)]
        else:
            log.debug('!jamo')
            sent_hcl = sent_hcl + [hcl.NonHangulLetter(cur_han)]

        if (next_han):
            cur_hcl = sent_hcl[-1]
            if (type(cur_hcl) is hcl.NonHangulLetter or \
                (cur_hcl.is_full() and (util.is_whole_hangul_letter(next_han) or \
                    util.is_hangul_jamo(next_han)))):
                sent_hcl = sent_hcl + [hcl.HangulLetter()]
        
        log.debug(sent_han)
        log.debug(sent_hcl)
        log.debug("")

    return sent_hcl
