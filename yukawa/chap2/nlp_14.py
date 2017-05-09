import sys
arg = sys.argv
n = arg[1]
n = int(n)
name = arg[2]
f = open(name,'r')
cnt = 0
for line in f:
    if cnt <= n:
        print(line[:len(line)-1])
    else:
        break
    cnt += 1
f.close()
