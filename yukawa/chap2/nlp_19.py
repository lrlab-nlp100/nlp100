from collections import Counter 
with open('hightemp.txt','r') as f:
    l = []
    for line in f:
        line = line.split()[0]
        l.append(line)
c = Counter(l)
for k,v in sorted(c.items(),key=lambda x:x[1],reverse=True):
    print(k,v)

# cut -f1 hightemp.txt | sort | uniq -c | sort -r
