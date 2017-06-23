# -*- coding:utf-8 -*-
import knock40

class Chunk():
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = int(dst)
        self.srcs = int(srcs.rstrip('D'))

    def pos_is_noun(self):
        return any([m.pos == '名詞' for m in self.morphs])
    def pos_is_verb(self):
        return any([m.pos == '動詞' for m in self.morphs])
    def pos_is_post(self):
        return any([m.pos == '助詞' for m in self.morphs])
    def pos_is_noun_s(self):
        for i, m in enumerate(self.morphs[:-1]):
            if m.pos1 == 'サ変接続' and self.morphs[i+1].surface == 'を':
                return True
        return False
    def first_verb(self):
        return [m.base for m in self.morphs if m.pos == '動詞'][0]
    def last_post(self):
        return [m.base for m in self.morphs if m.pos == '助詞'][-1]
    def s_phrase(self):
        return [m.base for m in self.morphs if m.pos1 == 'サ変接続'][0]
    def rep_noun(self, s):
        return s + ''.join([m.surface for m in self.morphs[1:]])

    def rm_symbol_phrase(self):
        return ''.join([m.surface for m in self.morphs if m.pos != '記号'])
    def __str__(self):
        return 'dst:{},srcs:{},morphs({})'.format(self.dst, self.srcs, '/'.join([str(m) for m in self.morphs]))

sentence, sentences, chunk = [], [], None
with open('neko.txt.cabocha', 'r') as txt:
# with open('test', 'r') as txt:
    for t in txt:
        lit = t.split('\t')
        if lit[0][0] == '*':
            if chunk is not None:
                sentence.append(chunk)
            l = str(lit[0]).split()
            chunk = Chunk(morphs=[], dst=l[1], srcs=l[2])
        elif lit[0] == 'EOS\n':
            if chunk is not None:
                sentence.append(chunk)
            if len(sentence) > 0:
                sentences.append(sentence)
                chunk = None
                sentence = []
        else:
            feature = lit[1].split(',')
            if feature[6] == '*\n':#単語の原型が登録されていない場合、表層系を原型とする。
                feature[6] = lit[0]
            morph = knock40.Morph(surface=lit[0], base=feature[6], pos=feature[0], pos1=feature[1])
            chunk.morphs.append(morph)

if __name__ == '__main__':
    for t in sentences[1]: #8文目を表示
        print(t)
