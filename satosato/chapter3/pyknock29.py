# -*- coding: utf-8 -*-
#29. 国旗画像のURLを取得する
#テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）


# -*- coding: utf-8 -*-
# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．


import re
from pyknock20 import extract_from_json
import requests
import json

def extract_basis_info(article):
    flag_basis_info = False
    temp_dict = {}
    for string in article:
        start = re.search(u"{{基礎情報(.*?)", string)
        if string == "}}":
            flag_basis_info = False
        if flag_basis_info == True:
            string = string.replace("[", "").replace("]", "").replace("<br />", "").replace("<br/>", "").replace("'", "").replace("{", "").replace("}", "").replace("*", "")
            temp = re.search(u"^(.*?)\s=\s(.*)", string)
            if temp is not None:
                temp_dict[temp.group(1).replace("|", "")] = re.sub(r"<ref(.*?)((/ref>)|(/>))", "", temp.group(2))

        if start is not None:
            flag_basis_info = True
    return temp_dict


if __name__ == "__main__":
    temp = extract_basis_info(extract_from_json(u"イギリス").replace("<br/>\n", "").split("\n"))
    wiki_api_url = "https://ja.wikipedia.org/w/api.php"
    parameter = {"action":"query",
                 "titles":"File:{}".format(temp["国旗画像"]),
                 "prop":"imageinfo",
                 "format": "json",
                 "iiprop": "url"
                 }
    data_json = requests.get(wiki_api_url, params=parameter).json()
    print(data_json)
    print(data_json["query"]["pages"]["-1"]["imageinfo"][0]["url"])