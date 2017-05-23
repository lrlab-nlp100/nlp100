# coding: utf-8
"""
自然言語処理100本ノック

13. col1.txtとcol2.txtをマージ

12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．

確認にはpasteコマンドを用いよ．

確認コマンド:
paste col1.txt col2.txt > merge.txt

エラー処理面倒くさくなった
"""


def merge_text(file1="./out/col1.txt", file2="./out/col2.txt"):

    with open(file1) as f1, open(file2) as f2:
        text1, text2 = f1.readlines(), f2.readlines()

    with open("./out/out13.txt", "w") as out:
        for (x, y) in zip(text1, text2):
            x = x.replace('\n', '\t')
            out.write(x + y)
    print("out13.txt is created.")


if __name__ == '__main__':
    merge_text()
