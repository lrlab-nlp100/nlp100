# 17. １列目の文字列の異なり

with open('hightemp.txt', 'r', encoding='utf-8') as f:
    pref = set()

    for line in f:
        s = line.split()
        pref.add(s[0])

    for p in pref:
        print(p)
