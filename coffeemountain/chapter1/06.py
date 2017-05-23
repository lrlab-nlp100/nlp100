str1 = "paraparaparadise"
str2 = "paragraph"

def make_ngram(n, input):
    n_gram = []
    for i in range(len(input)-n+1):
        n_gram.append(input[i:i+n])
    
    return n_gram

X = set(make_ngram(2, str1))
Y = set(make_ngram(2, str2))


#和
print(X.union(Y))

#差
print(X - Y)

#積
print(X & Y)

#seが入っているか
if "se" in X:
    print("TrueX")
else:
    print("FalseY")
if "se" in Y:
    print("TrueY")
else:
    print("FalseY")