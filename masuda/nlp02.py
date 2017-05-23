pato = 'パトカー'
taxi = 'タクシー'
ret = ''
for x, y in zip(pato, taxi):
    ret += x + y

print(ret)


# print(''.join([x + y for x, y in zip(pato, taxi)]))
