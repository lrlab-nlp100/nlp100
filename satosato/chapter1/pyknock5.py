# -*- coding: utf-8 -*-
# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def n_gram(n, str_array):
    n_gram_array = []
    for i in range(len(str_array) - n + 1):
        n_gram_item = []
        for j in range(n):
            n_gram_item.append(str_array[i + j])
        n_gram_array.append(n_gram_item)
    return n_gram_array

if __name__ == "__main__":
    string = "I am an NLPer"
    str_word = string.split(" ")
    str_chr = string.replace(" ", "")

    print(n_gram(2, str_word))
    print(n_gram(2, str_chr))
    print(n_gram(3, str_word))
    print(n_gram(3, str_chr))