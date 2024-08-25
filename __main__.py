#!/usr/bin/python3

import interface as api
import argparse
import logging as log
import os

import drawing as dr
import translit as tr

parser = argparse.ArgumentParser()
parser.add_argument('eng_sent', type=str, help="Sentence in English")
parser.add_argument('--file-input', '-f', action='store_true', help="Read from file and convert one line at a time")
parser.add_argument('--no-draw', '-D', action='store_true', help="Don't draw Hangul sentence")
parser.add_argument('--draw-output', '-o', type=str, default="", help="Draw output filename (empty: screen)")
parser.add_argument('--standard-hangul', '-s', action='store_true', help="Print in the standard Hangul")
parser.add_argument('--no-annotation', '-A', action='store_true', help="With consonant annotations")
parser.add_argument('--no-self-consonants', '-C', action='store_true', help="With self consonants")
args = parser.parse_args()

# Some convenience features
if (args.standard_hangul):
    args.no_annotation = False
    args.no_self_consonants = False

if (os.path.isfile(args.eng_sent)):
    args.file_input = True

if (not args.no_draw and not args.draw_output):
    log.info("Note: close the figure to continue.")

# Load sentences
eng_sents = []
if (args.file_input):
    with open(args.eng_sent, 'r') as f:
        eng_sents = [sent.strip() for sent in f.readlines()];
else:
    eng_sents = [args.eng_sent]

# Prepare drawing
if (not args.no_draw and args.draw_output):
    _split = args.draw_output.split('.')
    _dirname = os.path.dirname(args.draw_output)
    if (_dirname and not os.path.isdir(_dirname)):
        if (os.path.exists(_dirname)):
            log.critical("Output directory exists")
            exit
        else:
            os.mkdir(_dirname)

# Set up the arguments to pass
pass_args = {
    "eng_to_ipa": {},
    "ipa_to_hcl": {
        "no_annotation": args.no_annotation, 
        "no_self_consonants": args.no_self_consonants,
        },
    "hcl_to_han": {},
    }

# Convert one by one
for i, eng_sent in enumerate(eng_sents):
    log.info("Converting {}/{}...".format(i+1, len(eng_sents)))

    ipa_sent = api.convert(eng_sent, "eng", "ipa", pass_args["eng_to_ipa"])
    hcl_sent = api.convert(ipa_sent, "ipa", "hcl", pass_args["ipa_to_hcl"])
    han_sent = api.convert(hcl_sent, "hcl", "han", pass_args["hcl_to_han"])

    log.info("- ipa: {}".format(ipa_sent))
    log.debug("- hlo: {}".format(han_sent))
    log.debug("- hcl: {}".format(hcl_sent))
    log.info("- han: {}".format(han_sent))

    if (not args.no_draw):
        if (not args.draw_output):
            api.draw(hcl_sent)
        else:
            if (len(eng_sents) <= 1):
                api.draw(hcl_sent, args.draw_output)
            else:
                _split_new = _split[:]
                _split_new[-2] = _split[-2] + "-" + str(i+1).zfill(3)
                filename='.'.join(_split_new)
                api.draw(hcl_sent, filename)
