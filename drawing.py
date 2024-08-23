#!/usr/bin/python3

import logging as log
import matplotlib.lines as lines
import matplotlib.pyplot as plt

import hclasses as hcl
import tables

def draw(sent_hcl, output=None):
    log.debug("## Draw")

    VERTICAL_PAD = 20
    HORIZONTAL_PAD = 40
    FONTBOX_SIZE = 28
    FONTBOX_YOFF = 4

    plt.rcParams['font.family'] = 'UnDotum'
    plt.rcParams['font.size'] = str(FONTBOX_SIZE*0.75)
    plt.rcParams['axes.unicode_minus'] = False

    px = 1/plt.rcParams['figure.dpi']
    fig, ax = plt.subplots(figsize=((40+len(sent_hcl)*FONTBOX_SIZE)*px, (HORIZONTAL_PAD*2+FONTBOX_SIZE)*px))
    ax.set_axis_off()

    for i, letter in enumerate(sent_hcl):
        han = letter.get_str_wo_anno()
        cur_x = VERTICAL_PAD+i*FONTBOX_SIZE
        cur_y = HORIZONTAL_PAD

        #p = plt.Rectangle((cur_x, cur_y), FONTBOX_SIZE, FONTBOX_SIZE, fill=False, transform=None, clip_on=False)
        #ax.add_patch(p)

        overall_trans_off = (0.00, 0.00)
        overall_scale_factor = 1

        if (type(letter) is hcl.HangulLetter):
            if (not letter.initial.is_none() and letter.vowel.is_none() and letter.final.is_none()):
                overall_trans_off = (0.00, -0.10)
                overall_scale_factor = 0.8

            if (letter.initial.has_anno()):
                vert_pos_rel=[]
                if (letter.initial.value in ['ㅂ', 'ㅍ']):
                    vert_pos_rel = [[0.45, 0.25], [0.55, 0.25]]
                elif (letter.initial.value in ['ㄹ', 'ㄷ', 'ㄸ']):
                    vert_pos_rel = [[0.05, 0.23], [0.05, 0.33]]
                elif (letter.initial.value in ['ㅈ']):
                    vert_pos_rel = [[0.50, 0.40], [0.54, 0.40]]

                if (not letter.final.is_none()):
                    trans_off = (0.00, 0.40)
                    trans_scale = (0.70, 0.60)

                if (not letter.vowel.is_none()):
                    if (letter.vowel.value in tables.wide_han_vowel):
                        trans_off = (0.00, 0.25)
                        trans_scale = (0.75, 0.75)
                    elif (letter.vowel.value in tables.vertical_han_vowel):
                        trans_off = (0.00, 0.00)
                        trans_scale = (0.75, 1.00)
                    elif (letter.vowel.value in tables.horizontal_han_vowel):
                        trans_off = (0.00, 0.25)
                        trans_scale = (1.00, 0.75)
                else:
                    trans_off = (0.00, 0.00)
                    trans_scale = (1.00, 1.00)

                if (not letter.final.is_none()):
                    trans_off = (trans_off[0], trans_off[1]+0.05)
                    trans_scale = (trans_scale[0]*1.2, trans_scale[1]-0.0)

                vert_pos_rel = map(lambda v: (v[0]*trans_scale[0]+trans_off[0]+overall_trans_off[0], v[1]*trans_scale[1]+trans_off[1]+overall_trans_off[1]), vert_pos_rel)
                vert_pos_rel = map(lambda v: (v[0]*FONTBOX_SIZE*overall_scale_factor+cur_x, v[1]*FONTBOX_SIZE*overall_scale_factor+cur_y), vert_pos_rel)

                vert_pos_rel = list(map(list, zip(*vert_pos_rel)))
                print(vert_pos_rel)
                line = lines.Line2D(vert_pos_rel[0], vert_pos_rel[1], lw=1.5, color='black', transform=None, clip_on=False)
                ax.add_line(line)
        
        plt.rcParams['font.size'] = str(FONTBOX_SIZE*overall_scale_factor*0.75)
        ax.text(cur_x+FONTBOX_SIZE*overall_trans_off[0], cur_y+FONTBOX_YOFF+FONTBOX_SIZE*overall_trans_off[1], han, transform=None)
        plt.rcParams['font.size'] = str(FONTBOX_SIZE*0.75)

    if (not output):
        plt.show()
    else:
        plt.savefig(output)
