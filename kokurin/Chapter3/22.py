import re
import nltk

with open('uk.txt','r') as f:
    for line in f:
        target=re.findall("^\[\[Category:(.+)\]\]",line)
        if target:
            print(target)

        # "formhash\" value=\"(.*)\""
        #print(re.findall(r'\[Category:.*\]',line))