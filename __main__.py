#!/usr/bin/python3

import interface as api
import argparse
import logging as log
import os

import drawing as dr
import translit as tr

parser = argparse.ArgumentParser()
parser.add_argument('eng_sent', type=str, help="Sentence in English")
parser.add_argument('--file', '-f', type=bool, default=False, help="Read from file and convert one line at a time")
parser.add_argument('--draw', '-d', type=bool, default=True, help="Draw Hangul sentence")
parser.add_argument('--draw-output', '-o', type=str, default="", help="Draw output filename (empty: screen)")
parser.add_argument('--standard-hangul', '-s', type=bool, default=False, help="Print in the standard Hangul")
parser.add_argument('--annotation', '-a', type=bool, default=True, help="With consonant annotations")
parser.add_argument('--self-consonants', '-c', type=bool, default=True, help="With self consonants")
args = parser.parse_args()

if (args.standard_hangul):
    args.annotation = False
    args.self_consonants = False

if (os.path.isfile(args.eng_sent)):
    args.file = True

eng_sents = []
if (args.file):
    with open(args.eng_sent, 'r') as f:
        eng_sents = [sent.strip() for sent in f.readlines()];
else:
    eng_sents = [args.eng_sent]

if (args.draw and args.draw_output):
    _split = args.draw_output.split('.')
    _dirname = os.path.dirname(args.draw_output)
    if (_dirname and not os.path.isdir(_dirname)):
        if (os.path.exists(_dirname)):
            log.critical("Output directory exists")
            exit
        else:
            os.mkdir(_dirname)

for i, eng_sent in enumerate(eng_sents):
    log.info("Converting {}/{}...".format(i+1, len(eng_sents)))

    ipa_sent = api.convert(eng_sent, from_unit="eng", to_unit="ipa")
    hcl_sent = api.convert(ipa_sent, from_unit="ipa", to_unit="hcl")
    han_sent = api.convert(hcl_sent, from_unit="hcl", to_unit="han")

    log.info("ipa: {}".format(ipa_sent))
    log.info("han: {}".format(han_sent))
    log.info("hcl: {}".format(hcl_sent))
    log.info("hfu: {}".format(han_sent))

    if (args.draw):
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
