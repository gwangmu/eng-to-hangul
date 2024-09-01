#!/usr/bin/python3

import matplotlib
matplotlib.use("TkAgg", force=True)

import logging as log
import matplotlib.lines as lines
import matplotlib.pyplot as plt

from . import hclasses as hcl
from . import tables

tune_cons_w_vowel = {
    'ㅍ': {
        None: ((0.05, 0.15), (0.95, 0.85)),
        'ㅏ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅐ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅑ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅒ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅓ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅔ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅕ': ((0.00, 0.00), (0.78, 1.00)),
        'ㅖ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅗ': ((0.04, 0.25), (0.96, 0.75)),
        'ㅘ': ((0.00, 0.32), (0.75, 0.68)),
        'ㅙ': ((0.00, 0.33), (0.60, 0.67)),
        'ㅚ': ((0.00, 0.33), (0.80, 0.67)),
        'ㅛ': ((0.06, 0.26), (0.92, 0.74)),
        'ㅜ': ((0.04, 0.37), (0.96, 0.63)),
        'ㅝ': ((0.00, 0.37), (0.78, 0.63)),
        'ㅞ': ((0.00, 0.38), (0.62, 0.62)),
        'ㅟ': ((0.00, 0.38), (0.78, 0.62)),
        'ㅠ': ((0.03, 0.38), (0.97, 0.62)),
        'ㅡ': ((0.03, 0.22), (0.97, 0.78)),
        'ㅢ': ((0.00, 0.30), (0.83, 0.70)),
        'ㅣ': ((0.00, 0.00), (0.85, 1.00)),
    },
    'ㅂ': {
        None: ((0.05, 0.15), (0.95, 0.85)),
        'ㅏ': ((0.00, 0.00), (0.70, 1.00)),
        'ㅐ': ((0.00, 0.00), (0.60, 1.00)),
        'ㅑ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅒ': ((0.00, 0.00), (0.60, 1.00)),
        'ㅓ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅔ': ((0.00, 0.00), (0.57, 1.00)),
        'ㅕ': ((0.00, 0.00), (0.68, 1.00)),
        'ㅖ': ((0.00, 0.00), (0.57, 1.00)),
        'ㅗ': ((0.02, 0.25), (0.98, 0.75)),
        'ㅘ': ((0.00, 0.31), (0.75, 0.69)),
        'ㅙ': ((0.00, 0.32), (0.63, 0.68)),
        'ㅚ': ((0.00, 0.33), (0.80, 0.67)),
        'ㅛ': ((0.06, 0.24), (0.92, 0.76)),
        'ㅜ': ((0.02, 0.37), (0.98, 0.63)),
        'ㅝ': ((0.00, 0.39), (0.78, 0.61)),
        'ㅞ': ((0.00, 0.40), (0.63, 0.60)),
        'ㅟ': ((0.00, 0.37), (0.78, 0.63)),
        'ㅠ': ((0.02, 0.38), (0.97, 0.62)),
        'ㅡ': ((0.02, 0.20), (0.98, 0.80)),
        'ㅢ': ((0.00, 0.28), (0.85, 0.72)),
        'ㅣ': ((0.00, 0.00), (0.65, 1.00)),
    },
    'ㅈ': {
        None: ((0.05, 0.20), (0.95, 0.80)),
        'ㅏ': ((0.00, 0.00), (0.72, 1.00)),
        'ㅐ': ((0.00, 0.00), (0.56, 1.00)),
        'ㅑ': ((0.00, 0.00), (0.72, 1.00)),
        'ㅒ': ((0.00, 0.00), (0.56, 1.00)),
        'ㅓ': ((0.00, 0.00), (0.73, 1.00)),
        'ㅔ': ((0.00, 0.00), (0.56, 1.00)),
        'ㅕ': ((0.00, 0.00), (0.73, 1.00)),
        'ㅖ': ((0.00, 0.00), (0.56, 1.00)),
        'ㅗ': ((0.03, 0.26), (0.97, 0.74)),
        'ㅘ': ((0.00, 0.27), (0.77, 0.73)),
        'ㅙ': ((0.00, 0.34), (0.61, 0.66)),
        'ㅚ': ((0.00, 0.34), (0.80, 0.66)),
        'ㅛ': ((0.00, 0.22), (1.00, 0.78)),
        'ㅜ': ((0.01, 0.40), (0.99, 0.60)),
        'ㅝ': ((0.00, 0.35), (0.80, 0.65)),
        'ㅞ': ((0.00, 0.35), (0.60, 0.65)),
        'ㅟ': ((0.00, 0.35), (0.75, 0.65)),
        'ㅠ': ((0.00, 0.43), (1.00, 0.57)),
        'ㅡ': ((0.03, 0.20), (0.97, 0.80)),
        'ㅢ': ((0.00, 0.27), (0.80, 0.73)),
        'ㅣ': ((0.00, 0.00), (0.72, 1.00)),
    },
    'ㄹ': {
        None: ((0.00, 0.17), (1.00, 0.83)),
        'ㅏ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅐ': ((-.04, 0.00), (0.65, 1.00)),
        'ㅑ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅒ': ((-.04, 0.00), (0.65, 1.00)),
        'ㅓ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅔ': ((-.04, 0.00), (0.65, 1.00)),
        'ㅕ': ((0.00, 0.00), (0.65, 1.00)),
        'ㅖ': ((-.04, 0.00), (0.65, 1.00)),
        'ㅗ': ((0.08, 0.22), (0.92, 0.78)),
        'ㅘ': ((0.01, 0.29), (0.76, 0.71)),
        'ㅙ': ((0.00, 0.29), (0.75, 0.71)),
        'ㅚ': ((0.04, 0.27), (0.71, 0.73)),
        'ㅛ': ((0.08, 0.24), (0.92, 0.76)),
        'ㅜ': ((0.08, 0.40), (0.92, 0.60)),
        'ㅝ': ((0.04, 0.42), (0.69, 0.58)),
        'ㅞ': ((0.00, 0.42), (0.75, 0.58)),
        'ㅟ': ((0.04, 0.41), (0.71, 0.59)),
        'ㅠ': ((0.06, 0.42), (0.94, 0.59)),
        'ㅡ': ((0.06, 0.22), (0.94, 0.78)),
        'ㅢ': ((0.03, 0.28), (0.97, 0.72)),
        'ㅣ': ((0.00, 0.00), (0.65, 1.00)),
    },
    'ㄷ': {
        None: ((0.00, 0.10), (1.00, 0.90)),
        'ㅏ': ((0.00, 0.13), (0.65, 0.87)),
        'ㅐ': ((-.05, 0.10), (0.65, 0.90)),
        'ㅑ': ((0.00, 0.11), (0.65, 0.89)),
        'ㅒ': ((-.04, 0.11), (0.65, 0.89)),
        'ㅓ': ((0.00, 0.10), (0.65, 0.90)),
        'ㅔ': ((-.04, 0.10), (0.65, 0.90)),
        'ㅕ': ((0.00, 0.10), (0.65, 0.90)),
        'ㅖ': ((-.04, 0.14), (0.65, 0.86)),
        'ㅗ': ((0.06, 0.28), (0.94, 0.72)),
        'ㅘ': ((0.00, 0.39), (0.75, 0.61)),
        'ㅙ': ((0.00, 0.39), (0.75, 0.61)),
        'ㅚ': ((0.04, 0.39), (0.75, 0.61)),
        'ㅛ': ((0.08, 0.35), (0.92, 0.65)),
        'ㅜ': ((0.08, 0.46), (0.92, 0.54)),
        'ㅝ': ((0.04, 0.46), (0.71, 0.54)),
        'ㅞ': ((0.00, 0.46), (0.75, 0.54)),
        'ㅟ': ((0.04, 0.46), (0.71, 0.54)),
        'ㅠ': ((0.08, 0.46), (0.92, 0.54)),
        'ㅡ': ((0.06, 0.28), (0.94, 0.72)),
        'ㅢ': ((0.04, 0.40), (0.96, 0.60)),
        'ㅣ': ((0.00, 0.10), (0.65, 0.90)),
    },
    'ㄸ': {
        None: ((0.00, 0.10), (1.00, 0.90)),
        'ㅏ': ((-.02, 0.04), (0.65, 0.87)),
        'ㅐ': ((-.05, 0.06), (0.65, 0.90)),
        'ㅑ': ((-.02, 0.02), (0.65, 0.89)),
        'ㅒ': ((-.04, 0.03), (0.65, 0.89)),
        'ㅓ': ((-.02, 0.05), (0.65, 0.90)),
        'ㅔ': ((-.05, 0.05), (0.65, 0.90)),
        'ㅕ': ((-.02, 0.05), (0.65, 0.90)),
        'ㅖ': ((-.04, 0.06), (0.65, 0.86)),
        'ㅗ': ((0.04, 0.28), (0.94, 0.72)),
        'ㅘ': ((-.02, 0.39), (0.75, 0.61)),
        'ㅙ': ((-.02, 0.39), (0.75, 0.61)),
        'ㅚ': ((0.02, 0.37), (0.75, 0.61)),
        'ㅛ': ((0.03, 0.36), (0.92, 0.65)),
        'ㅜ': ((0.03, 0.44), (0.92, 0.54)),
        'ㅝ': ((0.02, 0.42), (0.71, 0.54)),
        'ㅞ': ((-.02, 0.42), (0.75, 0.54)),
        'ㅟ': ((0.02, 0.42), (0.71, 0.54)),
        'ㅠ': ((0.04, 0.44), (0.92, 0.54)),
        'ㅡ': ((0.04, 0.24), (0.94, 0.72)),
        'ㅢ': ((0.02, 0.36), (0.96, 0.60)),
        'ㅣ': ((-.02, 0.06), (0.65, 0.90)),
    },
}

def draw(sent_hcl, output=None):
    log.debug("## Draw")

    MAGN_FACTOR = 1.5
    VERTICAL_PAD = 30 * MAGN_FACTOR
    HORIZONTAL_PAD = 40 * MAGN_FACTOR
    FONTBOX_SIZE = 28 * MAGN_FACTOR
    FONTBOX_YOFF = 4 * MAGN_FACTOR
    ANNO_THICK = 1.7 * MAGN_FACTOR

    plt.rcParams['font.family'] = 'UnDotum'
    plt.rcParams['font.size'] = str(FONTBOX_SIZE*0.75)
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['toolbar'] = 'None'

    fig, ax = plt.subplots(frameon=False)
    ax.set_axis_off()

    num_nls = sum(1 for c in sent_hcl if isinstance(c, hcl.NonHangulLetter) and c.value == '\n')

    cur_x = HORIZONTAL_PAD
    cur_y = VERTICAL_PAD + num_nls * FONTBOX_SIZE
    max_x = HORIZONTAL_PAD
    for i, letter in enumerate(sent_hcl):
        han = letter.get_str_wo_anno()
        next_x = cur_x + FONTBOX_SIZE

        overall_trans_off = (0.00, 0.00)
        overall_scale_factor = 1

        if (type(letter) is hcl.NonHangulLetter):
            if (letter.value == '\n'):
                cur_x = HORIZONTAL_PAD
                cur_y = cur_y - FONTBOX_SIZE
                continue
            elif (letter.value in ['.', ',', "'", '"']):
                next_x = cur_x + FONTBOX_SIZE * 0.3
            else:
                next_x = cur_x + FONTBOX_SIZE * 0.5
        elif (type(letter) is hcl.HangulLetter):
            if (letter.is_self_consonant()):
                overall_trans_off = (0.00, -0.10)
                overall_scale_factor = 0.8
                next_x = cur_x + FONTBOX_SIZE * 0.8

        max_x = max(next_x, max_x)

        # Draw guide box
        #p = plt.Rectangle((cur_x, cur_y), next_x - cur_x, FONTBOX_SIZE, fill=False, transform=None, clip_on=False)
        #ax.add_patch(p)

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

                if (not letter.initial.is_none()):
                    tune_off, tune_scale = tune_cons_w_vowel[letter.initial.value][letter.vowel.value]
                    assert(tune_off and tune_scale)
                    apply_rel_off(tune_off[0], tune_off[1])
                    apply_rel_scale(tune_scale[0], tune_scale[1])

                if (not letter.final.is_none()):
                    apply_rel_off(0.00, 0.30)
                    apply_rel_scale(1.00, 0.70)
                    if (letter.final.value == 'ㄴ'):
                        trans_off = (trans_off[0], trans_off[1]-0.10)
                        trans_scale = (trans_scale[0], trans_scale[1]+0.10)

                vert_pos_rel = map(lambda v: (v[0]*trans_scale[0]+trans_off[0]+overall_trans_off[0], v[1]*trans_scale[1]+trans_off[1]+overall_trans_off[1]), vert_pos_rel)
                vert_pos_rel = map(lambda v: (v[0]*FONTBOX_SIZE*overall_scale_factor+cur_x, v[1]*FONTBOX_SIZE*overall_scale_factor+cur_y), vert_pos_rel)

                vert_pos_rel = list(map(list, zip(*vert_pos_rel)))
                log.debug(vert_pos_rel)
                line = lines.Line2D(vert_pos_rel[0], vert_pos_rel[1], lw=ANNO_THICK, color='black', transform=None, clip_on=False)
                ax.add_line(line)

            # TODO: handle final consonants with annotations (if any).
            assert(not letter.final.has_anno())

        cur_x = next_x

    px = 1 / plt.rcParams['figure.dpi']
    fig_width = (HORIZONTAL_PAD + max_x)*px
    fig_height = (VERTICAL_PAD * 2 + FONTBOX_SIZE * (num_nls + 1))*px
    fig.set_size_inches(fig_width, fig_height)
    #fig.canvas.manager.window.overrideredirect(1)

    if (not output):
        plt.show()
    else:
        plt.savefig(output)
