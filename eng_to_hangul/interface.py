#!/usr/bin/python3

import logging as log

from . import drawing as dr
from . import translit as tr

logger = log.getLogger()
logger.setLevel(log.INFO)

ch = log.StreamHandler()
formatter = log.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def convert(sent, from_unit="eng", to_unit="han", options={}):
    if not (from_unit == "eng" and to_unit in ["ipa", "hcl", "han"]) and \
       not (from_unit == "ipa" and to_unit in ["hcl", "han"]) and \
       not (from_unit == "hcl" and to_unit in ["han"]):
           log.error("unsupported conversion: '{}' to '{}'".format(from_unit, to_unit))
           return None
    
    cur_sent = sent
    cur_from = from_unit
    while (cur_from != to_unit):
        trans = getattr(tr, cur_from + "_to_" + to_unit)
        cur_sent = trans(cur_sent, options)

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
