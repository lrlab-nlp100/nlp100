import sys
import rfile
arg = sys.argv
n = arg[1]
n = int(n)
name = arg[2]
f = open(name,'r')
cnt  = rfile.rf(name)
for line in f:
    if cnt <= n:
        print(line[:len(line)-1])
    cnt -= 1
f.close()
