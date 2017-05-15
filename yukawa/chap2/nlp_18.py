# -*- encode: utf-8 -*- 
with open('hightemp.txt','r') as f:
    l=f.readlines()
sorted(l,key=lambda l:l[2])
print(''.join(l))

# sort -r -k3 hightemp.txt
