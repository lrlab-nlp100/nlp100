#! /usr/bin/env python

from chapter5.class_morph import Morph
from chapter5.class_chunk import Chunk
from chapter5.p40 import load_cabocha, spl_sentence, parse_morph
import re
from typing import List, Sequence
from chapter5.p41 import read_chunks


def main():
    sentence_array = read_chunks()
    for s in sentence_array:
        for cnk in s:
            if cnk.dst != -1:
                print("{0}\t{1}".format(cnk.to_surface(), s[cnk.dst].to_surface()))


if __name__ == "__main__":
    main()
