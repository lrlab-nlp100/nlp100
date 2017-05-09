# coding:utf-8
import sys

def cipher(string):
    res =""
    for cha in string:
        if cha.islower():#小文字ならTrue,数字/大文字はFalse
            res += chr(219 - ord(cha))#ord()文字からアスキー,chr()アスキーから文字
        else:
            res += cha
    return res

print("文字列を入力して下さい")
string = sys.stdin.readline()
print("入力文：" + string)

res = cipher(string)
print("暗号：" + res)

res2 = cipher(res)
print("復号：" + res2)
