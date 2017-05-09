import sys

argv = sys.argv

if len(argv) != 3:
    print("引数が足りません。few arguments")
    sys.exit()

with open(argv[1], encoding="utf-8") as f:
    for i in range(int(argv[2])):
        print(f.readline(), end="")
