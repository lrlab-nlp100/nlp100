from nlp_41 import *


def extract_chunk(_chunk):
    return print(_chunk.morphs.surface for morphs in _chunk.morphs)


if __name__ == '__main__':
    chunk_sentences = make_chunk_list('neko.txt.cabocha')
    for chunk in chunk_sentences[1]:
        # print(type(chunk.morphs))
        print(type(chunk.morph.surface for morph in chunk.morphs))
        # print(type(extract_chunk(chunk)))
