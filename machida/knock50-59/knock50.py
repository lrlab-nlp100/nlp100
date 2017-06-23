# -*- coding:utf-8 -*-
import re

pattern = re.compile(r'((\.|;|:|\?|!) [A-Z])')
sentence = []
# with open('nlp.txt', 'r') as txt:
with open('test', 'r') as txt:
    for t in txt:
        line = t
        if line == '\n':
            continue
        while True:
            punc = re.search(pattern, line)
            if punc:
                sentence.append(line[:punc.start()+1])
                line = line[punc.end()-1:]
            else:
                sentence.append(line.replace('\n', ''))
                break
def main():
    for s in sentence:
        print(s)

if __name__ == '__main__':
    main()
