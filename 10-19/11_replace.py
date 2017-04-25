# 11. タブをスペースに置換

lst = []
with open('hightemp.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lst.append(line.expandtabs(1)[:-1])
print(lst)

