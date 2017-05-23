#! /usr/bin/env python

from chapter5.p41 import read_chunks


def main():
    sentence_array = read_chunks()
    for s in sentence_array:
        for cnk in s:
            if cnk.dst != -1:
                if len([s for s in cnk.morphs if s.pos=="名詞"])!=0:
                    if len([k for k in s[cnk.dst].morphs if k.pos=="動詞"])!=0:
                        print("{0}\t{1}".format(cnk.to_surface(), s[cnk.dst].to_surface()))


if __name__ == "__main__":
    main()
