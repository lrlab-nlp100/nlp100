# -*- coding: utf-8 -*-

import nlp_05

X = nlp_05.make_gram(2,"paraparaparadise")
Y = nlp_05.make_gram(2,"paragraph")
X = set(X)
Y = set(Y)
print(X)
print(Y)
AND = []
for word in Y:
    if word in X:
        AND.append(word)
AND = set(AND)
print(AND)
OR = []
for word in Y:
    OR.append(word)
for word in X:
    OR.append(word)
OR = set(OR)
print(OR)
MINUS = []
for word in X:
    if not word in Y:
        MINUS.append(word)
MINUS = set(MINUS)
print(MINUS)

#AND = X&Y
#OR = X|Y
#MINUS = X - Y
#print(AND)
#print(OR)
#print(MINUS)
