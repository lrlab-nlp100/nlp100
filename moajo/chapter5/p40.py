#! /usr/bin/env python

from chapter5.class_morph import Morph


def parse_morph(l):
    spl = l.split("\t")
    surface = spl[0]
    commma = spl[1].split(",")
    base = commma[6]
    pos = commma[0]
    pos1 = commma[1]
    return Morph(surface, base, pos, pos1)


def spl_sentence(morph_array):
    ret = []
    buf = []
    for morph in morph_array:
        buf.append(morph)
        if morph.surface == "。":
            ret.append(buf)
            buf = []
    if len(buf) != 0:
        ret.append(buf)
    return ret


def load_cabocha():
    with open("neko.txt.cabocha", encoding="utf-8") as f:
        s = filter(lambda x: x != "EOS\n", f.readlines())
        return list(map(parse_morph, filter(lambda l: l[0] != "*", s)))


def main():
    morph_array = load_cabocha()
    sentence_array = spl_sentence(morph_array)
    print(sentence_array[2])


if __name__ == "__main__":
    main()
