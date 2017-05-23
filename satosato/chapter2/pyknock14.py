# -*- coding: utf-8 -*-
# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

def head(file_name, n):
    c = 0
    for line in open(file_name, "r"):
        print(line)
        c += 1
        if c >= int(n):
            break

if __name__ == "__main__":
    num = input("input number:")
    file_name = input("input file name:")
    head(file_name, num)

# $ head -n 3 hightemp.txt
# 高知県	江川崎	41	2013-08-12
# 埼玉県	熊谷	40.9	2007-08-16
# 岐阜県	多治見	40.9	2007-08-16