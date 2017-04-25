# coding: utf-8
"""
自然言語処理100本ノック
04. 元素記号

"Hi He Lied Because Boron Could Not Oxidize Fluorine.
New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
    New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str1 = str1.split()
num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dic = {}

for x in range(len(str1)):
    if x + 1 in num_list:
        dic[str1[x][0]] = x
    else:
        dic[str1[x][:2]] = x

# 確認用
for i, j in sorted(dic.items(), key=lambda x: x[1]):
    print(i + '\t' + str(j))
