#!/usr/bin/python3

import argparse
import eng_to_ipa as ipa
import logging as log
import matplotlib.lines as lines
import matplotlib.pyplot as plt

import tables
import util
import hclasses as hcl

parser = argparse.ArgumentParser()
parser.add_argument('sent_eng', type=str, help="Sentence in English")
args = parser.parse_args()

log.basicConfig(level=log.INFO)

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
    log.debug("")

sent_han_fuse = ''.join(x.get_str_wo_anno() for x in sent_hcls)

log.info("ipa: {}".format(sent_ipa_org))
log.info("han: {}".format(sent_han_org))
log.info("hcl: {}".format(sent_hcls))
log.info("hfu: {}".format(sent_han_fuse))

# Draw Hangul letters.
log.debug("## Draw")

VERTICAL_PAD = 20
HORIZONTAL_PAD = 40
FONTBOX_SIZE = 28
FONTBOX_YOFF = 4

plt.rcParams['font.family'] = 'UnDotum'
plt.rcParams['font.size'] = str(FONTBOX_SIZE*0.75)
plt.rcParams['axes.unicode_minus'] = False

px = 1/plt.rcParams['figure.dpi']
fig, ax = plt.subplots(figsize=((40+len(sent_han_fuse)*FONTBOX_SIZE)*px, (HORIZONTAL_PAD*2+FONTBOX_SIZE)*px))
ax.set_axis_off()

for i, letter in enumerate(sent_hcls):
    han = letter.get_str_wo_anno()
    cur_x = VERTICAL_PAD+i*FONTBOX_SIZE
    cur_y = HORIZONTAL_PAD
    ax.text(cur_x, cur_y+FONTBOX_YOFF, han, transform=None)
    p = plt.Rectangle((cur_x, cur_y), FONTBOX_SIZE, FONTBOX_SIZE, fill=False, transform=None, clip_on=False)
    ax.add_patch(p)

    if (type(letter) is hcl.HangulLetter):
        if (letter.initial.has_anno()):
            vert_pos_rel=[]
            if (letter.initial.value in ['ㅂ', 'ㅍ']):
                vert_pos_rel = [[0.45, 0.20], [0.55, 0.20]]
            elif (letter.initial.value in ['ㄹ', 'ㄷ', 'ㄸ']):
                vert_pos_rel = [[0.02, 0.20], [0.02, 0.30]]
            elif (letter.initial.value in ['ㅈ']):
                vert_pos_rel = [[0.50, 0.45], [0.54, 0.45]]

            if (not letter.final.is_none()):
                trans_off = (0.00, 0.40)
                trans_scale = (0.70, 0.60)
            elif (not letter.vowel.is_none()):
                trans_off = (0.00, 0.40)
                trans_scale = (1.00, 0.60)
            else:
                trans_off = (0.00, 0.00)
                trans_scale = (1.00, 1.00)

            vert_pos_rel = map(lambda v: (v[0]*trans_scale[0]+trans_off[0], v[1]*trans_scale[1]+trans_off[1]), vert_pos_rel)
            vert_pos_rel = map(lambda v: (v[0]*FONTBOX_SIZE+cur_x, v[1]*FONTBOX_SIZE+cur_y), vert_pos_rel)

            vert_pos_rel = list(map(list, zip(*vert_pos_rel)))
            print(vert_pos_rel)
            line = lines.Line2D(vert_pos_rel[0], vert_pos_rel[1], lw=2, color='r', transform=None, clip_on=False)
            ax.add_line(line)

plt.show()
