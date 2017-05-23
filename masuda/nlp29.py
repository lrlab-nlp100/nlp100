import re

dic = {}
with open("text_about_england.txt", encoding="utf-8") as f:
    flag = 0
    line = f.readline()
    while "基礎情報" not in line:
        line = f.readline()

    str = f.readline()[:-1]
    for line in f:
        if re.match(r"\||\}\}", line) is not None:
            temp = re.split(r"=", str[1:], 1)
            temp2 = re.sub(r"'{2,}", "", temp[1])
            temp2 = re.sub(r"\[\[[^|\]]*\||\]\]", "", temp2)
            temp2 = re.sub(r"\[\[", "", temp2) # 左側のマッチが優先されるので[[はあとから除去
            temp2 = re.sub(r"<ref.*?</ref>", "", temp2)
            temp2 = re.sub(r"<.*?/>", "", temp2)

            dic.update({temp[0].strip(): temp2.strip()})
            str = ""
            if re.match(r"\}\}", line) is not None:
                break

        str += line[:-1]

import requests
url = "https://en.wikipedia.org/w/api.php"
payload = {"action": "query",
           "titles": "File:{}".format(dic["国旗画像"]),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}

json_data = requests.get(url, params=payload).json()

print(json_data["query"]["pages"]["23473560"]["imageinfo"][0]["url"])
