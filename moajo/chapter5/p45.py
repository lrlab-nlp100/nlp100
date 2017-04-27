#! /usr/bin/env python

from chapter5.p41 import read_chunks
from chapter5.class_chunk import Chunk


def is_verb(chunk: Chunk):  # 動詞節判定
    return len([k for k in chunk.morphs if k.pos == "動詞"]) != 0


def get_kaku(chunk: Chunk):
    kaku = [k for k in chunk.morphs if k.pos == "助詞"]
    if len(kaku) == 0:
        return None
    return kaku[0]


def main():
    sentence_array = read_chunks()
    with open("p45_corpus.txt", "w", encoding="utf-8") as f:
        for s in sentence_array:
            for cnk in s:
                if is_verb(cnk):  # 動詞節
                    kaku_list = filter(lambda m: m is not None, [get_kaku(s[i]) for i in cnk.srcs])
                    v_base = [k for k in cnk.morphs if k.pos == "動詞"][0].base
                    f.write("{0}\t{1}\n".format(v_base, " ".join(map(lambda m: m.surface, kaku_list))))


if __name__ == "__main__":
    main()
