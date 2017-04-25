# 18. 各行を3コラム目の数値の降順にソート
from operator import itemgetter

with open('hightemp.txt', 'r', encoding='utf-8') as f:

    lst = []
    for line in f:
        lst.append(line.split())
    sorted_lst = sorted(lst, key=itemgetter(2), reverse=False)

    for x in sorted_lst:
        print(x)
