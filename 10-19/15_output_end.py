# 15. 末尾のN行を出力

f = open('hightemp.txt', 'r', encoding='utf-8')

print('input number')
inp = input()

if not inp.isdigit():
    print('please input digit')
    exit()

num = int(inp)

lst = []
for line in f:
    lst.append(line[:-1])

while num > 0:
    print(lst[-num])
    num -= 1

f.close()
