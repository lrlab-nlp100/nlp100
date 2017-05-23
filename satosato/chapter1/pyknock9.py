# -*- coding: utf-8 -*-
# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，
# その実行結果を確認せよ．

import random

def Typoglycemia(m_string):
    m_words = m_string.split(" ")
    c_string = ""
    for word in m_words:
        if len(word) > 4:
            #random.sample(str_string, len(str_string)) -> return list#a chr is a element of list
            #"str".join(list) -> return str#join list by str
            c = word[0] + "".join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1]
            c_string = c_string + c + " "
        else:
            c_string = c_string + word + " "
    return c_string


if __name__ == "__main__":
    print("text")
    print("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
    print("Typoglycemia")
    print(Typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))