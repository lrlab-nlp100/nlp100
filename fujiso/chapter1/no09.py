# coding: utf-8
"""
自然言語処理100本ノック

09. Typoglycemia

スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．

ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
（例えば"I couldn't believe that I could actually understand what I was reading :
 the phenomenal power of the human mind ."）
を与え，その実行結果を確認せよ．
"""
import random


def mid_rand(imput):
    output = []
    for x in imput.split():  # 単語ごとに処理
        if len(x) <= 4:
            output.append(x)  # そのまま追加
        else:
            mid = x[1:-1]
            # randam.sample()で、１文字のリストが帰ってくるので、join()で結合して代入
            mid = "".join(random.sample(mid, len(mid)))
            output.append(x[0] + mid + x[-1])
    return " ".join(output)


if __name__ == '__main__':
    mes = ("I couldn't believe that I could actually understand \
        what I was reading :the phenomenal power of the human mind.")
    print(mid_rand(mes))
