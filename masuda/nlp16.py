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
    divline = lines // n
    file_index = 0
    dist = open("div"+file_index+".txt", "w", encoding="utf-8")
    for line in f:
        count += 1
        dist.write(line)
        if count == divline:
            dist.close()
            file_index += 1
            dist = open("div"+file_index+".txt", "w", encoding="utf-8")

