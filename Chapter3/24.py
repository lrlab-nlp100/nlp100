import re
import nltk

with open('uk.txt','r') as f:
    for line in f:
        target=re.findall("File:(.+?)\|",line)
        if target:
            print(target[0])

        # "formhash\" value=\"(.*)\""
        #print(re.findall(r'\[Category:.*\]',line))