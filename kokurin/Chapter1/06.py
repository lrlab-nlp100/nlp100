import nltk

x=list('paraparaparadise')
y=list('paragraph')

X=set(nltk.bigrams(x))
Y=set(nltk.bigrams(y))

print(X | Y)
print(X & Y)
print(X - Y)
test=list(nltk.bigrams('se'))
print(test[0] in X)#验证某列表内是否包含特定元素时需要检查元素本身，并非整个列表，即便此只有一个元素
print(test[0] in Y)