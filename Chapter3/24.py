import re

with open('uk.txt','r') as f:
    for line in f:
        target=re.findall("(ファイル|File):(.+?)\|",line)
        if target:
            print(target[0][1])

        # "formhash\" value=\"(.*)\""
        #print(re.findall(r'\[Category:.*\]',line))