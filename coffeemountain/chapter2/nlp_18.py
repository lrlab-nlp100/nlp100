import sys

with open("hightemp.txt", "r") as f:
    lines = f.readlines()

for line in sorted(lines, key=lambda x: x.split()[2], reverse=True):
    print(line)