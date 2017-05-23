# coding: utf-8
u"""
自然言語処理100本ノック

29. 国旗画像のURLを取得する

テンプレートの内容を利用し，国旗画像のURLを取得せよ
"""


from no20 import read_json
from no25_28 import get_tempdic
#import urllib
#import urllib2
import requests


def no29(article):
    dic = get_tempdic(article)
    url = "https://www.mediawiki.org/w/api.php"
    values = {
        "action": "query",
        "titles": "File:{svg}".format(svg=dic[u"国旗画像"]),
        "prop": "imageinfo",
        "format": "json",
        "iiprop": "url"}

    req = requests.get(url, params=values).json()
    print(req["query"]["pages"]["-1"]["imageinfo"][0]["url"])    # 無理やり出しただけです


if __name__ == '__main__':
    no29(read_json())
