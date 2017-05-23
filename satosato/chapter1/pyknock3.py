# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
string = string.replace(",", "").replace(".", "")
string = string.split(" ")
word_cnt = []
for s in string:
    word_cnt.append(len(s))

print(word_cnt)