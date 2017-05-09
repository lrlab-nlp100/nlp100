
def sent_gene(x, y, z):
    return '{h}時の{t}は{z}度'.format(h=x, t=y, z=z)#str.format書式化操作

x = 12
y = '気温'
z = 22.4

print (sent_gene(x, y, z))
