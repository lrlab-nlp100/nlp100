#! /usr/bin/env python
import sys


# 71. ストップワード
# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
# さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．
# さらに，その関数に対するテストを記述せよ．

# p71_stopwordに引数が入ってるか確認する。
# これ自体は適当にネットから持ってきた。

class StopwordChecker:
    def __init__(self):
        with open("p71_stopword.txt", "r", encoding="utf-8") as f:
            self.stops = f.readlines()

    def isStopword(self, w: str) -> bool:
        return w in [s[:-1] for s in self.stops]


def main():
    arg = sys.argv[1]
    checker = StopwordChecker()

    print(checker.isStopword(arg))


if __name__ == "__main__":
    main()
