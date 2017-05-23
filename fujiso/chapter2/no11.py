# coding: utf-8
"""
自然言語処理100本ノック

11. タブをスペースに置換

タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

確認コマンド:
$ sed -e s/$'\t'/' '/g hightemp.txt
$ cat hightemp.txt | tr '\t' ' '
$ expand -t 1 hightemp.txt
"""
import os


def tab2space(filename="hightemp.txt"):
    if not os.path.lexists(filename):
        return None
    with open(filename) as f:
        text = f.read()
    return text.replace('\t', ' ')


if __name__ == '__main__':
    print(tab2space())

"""
・sedコマンド:文字列の置換、削除を行う
オプションが複雑すぎるのでgoogle先生に聞いてください

・trコマンド：文字列の一括変換

・expandコマンド：タブをスペースに変換する
expand -t [num] [file]
"""
