# -*- coding; utf-8 -*-
import re
pa = re.compile(r'<(word|lemma|POS)>(.+?)</(word|lemma|POS)>')
with open('nlp.txt.xml','r') as f:
    cnt = 0
    for line in f:
        contents = pa.search(line)
        if contents is not None:
            print(contents.group(2)+'\t',end="")
            cnt += 1
            if(cnt == 3):
                print()
                cnt = 0
