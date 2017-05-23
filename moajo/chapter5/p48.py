#! /usr/bin/env python

from chapter5.p41 import read_chunks
from chapter5.class_chunk import Chunk
from chapter5.p46 import is_verb, get_kaku
from typing import List


def is_noun(chunk: Chunk):
    return len([k for k in chunk.morphs if k.pos == "名詞"]) != 0


def get_path(chunk: Chunk, sentence: List[Chunk]) -> List[Chunk]:
    if chunk.dst == -1:
        return [chunk]
    return [chunk] + get_path(sentence[chunk.dst], sentence)


def main():
    sentence_array = read_chunks()
    with open("p48_path.txt", "w", encoding="utf-8") as f:
        for s in sentence_array:
            for cnk in s:
                if is_noun(cnk):
                    path = get_path(cnk, s)
                    print(" -> ".join([a.to_surface() for a in path]))
                    f.write(" -> ".join([a.to_surface() for a in path])+"\n")


if __name__ == "__main__":
    main()
