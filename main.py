#!/usr/bin/python3

import argparse
import logging as log

import drawing as dr
import translit as tr

parser = argparse.ArgumentParser()
parser.add_argument('sent_eng', type=str, help="Sentence in English")
parser.add_argument('--standard-hangul', '-s', type=bool, default=False, help="Print in the standard Hangul")
parser.add_argument('--annotation', '-a', type=bool, default=True, help="With consonant annotations")
parser.add_argument('--self-consonants', '-c', type=bool, default=True, help="With self consonants")
args = parser.parse_args()

if (args.standard_hangul):
    args.annotation = False
    args.self_consonants = False

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

def draw(sent_hcl, output=None):
    dr.draw(sent_hcl, output)

sent_eng = args.sent_eng
sent_ipa = convert(sent_eng, from_unit="eng", to_unit="ipa")
sent_hcl = convert(sent_ipa, from_unit="ipa", to_unit="hcl")
sent_han = convert(sent_hcl, from_unit="hcl", to_unit="han")

log.info("ipa: {}".format(sent_ipa))
log.info("han: {}".format(sent_han))
log.info("hcl: {}".format(sent_hcl))
log.info("hfu: {}".format(sent_han))

draw(sent_hcl)
