import sys
arg = sys.argv
n = int(arg[1])
name = arg[2]
with open(name,'r') as f:
    cnt = 0
    for line in f:
        if cnt <= n:
            print(line,end="")
        else:
            break
        cnt += 1

# head -n N filename
