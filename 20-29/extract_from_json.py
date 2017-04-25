# extract_from_json.py

import json


def extract(title):
    with open("jawiki-country.json", encoding='utf-8') as f:
        json_data = f.readline()
        while json_data:
            article_dict = json.loads(json_data)
            if article_dict["title"] == title:
                return article_dict["text"]
            else:
                json_data = f.readline()
    return ""


# ↑の簡易版 イギリスについて保存してあるものを読み込むだけ
def read():
    with open("england.txt", "r", "utf-8") as f:
        return f.read()


if __name__ == '__main__':
    extract("イギリス")
