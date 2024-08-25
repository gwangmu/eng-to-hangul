#!/usr/bin/python3

import logging as log
import matplotlib.lines as lines
import matplotlib.pyplot as plt

import hclasses as hcl
import tables
import util

def draw(sent_hcl, output=None):
    log.debug("## Draw")

    VERTICAL_PAD = 30
    HORIZONTAL_PAD = 40
    FONTBOX_SIZE = 28
    FONTBOX_YOFF = 4

    plt.rcParams['font.family'] = 'UnDotum'
    plt.rcParams['font.size'] = str(FONTBOX_SIZE*0.75)
    plt.rcParams['axes.unicode_minus'] = False

    px = 1/plt.rcParams['figure.dpi']
    fig_width = (VERTICAL_PAD*2+len(sent_hcl)*FONTBOX_SIZE)*px
    fig_height = (HORIZONTAL_PAD*2+FONTBOX_SIZE)*px
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.set_axis_off()

    cur_x = VERTICAL_PAD
    cur_y = HORIZONTAL_PAD
    for i, letter in enumerate(sent_hcl):
        han = letter.get_str_wo_anno()
        next_x = cur_x + FONTBOX_SIZE

        # Draw guide box
        #p = plt.Rectangle((cur_x, cur_y), FONTBOX_SIZE, FONTBOX_SIZE, fill=False, transform=None, clip_on=False)
        #ax.add_patch(p)

        overall_trans_off = (0.00, 0.00)
        overall_scale_factor = 1

        if (type(letter) is hcl.NonHangulLetter):
            next_x = cur_x + FONTBOX_SIZE * 0.5
        elif (type(letter) is hcl.HangulLetter):
            if (letter.is_self_consonant()):
                overall_trans_off = (0.00, -0.10)
                overall_scale_factor = 0.8
                next_x = cur_x + FONTBOX_SIZE * 0.8

            if (letter.initial.has_anno()):
                vert_pos_rel=[]
                if (letter.initial.value in ['ㅂ', 'ㅍ']):
                    vert_pos_rel = [[0.45, 0.25], [0.55, 0.25]]
                elif (letter.initial.value in ['ㄹ', 'ㄷ', 'ㄸ']):
                    vert_pos_rel = [[0.05, 0.23], [0.05, 0.33]]
                elif (letter.initial.value in ['ㅈ']):
                    vert_pos_rel = [[0.50, 0.40], [0.54, 0.40]]

                trans_off = (0.00, 0.00)
                trans_scale = (1.00, 1.00)

                def apply_rel_off(rel_w, rel_h):
                    nonlocal trans_off
                    trans_off = (trans_off[0] + (1-trans_off[0])*rel_w, trans_off[1] + (1-trans_off[1])*rel_h)

                def apply_rel_scale(rel_w, rel_h):
                    nonlocal trans_scale
                    trans_scale = (trans_scale[0]*rel_w, trans_scale[1]*rel_h)

                if (not letter.final.is_none()):
                    apply_rel_off(0.00, 0.25)
                    apply_rel_scale(1.00, 0.75)

                if (not letter.vowel.is_none()):
                    if (letter.vowel.value in tables.wide_han_vowel):
                        apply_rel_off(0.00, 0.25)
                        apply_rel_scale(0.75, 0.75)
                    elif (letter.vowel.value in tables.vertical_han_vowel):
                        apply_rel_off(0.00, 0.00)
                        apply_rel_scale(0.75, 1.00)
                    elif (letter.vowel.value in tables.horizontal_han_vowel):
                        apply_rel_off(0.00, 0.25)
                        apply_rel_scale(1.00, 0.75)

                if (not letter.final.is_none() and letter.final.value == 'ㄴ'):
                    print(trans_off, trans_scale)
                    trans_off = (trans_off[0], trans_off[1]-0.18)
                    trans_scale = (trans_scale[0]+0.15, trans_scale[1]+0.1)
                    print(trans_off, trans_scale)

                vert_pos_rel = map(lambda v: (v[0]*trans_scale[0]+trans_off[0]+overall_trans_off[0], v[1]*trans_scale[1]+trans_off[1]+overall_trans_off[1]), vert_pos_rel)
                vert_pos_rel = map(lambda v: (v[0]*FONTBOX_SIZE*overall_scale_factor+cur_x, v[1]*FONTBOX_SIZE*overall_scale_factor+cur_y), vert_pos_rel)

                vert_pos_rel = list(map(list, zip(*vert_pos_rel)))
                log.debug(vert_pos_rel)
                line = lines.Line2D(vert_pos_rel[0], vert_pos_rel[1], lw=1.5, color='black', transform=None, clip_on=False)
                ax.add_line(line)
        
        plt.rcParams['font.size'] = str(FONTBOX_SIZE*overall_scale_factor*0.75)
        ax.text(cur_x+FONTBOX_SIZE*overall_trans_off[0], cur_y+FONTBOX_YOFF+FONTBOX_SIZE*overall_trans_off[1], han, transform=None)
        plt.rcParams['font.size'] = str(FONTBOX_SIZE*0.75)

        cur_x = next_x

    fig_width = (VERTICAL_PAD+cur_x)*px
    fig.set_size_inches(fig_width, fig_height)

    if (not output):
        plt.show()
    else:
        plt.savefig(output)
