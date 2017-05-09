f = open('hightemp.txt','r')
l = []
for line in f:
   l.append(line)

sorted(l,key=lambda l:l[2])

for word in l:
    print(word)

