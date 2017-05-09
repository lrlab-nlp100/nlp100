f = open('hightemp.txt','r')
l = []
p = []
for line in f:
    l = line.split()
    p.append(l[0]) 
p = set(p)
print(p)

