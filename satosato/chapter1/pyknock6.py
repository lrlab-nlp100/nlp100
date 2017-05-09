# -*- coding: utf-8 -*-
# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def n_gram(n, str_array):
    n_gram_array = []
    for i in range(len(str_array) - n + 1):
        n_gram_item = ""
        for j in range(n):
            n_gram_item = n_gram_item + str_array[i + j]
        n_gram_array.append(n_gram_item)
    return n_gram_array

if __name__ == "__main__":
    X = n_gram(2, "paraparaparadise")
    Y = n_gram(2, "paragraph")

    X_set = set(X)
    Y_set = set(Y)
    se_set = set(["se"])

    print("'paraparaparadise' bi-gram")
    print(X_set)
    print("'paragraph' bi-gram")
    print(Y_set)
    print("和集合")
    print(X_set.union(Y_set))
    print("和集合")
    print(X_set.union(Y_set))
    print("積集合")
    print(X_set.symmetric_difference(Y_set))
    print("差集合")
    print(X_set.difference(Y_set))
    print("'se' in 'paraparaparadise'")
    print(X_set.issuperset(se_set))
    print("'se' in 'paragraph'")
    print(Y_set.issuperset(se_set))
    print("'se' in 'paraparaparadise' and 'paragraph'")
    print(X_set.symmetric_difference(Y_set).issuperset(se_set))