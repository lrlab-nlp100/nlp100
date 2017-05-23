import sys

argv = sys.argv

with open(argv[1], encoding="utf-8") as f:
    first_chars = {line[0] for line in f}
print(first_chars)

# cut -b 1-3 hightemp.txt | sort | uniq
# sort hightemp.txt | uniq -w 3
