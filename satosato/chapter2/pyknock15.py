# -*- coding: utf-8 -*-
# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

def tail(filename, n):
    c = 0
    n = int(n)
    with open(file_name, "r") as file:
        lines = file.readlines()

    for line in lines[-n:]:
        print(line)
        c += 1
        if c >= int(n):
            break

if __name__ == "__main__":
    num = input("input number:")
    file_name = input("input file name:")
    tail(file_name, num)
# $ tail -n 3 hightemp.txt
# 山梨県	大月	39.9	1990-07-19
# 山形県	鶴岡	39.9	1978-08-03
# 愛知県	名古屋	39.9	1942-08-02
