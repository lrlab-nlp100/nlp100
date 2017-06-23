from nlp_41 import *


def extract_chunk(_chunk):
    return print(_chunk.morphs.surface for morphs in _chunk.morphs)


if __name__ == '__main__':
    chunk_sentences = make_chunk_list('neko.txt.cabocha')
    chunks = chunk_sentences[1]

    for chunk in chunks:
        print(len(chunk.morphs))
        print(chunk.morphs[1].surface)