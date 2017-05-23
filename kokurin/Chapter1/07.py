def gen(x,y,z):
    sent='{x}時の{y}は{z}'.format(x=x,y=y,z=z) #字符串中替换变量值
    print(sent)

x=12
y="気温"
z=22.4

gen(x,y,z)