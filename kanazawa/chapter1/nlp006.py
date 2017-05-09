
from nlp005 import n_gram

x = set(n_gram("paraparaparadise",2))#set():重複除去
y = set(n_gram("paragraph",2))

print("X：" + str(x))
print("Y：" + str(y))

print("和集合：" + str(x.union(y)))
print("積集合：" + str(x.intersection(y)))#xとyの共通部分
print("差集合(X-Y)；" + str(x.difference(y)))
print("差集合(Y-X)；" + str(y.difference(x)))

key = set(['se'])#setに文字列渡すにはリスト
print("Xにse含まれる：" + str(key.issubset(x)))#isublistは部分集合判別
print("Yにse含まれる：" + str(key.issubset(y)))


"""
#簡単な方法
print ("se" in x)
print ("se" in y)
"""
