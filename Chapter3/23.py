import re

with open('uk.txt','r') as f:
    for line in f:
        target=re.search("^(\=+)(.*?)\=+",line)
        if target:
            print(target.group(2),len(target.group(1))-1)

        # "formhash\" value=\"(.*)\""
        #print(re.findall(r'\[Category:.*\]',line))