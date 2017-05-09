from collections import Counter 
f = open('hightemp.txt','r')
l = []
p = []
for line in f:
    line = line.split()[0]
    l.append(line)

c = Counter(l)
for k,v in sorted(c.items(),key=lambda x:x[1],reverse=True):
    print(v,k)
f.close()
