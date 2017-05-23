#! /usr/bin/env python

from chapter5.p41 import read_chunks
from chapter5.class_chunk import Chunk
from chapter5.p46 import is_verb, get_kaku


def get_verb(chunk: Chunk):  # 動詞節判定
    v = [k for k in chunk.morphs if k.pos == "動詞"]
    if len(v) != 0:
        return v[0]
    return None


def is_sahen_plus_wo(chunk: Chunk):
    sahen = len([k for k in chunk.morphs if k.pos1 == "サ変接続"]) != 0
    wo = len([k for k in chunk.morphs if k.pos == "助詞" and k.surface == "を"]) != 0
    return sahen and wo


def main():
    sentence_array = read_chunks()
    with open("p47_corpus.txt", "w", encoding="utf-8") as f:
        for s in sentence_array:
            for cnk in s:
                if is_sahen_plus_wo(cnk):
                    if cnk.dst != -1 and is_verb(s[cnk.dst]):
                        v_chunk = s[cnk.dst]
                        v = get_verb(v_chunk)
                        pred = cnk.to_surface() + v.base
                        kaku_list = list(filter(lambda t: t[1] is not None and t[1].surface != "を",
                                                [(s[i], get_kaku(s[i])) for i in v_chunk.srcs]))
                        joind_kaku = " ".join(map(lambda t: t[1].surface, kaku_list))
                        joined_chunk = " ".join(map(lambda t: t[0].to_surface(), kaku_list))
                        f.write("{0}\t{1}\t{2}\n".format(pred, joind_kaku, joined_chunk))


if __name__ == "__main__":
    main()
