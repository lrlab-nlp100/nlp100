# -*- coding: utf-8 -*-
# 20. JSONデータの読み込み
#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
import json

def extract_from_json(title):
    with open("jawiki-country.json","r") as json_file:
        for article_json in json_file:
            article_dict = json.loads(article_json)
            if article_dict["title"] == title:
                return article_dict["text"]
    return ""
if __name__ == "__main__":
    print(extract_from_json(u"イギリス"))