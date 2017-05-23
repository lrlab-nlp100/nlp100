# -*- coding: utf-8 -*-
# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

def get_uniq_word(filename):
    with open(filename, "r") as file:
        word = []
        for line in file:
            line = line.split("\t")
            word.append(line[0])
        word = list(set(word))
    return word

if __name__ == "__main__":
    print(get_uniq_word("hightemp.txt"))

# $ sort col1.txt | uniq
# 千葉県 /
# 埼玉県 /
# 大阪府 /
# 山形県 /
# 山梨県 /
# 岐阜県 /
# 愛媛県 /
# 愛知県 /
# 群馬県 /
# 静岡県 /
# 高知県 /
# 和歌山県 /