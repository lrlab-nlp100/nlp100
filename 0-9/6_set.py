# 06. 集合


def chara_ngram(text, n):
    results = []
    text = text.replace(' ', '')
    if len(text) >= n:
        for i in range(len(text)-n+1):
            results.append(text[i:i+n])
    return results

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(chara_ngram(str1, 2))
Y = set(chara_ngram(str2, 2))

# set union
print("union:" + str(X.union(Y)))

# set intersection
print("intersection:" + str(X.intersection(Y)))

# set difference
print("difference:" + str(X.difference(Y)))

print("se in X:" + str('se' in X))
print('se in Y:' + str('se' in Y))
