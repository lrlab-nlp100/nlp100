# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

from collections import Counter

with open('hightemp.txt', 'r', encoding='utf-8') as f:

    lst = []
    for line in f:
        lst.append(line.split()[0])

    counter = Counter(lst)
    for word, cnt in counter.most_common():
        print(word, cnt)