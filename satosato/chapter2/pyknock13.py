# -*- coding: utf-8 -*-
# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

def marge_col(file1_name, file2_name, write_file_name):
    with open(write_file_name, "w") as write_file:
        for col1, col2 in zip(open(file1_name, "r"), open(file2_name, "r")):
            write_file.write(col1.replace("\n", "") + "\t" + col2)

if __name__ == "__main__":
    marge_col("col1.txt", "col2.txt", "pyknock13_out.txt")

# paste -d "\t" col1.txt col2.txt
# 高知県	江川崎
# 埼玉県	熊谷
# 岐阜県	多治見
# 山形県	山形
# 山梨県	甲府
# 和歌山県	かつらぎ
# 静岡県	天竜
# 山梨県	勝沼
# 埼玉県	越谷
# 群馬県	館林
# 群馬県	上里見
# 愛知県	愛西
# 千葉県	牛久
# 静岡県	佐久間
# 愛媛県	宇和島
# 山形県	酒田
# 岐阜県	美濃
# 群馬県	前橋
# 千葉県	茂原
# 埼玉県	鳩山
# 大阪府	豊中
# 山梨県	大月
# 山形県	鶴岡
# 愛知県	名古屋
