import sys
from operator import itemgetter

argv = sys.argv

with open(argv[1], encoding="utf-8") as f:
    line_num = 0
    lis = []
    for line in f:
        line_num += 1
        if len(line) >= 3:
            lis.append((line[2], line_num))
    sorted_list = sorted(lis, key=itemgetter(0), reverse=True)
    for sl in sorted_list:
        f.seek(0)
        line_num = 0
        for line in f:
            line_num += 1
            if line_num == sl[1]:
                print(line, end="")
                break

# sort -k 7 hightemp.txt
