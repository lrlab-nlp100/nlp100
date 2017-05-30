# coding: utf-8
"""
自然言語処理100本ノック
03. 円周率

"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

"""

str1 = "Now I need a drink, alcoholic of course, \
        after the heavy lectures involving quantum mechanics."
str1 = str1.replace(",", "")  # 文字の置換
str1 = str1.replace(".", "")
words_len = []

for x in str1.split():		# splitメソッドは空白文字で文字列を分解する
    words_len.append(len(x))
    print("{0}\t{1}".format(len(x), x))

return words_len
