# coding: utf-8
"""
自然言語処理100本ノック

10. 行数のカウント

行数をカウントせよ．
確認にはwcコマンドを用いよ．
"""


def count_line(filename="hightemp.txt"):
    try:
        with open(filename) as f:
            return len(f.readlines())
    except Exception as e:
        print(e)
        return 0


if __name__ == '__main__':
    print(count_line())
