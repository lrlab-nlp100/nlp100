# coding: utf-8
"""
自然言語処理100本ノック

07. テンプレートによる文生成

引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""


def tmp(x, y, z):
    print("{time}時の{feature}は{num}".format(
        time=x, feature=y, num=z))


if __name__ == "__main__":
    tmp(12, "気温", 22.4)
