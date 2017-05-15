import sys
from operator import itemgetter

with open(sys.argv[1], encoding="utf-8") as f:
    dic = {}
    for line in f:
        freq = dic.get(line[0], 0) + 1
        dic.update({line[0]:freq})
    for item in sorted(dic.items(), key=itemgetter(1), reverse=True):
        print(str(item[1]) + " " +item[0])


# cut -b 1-3 hightemp.txt | sort | uniq -c | sort -r
