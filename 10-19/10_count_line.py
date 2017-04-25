# 10. 行数のカウント

with open('hightemp.txt', 'r', encoding='utf-8') as f:
    i = 0
    for line in f:
        i += 1
print(i)
