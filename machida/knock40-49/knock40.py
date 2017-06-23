# -*- coding:utf-8 -*-

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'sur:{},base:{},pos:{},pos1:{}'.format(self.surface, self.base, self.pos, self.pos1)

if __name__ == '__main__':
    sentence = []
    sentences = []
    with open('neko.txt.cabocha', 'r') as txt:
        for t in txt:
            lit = t.split('\t')
            if lit[0][0] == '*':
                continue
            if lit[0] == 'EOS\n':
                if len(sentence) > 0:
                    sentences.append(sentence)
                    sentence = []
            else:
                feature = lit[1].split(',')
                morph = Morph(surface=lit[0], base=feature[6], pos=feature[0], pos1=feature[1])
                sentence.append(morph)

    for t in sentences[2]:#3文目を表示
        print(t)
