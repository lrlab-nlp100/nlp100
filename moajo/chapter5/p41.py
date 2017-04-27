#! /usr/bin/env python

from chapter5.class_morph import Morph
from chapter5.class_chunk import Chunk
from chapter5.p40 import load_cabocha, spl_sentence, parse_morph
import re
from typing import List, Sequence


def read_cabocha():
    with open("neko.txt.cabocha", encoding="utf-8") as f:
        s = filter(lambda x: x != "EOS\n", f.readlines())
        return list(s)


def read_chunks()->List[List[Chunk]]:
    lines = read_cabocha()
    ret = []  # sentence array
    buf_sentence: Sequence[Chunk] = []  # current sentence as chunk array
    buf_morph = []  # current chunk as morph array
    buf_chunk_dst = -1  # current chunk dst

    for l in lines:
        if l[0] == "*":  # start new chunk
            if len(buf_morph) != 0:
                # completion chunk by buffered morphs
                buf_sentence.append(Chunk(buf_morph, buf_chunk_dst, []))
                buf_morph = []

            # parse chunk metadata
            match = re.match(r"\* (\d+) (-?\d+)D", l)
            chunk_index = int(match.group(1))
            buf_chunk_dst = int(match.group(2))

            if chunk_index == 0 and len(buf_sentence) != 0:
                # sentence completion
                l = list(map(lambda x: [], range(len(buf_sentence))))
                for i, chunk in enumerate(buf_sentence):
                    if chunk.dst != -1:
                        l[chunk.dst].append(i)
                for i, srcs in enumerate(l):
                    buf_sentence[i].srcs = srcs

                ret.append(buf_sentence)
                buf_sentence = []
        else:  # chunk continue
            morph = parse_morph(l)
            buf_morph.append(morph)
    return ret


def main():
    sentence_array = read_chunks()
    for c in sentence_array[7]:
        print(c)


if __name__ == "__main__":
    main()
