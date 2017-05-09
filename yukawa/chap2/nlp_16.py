import sys
import rfile
arg = sys.argv
n = arg[1]
n = int(n)
num = n
name = arg[2]
cnt = rfile.rf(name)
n = round(cnt/n)
nfile = 0
nline = 0
f = open(name,'r')
for line in f:
    if nline == 0:
        f1 = open(name[:len(name)-4]+str(nfile)+'.txt','w')
        f1.write(line)
        nfile += 1
        nline += 1
    elif num == nfile:
        f1.write(line)
        nline += 1
    elif nline < n-1:
        f1.write(line)
        nline += 1
    elif nline == n-1:
        f1.write(line)
        f1.close()
        nline = 0
        
f.close()
f1.close()
        
