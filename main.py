#!/usr/bin/python3

import eng_to_ipa as ipa
import argparse

ipa_to_han = {
    # Two-symbol transcription
    2: {
        "eɪ": "ㅔ이", 
        "aʊ": "ㅏ우",
        "aɪ": "ㅏ이", 
        "ər": "ㅓ얼", 
        "oʊ": "ㅗ우", 
        "ɔɪ": "ㅗ이", 
        "əʊ": "ㅓ우",
        "ts": "ㅊ",
        "wɑ": "와",
        "wə": "워",
        "ʃə": "셔",
    },
    # Single-symbol transcription
    1: {
        "ʤ": "ㅈ", 
        "ʧ": "ㅊ",
        "æ": "ㅐ", 
        "a": "ㅏ",
        "b": "ㅂ",
        "d": "ㄷ",
        "e": "ㅔ",
        "f": "`ㅍ",
        "g": "ㄱ",
        "i": "ㅣ",
        "k": "ㅋ",
        "l": "ㄹ",
        "m": "ㅁ",
        "n": "ㄴ",
        "o": "ㅗ",
        "p": "ㅍ",
        "q": "ㅋ",
        "r": "`ㄹ",
        "s": "ㅅ",
        "t": "ㅌ",
        "v": "`ㅂ",
        "w": "ㅜ",
        "x": "ㅋㅅ",
        "z": "`ㅈ",
        "ə": "ㅓ",
        "ɑ": "ㅏ",
        "ɔ": "ㅗ",
        "ð": "`ㄷ",
        "ɛ": "ㅔ",
        "h": "ㅎ",
        "ɪ": "ㅣ",
        "ŋ": "ㅇ응",
        "ʃ": "쉬",
        "θ": "`ㄸ",
        "ʊ": "ㅜ",
        "u": "ㅜ",
        "ʒ": "ㅈ",
        "i": "ㅣ",
        "j": "ㅠ",
    }}

ipa_nums = sorted(ipa_to_han.keys(), reverse=True)

parser = argparse.ArgumentParser()
parser.add_argument('sent_eng', type=str, help="Sentence in English")
args = parser.parse_args()

sent_eng = args.sent_eng
sent_ipa = ipa.convert(sent_eng, keep_punct=False)
sent_ipa_org = sent_ipa

trans_steps = []
sent_han = ""
while (sent_ipa):
    # Carry over spaces.
    if (sent_ipa[0:1] == " "):
        sent_han = sent_han + " "
        sent_ipa = sent_ipa[1:]

    # Ignore stresses for now.
    if (sent_ipa[0:1] == "ˈ" or sent_ipa[0:1] == "ˌ"):
        sent_ipa = sent_ipa[1:]

    # Transcribe IPA symbols, longer symbol sets first.
    for ipa_num in ipa_nums + [-1]:
        if (ipa_num == -1): 
            print("error: unrecognized IPA symbol '{}'".format(sent_ipa[0:1]))
            print("error: transcription steps;")
            for i, trans_step in enumerate(trans_steps):
                print("{}: {}".format(i, trans_step))
            exit
        if (sent_ipa[0:ipa_num] in ipa_to_han[ipa_num].keys()):
            sent_han = sent_han + ipa_to_han[ipa_num][sent_ipa[0:ipa_num]]
            sent_ipa = sent_ipa[ipa_num:]
            break

    trans_steps = trans_steps + [sent_ipa, sent_han]

print("IPA: {}".format(sent_ipa_org))
print("Han: {}".format(sent_han))
