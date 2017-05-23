#! /usr/bin/env python

from chapter5.p41 import read_chunks
from chapter5.class_chunk import Chunk
from chapter5.p46 import is_verb, get_kaku
from typing import List
from chapter5.p48 import is_noun


def get_path_2(i: int, chunk: Chunk, sentence: List[Chunk]):
    if chunk.dst == -1:
        return [(i, chunk)]
    return [(i, chunk)] + get_path_2(chunk.dst, sentence[chunk.dst], sentence)


def get_min_index_and_val(p: List[int], set):  # 集合要素の最小インデックス探索
    index = -1
    val = None
    for v in set:
        current_index = p.index(v)
        if index == -1 or index > current_index:
            index = current_index
            val = v
    return index, val


def get_path_join(p1: List[int], p2: [int]):  # 列の後半一致のp1p2インデックスと値
    s1 = set(p1)
    s2 = set(p2)
    intersection = s1.intersection(s2)
    p1_min = get_min_index_and_val(p1, intersection)
    p2_min = get_min_index_and_val(p2, intersection)
    return p1_min[0], p2_min[0], p2_min[1]


def replace_noun(chunk: Chunk, replace: str) -> str:
    return "".join([replace if m.pos == "名詞" else m.surface for m in chunk.morphs])


def main():
    sentence_array = read_chunks()
    with open("p48_path.txt", "w", encoding="utf-8") as f:
        for s in sentence_array:
            # print(" ".join([a.to_surface() for a in s]))
            pathes: [[(int, Chunk)]] = []
            for i, cnk in enumerate(s):
                # print("i:{0} cnk:{1}".format(i, cnk.to_surface()))
                if is_noun(cnk):
                    path = get_path_2(i, cnk, s)
                    pathes.append(path)
            joins = []  # i番pathとj番pathはkで交わる
            for i, p1 in enumerate(pathes):
                for j, p2 in list(enumerate(pathes))[i + 1:]:
                    jn = get_path_join([a[0] for a in p1], [a[0] for a in p2])
                    p1_index = jn[0]
                    p2_index = jn[1]
                    v = jn[2]
                    joins.append((i, j, v, p1_index, p2_index))
                    # print(i, j, v, p1_index, p2_index)

            for j in joins:
                if j[4] == 0:
                    p1 = pathes[j[0]]
                    p1_index = j[3]
                    p2 = pathes[j[1]]
                    jjj = [t[1].to_surface() if i != 0 else replace_noun(t[1], "X") for i, t in
                           enumerate(p1[:p1_index])]
                    print(" -> ".join(jjj + [replace_noun(p2[0][1], "Y")]))

                else:
                    p1 = pathes[j[0]]
                    p1_index = j[3]
                    p1_str = " -> ".join(
                        [a[1].to_surface() if i != 0 else replace_noun(a[1], "X") for i, a in enumerate(p1[:p1_index])])
                    p2 = pathes[j[1]]
                    p2_index = j[4]
                    p2_str = " -> ".join(
                        [a[1].to_surface() if i != 0 else replace_noun(a[1], "Y") for i, a in enumerate(p2[:p2_index])])
                    print("{0} | {1} | {2}".format(p1_str, p2_str, s[j[2]].to_surface()))


if __name__ == "__main__":
    main()
