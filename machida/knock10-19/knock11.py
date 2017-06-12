# -*- coding: utf-8 -*-

f = open('hightemp.txt')
txt = f.read().replace('\t', ' ')
f.close()

print(txt)

# command
# cat hightemp.txt | tr '\t' ' '
# sedだとできん
# sed 's/\t/ /g' hightemp.txt
