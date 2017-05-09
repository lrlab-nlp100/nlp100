# coding:utf-8
import sys
import random

def Typoglycemia(string):
    result = []
    words = string.split()
    for word in words:
        if len(word) <= 4:
            result.append(word)
        else:
            word_naka = list(word[1:-1])#単語の先頭と末尾以外
            random.shuffle(word_naka)#リストの要素並び替え
            result.append(word[0] + ''.join(word_naka) + word[-1])#リスト連結："区切り".join(リスト)
    return ' '.join(result)#区切りはスペース


print("文字列入力>>")
string = sys.stdin.readline()
print("入力文：" + string)

res = Typoglycemia(string)
print("結果：" + str(res))
