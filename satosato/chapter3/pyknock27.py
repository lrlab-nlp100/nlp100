# -*- coding: utf-8 -*-
# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．


import re
from pyknock20 import extract_from_json

def extract_basis_info(article):
    flag_basis_info = False
    temp_dict = {}
    for string in article:
        start = re.search(u"{{基礎情報(.*?)", string)
        if string == "}}":
            flag_basis_info = False
        if flag_basis_info == True:
            string = string.replace("[", "").replace("]", "").replace("<ref>", "").replace("</ref>", "").replace("<br />", "").replace("<br/>", "").replace("'", "")
            temp = re.search(u"^(.*?)\s=\s(.*)", string)
            if temp is not None:
                temp_dict[temp.group(1).replace("|", "")] = temp.group(2)

        if start is not None:
            flag_basis_info = True
    return temp_dict


if __name__ == "__main__":
    temp = extract_basis_info(extract_from_json(u"イギリス").replace("<br/>\n", "").split("\n"))
    for k, v in sorted(temp.items(), key=lambda x: x[1]):
        print(k, v)