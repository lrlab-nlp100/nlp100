# -*- coding: utf-8 -*-
import nlp_40
import re
from collections import defaultdict
class Chunk:
    def __init__(self,d,s):
        self.dst = d
        self.srcs = s
        self.morphs = []

    def set(self,m):
        self.morphs = m

    def mtoc(self,d):
        text = []
        for m in d.morphs:
            if m.pos != '記号':
                text.append(m.surface)
        return ''.join(text)
    
    def mtoc_t(self,d,x):
        text = []
        for m in d.morphs:
            if m.pos != '記号':
                if m.pos == '名詞':
                    text.append(x)
                else:
                    text.append(m.surface)
        return ''.join(text)

    def out(self):
        for m in self.morphs:
            print(m.surface,end="")
        print('=> '+str(self.dst),self.srcs)

    def verb(self):
        for m in self.morphs:
            if m.pos == '動詞':
                return m.base

    def is_jo(self,s=u'.*'):
        for m in self.morphs[::-1]:
            if m.pos == '助詞' and re.fullmatch(s,m.surface) is not None: 
                return m.surface

    def jo(self):
        text = []
        for m in self.morphs:
            text.append(m.surface)
        return ''.join(text)

    def is_noun(self,opt=''):
        for m in self.morphs:
            if m.pos == '名詞':
                if opt != '' and m.pos1 == opt:
                    return True
                elif opt == '':
                    return True
        return False

    def is_ntov(self,d,opt=''):
        n,v = 0,0
        if self.is_noun(opt):
            n += 1
        if d.verb() is not None:
            v += 1
        if n != 0 and v != 0:
            return True
        return False

def make_chunk():
    with open('neko.txt.cabocha','r') as f:
        l = []
        lm = []
        ch = []
        d = defaultdict(list)
        for line in f:
            word = re.split(r'\,|\t|\s',line)
            if len(word) == 11 or len(word) == 9 and word[0] != '':
                lm.append(nlp_40.Morph(word[0],word[7],word[1],word[2]))
            elif len(word) == 6:
                d[int(word[2][:-1])].append(int(word[1]))
                ch.append(Chunk(int(word[2][:-1]),d[int(word[1])]))
                if len(lm) != 0:
                    ch[-2].set(lm)
                    lm = []
            elif word[0] == 'EOS':
                if len(lm) != 0:
                    ch[-1].set(lm)
                    lm = []
                    l.append(ch)
                    ch = []
                    d = defaultdict(list)
    return l

if __name__ == '__main__':
    l = make_chunk()
    for c in l[7]:
        c.out()
