import re

with open('uk.txt','r') as f:
    for line in f:
        if re.search('Category',line):
            part_line=line.split(':')[1]
            print(part_line.split(']')[0])