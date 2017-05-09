f = open('hightemp.txt','r')
ret = open('new-hightemp.txt','w')
for line in f:
    s = line.replace('\t',' ')
    ret.write(s)
f.close()
ret.close()
