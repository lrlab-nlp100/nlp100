# 16. ファイルをN分割する
import math

print('input number')
inp = input()
if not inp.isdigit():
    print('please input digit')
    exit()
N = int(inp)

lst = []
with open('hightemp.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lst.append(line[:-1])
row = math.ceil(len(lst) / N)

for n in range(N):
    with open('hightemp_' + str(n) + '.txt', 'w', encoding='utf-8') as fs:
        for r in range(row):
            if len(lst) == 0:
                break
            p = str(lst.pop(0)) + "\n"
            fs.write(p)
