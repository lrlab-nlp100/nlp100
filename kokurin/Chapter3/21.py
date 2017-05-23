import re

with open('uk.txt','r') as f:
    for line in f:
        if re.search('Category',line):
            print(line)