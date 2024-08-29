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
                    vert_pos_rel = [[0.42, 0.15], [0.58, 0.15]]
                elif (letter.initial.value in ['ㄹ', 'ㄷ', 'ㄸ']):
                    vert_pos_rel = [[0.05, 0.23], [0.05, 0.33]]
                elif (letter.initial.value in ['ㅈ']):
                    vert_pos_rel = [[0.46, 0.30], [0.56, 0.30]]

                trans_off = (0.00, 0.00)
                trans_scale = (1.00, 1.00)

                def apply_rel_off(rel_w, rel_h):
                    nonlocal trans_off
                    trans_off = (trans_off[0] + (1-trans_off[0])*rel_w, trans_off[1] + (1-trans_off[1])*rel_h)

                def apply_rel_scale(rel_w, rel_h):
                    nonlocal trans_scale
                    trans_scale = (trans_scale[0]*rel_w, trans_scale[1]*rel_h)

                if (letter.is_self_consonant()):
                    apply_rel_off(0.00, 0.15)
                    apply_rel_scale(1.00, 0.85)

                if (not letter.final.is_none()):
                    apply_rel_off(0.00, 0.25)
                    apply_rel_scale(1.00, 0.75)

                if (not letter.vowel.is_none()):
                    if (letter.vowel.value in tables.wide_han_vowel):
                        apply_rel_off(0.00, 0.25)
                        apply_rel_scale(0.75, 0.75)
                    elif (letter.vowel.value in tables.vertical_han_vowel):
                        apply_rel_off(0.00, 0.00)
                        apply_rel_scale(0.65, 1.00)
                    elif (letter.vowel.value in tables.horizontal_han_vowel):
                        apply_rel_off(0.00, 0.22)
                        apply_rel_scale(1.00, 0.78)

                if (not letter.final.is_none() and letter.final.value == 'ㄴ'):
                    trans_off = (trans_off[0], trans_off[1]-0.10)
                    trans_scale = (trans_scale[0], trans_scale[1]+0.10)

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
