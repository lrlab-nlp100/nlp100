# coding: utf-8
"""
自然言語処理100本ノック

08. 暗号文

与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

*英小文字ならば(219 - 文字コード)の文字に置換
*その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．


アトバッシュ法という暗号方式らしい
"""


def cipher(x):
    out = ""
    for i in x:
        i = i if not i.islower() else chr(219 - ord(i))
        out += i
    return out


if __name__ == "__main__":
    mes = "I'm GOD of udon!"
    seq = cipher(mes)   # 暗号化
    print(seq)
    print(cipher(seq))   # 復号化
