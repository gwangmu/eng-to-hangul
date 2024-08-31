#!/usr/bin/python3

import logging as log
import matplotlib.lines as lines
import matplotlib.pyplot as plt

import hclasses as hcl
import tables
import util

tune_cons_w_vowel = {
    'ㅍ': {
        'ㅏ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅐ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅑ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅒ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅓ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅔ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅕ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅖ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅗ': ((0.10, 0.26), (0.90, 0.74)),
        'ㅘ': ((0.00, 0.30), (0.80, 0.70)),
        'ㅙ': ((0.00, 0.28), (0.72, 0.72)),
        'ㅚ': ((0.00, 0.30), (0.80, 0.70)),
        'ㅛ': ((0.10, 0.26), (0.90, 0.74)),
        'ㅜ': ((0.05, 0.35), (0.95, 0.65)),
        'ㅝ': ((0.00, 0.32), (0.78, 0.68)),
        'ㅞ': ((0.00, 0.28), (0.68, 0.72)),
        'ㅟ': ((0.00, 0.32), (0.78, 0.68)),
        'ㅠ': ((0.05, 0.35), (0.95, 0.65)),
        'ㅡ': ((0.10, 0.15), (0.90, 0.85)),
        'ㅢ': ((0.00, 0.25), (0.85, 0.75)),
        'ㅣ': ((0.00, 0.00), (0.85, 1.00)),
    },
    'ㅂ': {
        'ㅏ': ((0.00, 0.00), (0.72, 1.00)),
        'ㅐ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅑ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅒ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅓ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅔ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅕ': ((0.00, 0.00), (0.74, 1.00)),
        'ㅖ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅗ': ((0.10, 0.26), (0.90, 0.74)),
        'ㅘ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅙ': ((0.00, 0.28), (0.72, 0.72)),
        'ㅚ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅛ': ((0.10, 0.26), (0.90, 0.74)),
        'ㅜ': ((0.05, 0.35), (0.95, 0.65)),
        'ㅝ': ((0.00, 0.32), (0.78, 0.68)),
        'ㅞ': ((0.00, 0.32), (0.68, 0.68)),
        'ㅟ': ((0.00, 0.32), (0.78, 0.68)),
        'ㅠ': ((0.05, 0.35), (0.95, 0.65)),
        'ㅡ': ((0.10, 0.15), (0.90, 0.85)),
        'ㅢ': ((0.00, 0.25), (0.85, 0.75)),
        'ㅣ': ((0.00, 0.00), (0.75, 1.00)),
    },
    'ㅈ': {
        'ㅏ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅐ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅑ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅒ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅓ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅔ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅕ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅖ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅗ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅘ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅙ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅚ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅛ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅜ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅝ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅞ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅟ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅠ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅡ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅢ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅣ': ((0.00, 0.00), (0.65, 1.00)),
    },
    'ㄹ': {
        'ㅏ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅐ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅑ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅒ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅓ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅔ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅕ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅖ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅗ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅘ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅙ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅚ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅛ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅜ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅝ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅞ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅟ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅠ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅡ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅢ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅣ': ((0.00, 0.00), (0.65, 1.00)),
    },
    'ㄷ': {
        'ㅏ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅐ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅑ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅒ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅓ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅔ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅕ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅖ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅗ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅘ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅙ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅚ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅛ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅜ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅝ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅞ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅟ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅠ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅡ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅢ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅣ': ((0.00, 0.00), (0.65, 1.00)),
    },
    'ㄸ': {
        'ㅏ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅐ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅑ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅒ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅓ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅔ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅕ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅖ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅗ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅘ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅙ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅚ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅛ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅜ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅝ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅞ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅟ': ((0.00, 0.25), (0.75, 0.75)),
        'ㅠ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅡ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅢ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅣ': ((0.00, 0.00), (0.65, 1.00)),
    },
}

def draw(sent_hcl, output=None):
    log.debug("## Draw")

    VERTICAL_PAD = 30
    HORIZONTAL_PAD = 40
    FONTBOX_SIZE = 28
    FONTBOX_YOFF = 4

    plt.rcParams['font.family'] = 'UnDotum'
    plt.rcParams['font.size'] = str(FONTBOX_SIZE*0.75)
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['toolbar'] = 'None'

    fig, ax = plt.subplots(frameon=False)
    ax.set_axis_off()

    cur_x = HORIZONTAL_PAD
    cur_y = VERTICAL_PAD
    max_x = HORIZONTAL_PAD
    for i, letter in enumerate(sent_hcl):
        han = letter.get_str_wo_anno()
        next_x = cur_x + FONTBOX_SIZE

        # Draw guide box
        #p = plt.Rectangle((cur_x, cur_y), FONTBOX_SIZE, FONTBOX_SIZE, fill=False, transform=None, clip_on=False)
        #ax.add_patch(p)

        overall_trans_off = (0.00, 0.00)
        overall_scale_factor = 1

        if (type(letter) is hcl.NonHangulLetter):
            if (letter.value == '\n'):
                # FIXME: we're going upward now.
                cur_x = HORIZONTAL_PAD
                cur_y = cur_y + FONTBOX_SIZE
                continue
            else:
                next_x = cur_x + FONTBOX_SIZE * 0.5
        elif (type(letter) is hcl.HangulLetter):
            if (letter.is_self_consonant()):
                overall_trans_off = (0.00, -0.10)
                overall_scale_factor = 0.8
                next_x = cur_x + FONTBOX_SIZE * 0.8

        max_x = max(next_x, max_x)

        plt.rcParams['font.size'] = str(FONTBOX_SIZE*overall_scale_factor*0.75)
        ax.text(cur_x+FONTBOX_SIZE*overall_trans_off[0], cur_y+FONTBOX_YOFF+FONTBOX_SIZE*overall_trans_off[1], han, transform=None)
        plt.rcParams['font.size'] = str(FONTBOX_SIZE*0.75)

        if (type(letter) is hcl.HangulLetter):
            if (letter.initial.has_anno()):
                vert_pos_rel=[]
                if (letter.initial.value in ['ㅂ', 'ㅍ']):
                    vert_pos_rel = [[0.40, 0.15], [0.60, 0.15]]
                elif (letter.initial.value in ['ㄹ', 'ㄷ', 'ㄸ']):
                    vert_pos_rel = [[0.05, 0.23], [0.05, 0.33]]
                elif (letter.initial.value in ['ㅈ']):
                    vert_pos_rel = [[0.48, 0.30], [0.54, 0.30]]

                trans_off = (0.00, 0.00)
                trans_scale = (1.00, 1.00)

                def apply_rel_off(rel_w, rel_h):
                    nonlocal trans_off
                    trans_off = (trans_off[0] + (1-trans_off[0])*rel_w, trans_off[1] + (1-trans_off[1])*rel_h)

                def apply_rel_scale(rel_w, rel_h):
                    nonlocal trans_scale
                    trans_scale = (trans_scale[0]*rel_w, trans_scale[1]*rel_h)

                if (letter.is_self_consonant()):
                    if (letter.initial.value in ['ㅂ', 'ㅍ']): 
                        apply_rel_off(0.10, 0.15)
                        apply_rel_scale(0.90, 0.85)
                    elif (letter.initial.value in ['ㅈ']): 
                        apply_rel_off(0.00, 0.20)
                        apply_rel_scale(1.00, 0.80)

                if (not letter.final.is_none()):
                    apply_rel_off(0.00, 0.30)
                    apply_rel_scale(1.00, 0.70)
                    if (letter.final.value == 'ㄴ'):
                        trans_off = (trans_off[0], trans_off[1]-0.10)
                        trans_scale = (trans_scale[0], trans_scale[1]+0.10)

                if (not letter.vowel.is_none()):
                    tune_off, tune_scale = tune_cons_w_vowel[letter.initial.value][letter.vowel.value]
                    assert(tune_off and tune_scale)
                    apply_rel_off(tune_off[0], tune_off[1])
                    apply_rel_scale(tune_scale[0], tune_scale[1])

                vert_pos_rel = map(lambda v: (v[0]*trans_scale[0]+trans_off[0]+overall_trans_off[0], v[1]*trans_scale[1]+trans_off[1]+overall_trans_off[1]), vert_pos_rel)
                vert_pos_rel = map(lambda v: (v[0]*FONTBOX_SIZE*overall_scale_factor+cur_x, v[1]*FONTBOX_SIZE*overall_scale_factor+cur_y), vert_pos_rel)

                vert_pos_rel = list(map(list, zip(*vert_pos_rel)))
                log.debug(vert_pos_rel)
                line = lines.Line2D(vert_pos_rel[0], vert_pos_rel[1], lw=1.5, color='black', transform=None, clip_on=False)
                ax.add_line(line)

            # TODO
            if (letter.final.has_anno()):
                pass

        cur_x = next_x

    px = 1/plt.rcParams['figure.dpi']
    fig_width = (HORIZONTAL_PAD+max_x)*px
    fig_height = (VERTICAL_PAD+FONTBOX_SIZE+cur_y)*px
    fig.set_size_inches(fig_width, fig_height)

    if (not output):
        plt.show()
    else:
        plt.savefig(output)
