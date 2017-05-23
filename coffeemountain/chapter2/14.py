import sys

with open("hightemp.txt", "r") as f:
    lines = f.readlines()

for line in lines[:int(sys.argv[1])]:
    print(line)

