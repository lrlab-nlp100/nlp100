from nlp_40 import Morph


class Chunk:
    def __init__(self, morphs: list, dst: str, srcs: str) -> None:
        self.morphs = morphs
        self.dst = int(dst.strip("D"))
        self.srcs = int(srcs)

    def _print(self):
        return print("(文節" + str(self.srcs) + "): " + "".join(morph.surface for morph in self.morphs) + "    (係り先): " + str(self.dst))


def make_chunk_list(input_file):
    sentence = []
    sentences = []
    _chunk = None
    with open(input_file, "r", encoding='utf8') as input_file:
        for line in input_file:
            if line.split()[0] == '*':
                if _chunk is not None:
                    sentence.append(_chunk)
                    _chunk = None
                factor = line.split()
                _chunk = Chunk([], factor[2], factor[1])

            elif line.split()[0] == 'EOS':
                if _chunk is not None:
                    sentence.append(_chunk)
                    sentences.append(sentence)
                    _chunk = None
                    sentence = []
            else:
                factor1, factor2 = line.split('\t')
                factor2 = factor2.split(',')
                _chunk.morphs.append(Morph(factor1, factor2[6], factor2[0], factor2[1]))

        return sentences

if __name__ == '__main__':
    chunk_sentences = make_chunk_list(input_file='neko.txt.cabocha')
    for chunk in chunk_sentences[7]:
        chunk._print()
