#!/usr/bin/python3

import argparse
import logging as log
import os

import drawing as dr
import translit as tr

parser = argparse.ArgumentParser()
parser.add_argument('eng_sent', type=str, help="Sentence in English")
parser.add_argument('--file', '-f', type=bool, default=False, help="Read from file and convert one line at a time")
parser.add_argument('--standard-hangul', '-s', type=bool, default=False, help="Print in the standard Hangul")
parser.add_argument('--annotation', '-a', type=bool, default=True, help="With consonant annotations")
parser.add_argument('--self-consonants', '-c', type=bool, default=True, help="With self consonants")
args = parser.parse_args()

if (args.standard_hangul):
    args.annotation = False
    args.self_consonants = False

if (os.path.isfile(args.eng_sent)):
    args.file = True

log.basicConfig(level=log.INFO)

def convert(sent, from_unit="eng", to_unit="han"):
    if not (from_unit == "eng" and to_unit in ["ipa", "hcl", "han"]) and \
       not (from_unit == "ipa" and to_unit in ["hcl", "han"]) and \
       not (from_unit == "hcl" and to_unit in ["han"]):
           log.error("unsupported conversion: '{}' to '{}'".format(from_unit, to_unit))
           return None
    
    cur_sent = sent
    cur_from = from_unit
    while (cur_from != to_unit):
        trans = getattr(tr, cur_from + "_to_" + to_unit)
        cur_sent = trans(cur_sent)

        if (cur_from == "eng"):
            cur_from = "ipa"
        elif (cur_from == "ipa"):
            cur_from = "hcl"
        elif (cur_from == "hcl"):
            cur_from = "han"
        else:
            log.critical("bogus conversion from '{}'".format(cur_from))
            exit

    return cur_sent

def draw(hcl_sent, output=None):
    dr.draw(hcl_sent, output)

eng_sents = []
if (args.file):
    with open(args.eng_sent, 'r') as f:
        eng_sents = [sent.strip() for sent in f.readlines()];
else:
    eng_sents = [args.eng_sent]

for i, eng_sent in enumerate(eng_sents):
    log.info("Converting {}/{}...".format(i+1, len(eng_sents)))

    ipa_sent = convert(eng_sent, from_unit="eng", to_unit="ipa")
    hcl_sent = convert(ipa_sent, from_unit="ipa", to_unit="hcl")
    han_sent = convert(hcl_sent, from_unit="hcl", to_unit="han")

    log.info("ipa: {}".format(ipa_sent))
    log.info("han: {}".format(han_sent))
    log.info("hcl: {}".format(hcl_sent))
    log.info("hfu: {}".format(han_sent))

    draw(hcl_sent)
