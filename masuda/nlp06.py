from nlp05 import n_gram

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(n_gram(2, str1))
Y = set(n_gram(2, str2))
print("X = ", X, "\nY = ", Y)

print("X∪Y = ", X | Y, "\nX∩Y = ", X & Y, "\nX-Y = ", X - Y)
