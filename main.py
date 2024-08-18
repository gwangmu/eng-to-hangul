#!/usr/bin/python3

import eng_to_ipa as ipa

ipa_to_han = {
    # Two-symbol transcription
    2: {
        "eɪ": "ㅔ이", 
        "aʊ": "ㅏ우",
        "aɪ": "ㅏ이", 
        "ər": "ㅓ얼", 
        "oʊ": "ㅗ우", 
        "ɔɪ": "ㅗ이", 
        "əʊ": "ㅓ우"},
    # Single-symbol transcription
    1: {
        "ʤ": "ㅈ", 
        "ʧ": "ㅊ",
        "æ": "ㅐ", 
        "a": "ㅏ",
        "b": "ㅂ",
        "d": "ㄷ",
        "e": "ㅔ",
        "f": "ㅍ",
        "g": "ㄱ",
        "i": "ㅣ",
        "k": "ㅋ",
        "l": "ㄹ",
        "m": "ㅁ",
        "n": "ㄴ",
        "o": "ㅗ",
        "p": "ㅍ",
        "q": "ㅋ",
        "r": "ㄹ",
        "s": "ㅅ",
        "t": "ㅌ",
        "v": "ㅂ",
        "w": "ㅜ",
        "x": "ㅋㅅ",
        "z": "ㅈ",
        "ə": "ㅓ",
        "ɑ": "ㅏ",
        "ɔ": "ㅗ",
        "ð": "ㄷ",
        "ɛ": "ㅔ",
        "h": "ㅎ",
        "ɪ": "ㅣ",
        "ŋ": "ㅇ응",
        "ʃ": "쉬",
        "θ": "ㄸ",
        "ʊ": "ㅜ",
        "u": "ㅜ",
        "ʒ": "ㅈ",
        "i": "ㅣ",
        "j": "ㅠ"}}

while True:
    sent_eng = input("Eng: ")
    sent_ipa = ipa.convert(sent_eng, keep_punct=False)

    ipa_nums = sorted(ipa_to_han.keys(), reverse=True) + [0]

    sent_han = ""
    while (sent_ipa):
        if (sent_ipa[0:1] == " "):
            sent_han = sent_han + " "
            sent_ipa = sent_ipa[1:]

        for ipa_num in ipa_nums:
            if (ipa_num == 0): exit
            if (sent_ipa[0:ipa_num] in ipa_to_han[ipa_num].keys()):
                sent_han = sent_han + ipa_to_han[ipa_num][sent_ipa[0:ipa_num]]
                sent_ipa = sent_ipa[ipa_num:]
                break
        print(sent_ipa, sent_han)
