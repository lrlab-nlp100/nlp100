import sys

argv = sys.argv

if len(argv) != 3:
    print("引数が足りません。few arguments")
    sys.exit()

with open(argv[1], encoding="utf-8") as f:
    lines = 0
    for line in f:
        lines += 1

    f.seek(0)
    count = 0
    n = int(argv[2])
    for line in f:
        count += 1
        if count > lines - n:
            print(line, end="")

# head -3 hightemp.txt
