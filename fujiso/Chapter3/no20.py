# coding: utf-8
"""
自然言語処理100本ノック

20. JSONデータの読み込み

Wikipedia記事のJSONファイルを読み込み，
「イギリス」に関する記事本文を表示せよ．

(問題21-29では，ここで抽出した記事本文に対して実行せよ．)
"""

import json


def read_json(title="イギリス", file="jawiki-country.json"):
    with open(file) as f:
        for article in f:
            a_dict = json.loads(article)
            if a_dict["title"] == title:
                return a_dict["text"]

    print("topic not found.")
    return str()


if __name__ == '__main__':
    print(read_json())
