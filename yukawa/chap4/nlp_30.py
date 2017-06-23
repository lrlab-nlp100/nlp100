# -*- coding: utf-8 -*-
import re
def read():
    with open('neko.txt.mecab','r') as f:
        d = {}
        line = []
        text = []
        for l in f:
            li = re.split(r'\s|,',l)
            if li[0] != 'EOS' and li[0] != '':
                d.update({'surface':li[0]})
                d.update({'base':li[7]})
                d.update({'pos':li[1]})
                d.update({'pos1':li[2]})
                line.append(d)
                d = {}
            elif li[0] == 'EOS':
                if len(line) != 0:
                    text.append(line)
                    line = []
                    d = {}
    return text

if __name__ == '__main__':
    l = read()
    print(l)
