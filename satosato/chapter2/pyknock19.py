# -*- coding: utf-8 -*-
# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
from collections import defaultdict

def sort_by_freq(file_name):
    prefectures = defaultdict(int)
    with open(file_name, "r") as file:
        for line in file:
            prefectures[line.split("\t")[0]] += 1
    for prefecture in sorted(prefectures.items(), key = lambda x:x[1], reverse=True):
        print(prefecture)
if __name__ == "__main__":
    sort_by_freq("hightemp.txt")

# cut -f1 hightemp.txt | sort | uniq -c | sort -r
#    3 群馬県
#    3 山梨県
#    3 山形県
#    3 埼玉県
#    2 静岡県
#    2 愛知県
#    2 岐阜県
#    2 千葉県
#    1 和歌山県
#    1 高知県
#    1 愛媛県
#    1 大阪府
