# 14. 先頭からN行を出力

f = open('hightemp.txt', 'r', encoding='utf-8')

print('input number')
inp = input()

if not inp.isdigit():
    print('please input digit')
    exit()

num = int(inp)

while num > 0:
    print(f.readline()[:-1])
    num -= 1

f.close()
