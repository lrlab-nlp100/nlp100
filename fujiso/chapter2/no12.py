# coding: utf-8
"""
自然言語処理100本ノック

12. 1列目をcol1.txtに，2列目をcol2.txtに保存

各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．

確認にはcutコマンドを用いよ．

確認コマンド:
$ cut -f1 hightemp.txt > col1.txt
$ cut -f2 hightemp.txt > col2.txt
"""


def extract_col(col_num, filename="hightemp.txt"):
    with open(filename, "r") as f, open("./out/col{}.txt".format(col_num), "w") as o:
        for text in f:
            t = text.split('\t')
            o.write(t[col_num - 1] + '\n')
    print("col{0}.txt is created.".format(col_num))


if __name__ == '__main__':
    try:
        extract_col(1)
        extract_col(2)
    except Exception as e:
        print(e.message)
