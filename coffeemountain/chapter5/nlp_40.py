class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def _print(self):
        return print(self.surface + "\t" + self.base + "," + self.pos + "," + self.pos1)

    def make_morph_list(input_file):
        sentences = []
        sentence = []
        with open(input_file, 'r', encoding='utf8') as input_file:
            for line in input_file:
                splits = line.split()[0]
                if splits != '*' and splits != 'EOS':
                    facter1, facter2 = line.split('\t')
                    facter2 = facter2.split(',')

                    sentence.append(Morph(facter1, facter2[6], facter2[0], facter2[1]))
                    if facter2[1] == '句点':
                        sentences.append(sentence)
                        sentence = []
        return sentences

if __name__ == "__main__":
      morph_sentences = Morph.make_morph_list('neko.txt.cabocha')

      for morphs in morph_sentences[2]:
            morphs._print()