# -*- coding:utf-8 -*-
import re
class Morph():
    def __init__(self,s,b,p,p1):
        self.surface = s
        self.base = b
        self.pos = p
        self.pos1 = p1

    def print_value(self):
        print(self.surface,self.base,self.pos,self.pos1)

if __name__ == '__main__':
    with open('neko.txt.cabocha','r') as f:
        l = []
        lm = []
        for line in f:
            word = re.split(r'\,|\t',line)
            if len(word) == 10:
                lm.append(Morph(word[0],word[7],word[1],word[2]))
            elif word[0] == 'EOS\n':
                l.append(lm)
                lm = []
        for w in l[2]:
            w.print_value()
