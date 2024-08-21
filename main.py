#!/usr/bin/python3

import eng_to_ipa as ipa
import argparse

import tables
import util
import hclasses as hcl
import log

log.init()

parser = argparse.ArgumentParser()
parser.add_argument('sent_eng', type=str, help="Sentence in English")
args = parser.parse_args()

sent_eng = args.sent_eng
sent_ipa = ipa.convert(sent_eng, keep_punct=False)
sent_ipa_org = sent_ipa

# Transcribe IPA to hangul.
log.debug("## Transcription")

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
    ipa_found=False
    for ipa, han in tables.ipa_to_han.items():
        if (sent_ipa[0:len(ipa)] == ipa):
            sent_han = sent_han + han 
            sent_ipa = sent_ipa[len(ipa):]
            ipa_found=True
            break
    if (not ipa_found):
        log.error("unrecognized IPA symbol '{}'".format(sent_ipa[0:1]))
        log.error("transcription steps;")
        for i, trans_step in enumerate(trans_steps):
            log.error("{}: {}".format(i, trans_step))
        log.fatal("terminating...")

    log.debug(sent_ipa + " --> " + sent_han)

# Pack loose Hangul letters.
log.debug("## Packing")

sent_han_org = sent_han
sent_hcls = [hcl.HangulLetter()]
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

    if (util.is_whole_hangul_letter(cur_han)):
        if (cur_hcl.is_empty()):
            sent_hcls = sent_hcls[:-1]
        sent_hcls = sent_hcls + [hcl.HangulLetter(whole=cur_han)]
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
                    sent_hcls = sent_hcls + [hcl.HangulLetter(initial=cur_han, initial_anno=has_anno)]
            elif (util.is_hangul_vowel(cur_han)):
                log.debug('jamo.vowel.vowel')
                cur_hcl.set_vowel(cur_han)
        elif (cur_hcl.final.is_none()):
            if (util.is_hangul_initial(cur_han)):
                if (util.is_hangul_initfin(cur_han)):
                    if (util.is_hangul_vowel(next_han)):
                        log.debug('jamo.final.initial.initfin.vowel')
                        sent_hcls = sent_hcls + [hcl.HangulLetter(initial=cur_han, initial_anno=has_anno)]
                    else:
                        log.debug('jamo.final.initial.initfin.!vowel')
                        cur_hcl.set_final(cur_han, anno=has_anno)
                else:
                    log.debug('jamo.final.initial.!initfin')
                    sent_hcls = sent_hcls + [hcl.HangulLetter(initial=cur_han, initial_anno=has_anno)]
            elif (util.is_hangul_vowel(cur_han)):
                log.debug('jamo.final.vowel')
                sent_hcls = sent_hcls + [hcl.HangulLetter(initial='ㅇ', vowel=cur_han)]
    else:
        log.debug('!jamo')
        sent_hcls = sent_hcls + [hcl.NonHangulLetter(cur_han)]

    if (next_han):
        cur_hcl = sent_hcls[-1]
        if (type(cur_hcl) is hcl.NonHangulLetter or \
            (cur_hcl.is_full() and (util.is_whole_hangul_letter(next_han) or \
                util.is_hangul_jamo(next_han)))):
            sent_hcls = sent_hcls + [hcl.HangulLetter()]
    
    log.debug(sent_han)
    log.debug(sent_hcls)
    log.debug()

log.info("ipa: {}".format(sent_ipa_org))
log.info("han: {}".format(sent_han_org))
log.info("hcl: {}".format(sent_hcls))
