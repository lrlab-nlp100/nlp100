import sys
arg = sys.argv
n = int(arg[1])
name = arg[2]
with open(name,'r') as f:
    cnt = sum(1 for line in open(name))
    for line in f:
        if cnt <= n:
            print(line,end="")
        cnt -= 1

# tail -n N filename
