#!/usr/bin/env python

import re
import json
from p20 import read_eng
from common import get_brace


def main():
    str_ = read_eng()
    pos = str_.find("{{基礎情報")
    content = get_brace(str_, pos, "{{", "}}")[:-2]
    regex = re.compile(r"(.+?)=(.+)")
    obj = {}
    for s in content.split("\\n|")[1:]:
        match = regex.match(s)
        sub = re.sub(r"'{2,5}(.*?)'{2,5}", r"\1", match.group(2))
        sub = re.sub(r"\[\[(?!ファイル)(?:[^:|\]]+\|)?(.+?)\]\]", r"\1", sub)
        sub = re.sub(r"<br */>", r"", sub)
        sub = re.sub(r"{{lang\|...?\|(.+?)}}", r"\1", sub)
        sub = re.sub(r"<ref>(.+?)</ref>", r"\1", sub)
        obj[match.group(1).strip()] = sub
    img_name = obj["国旗画像"]

    import urllib.request, urllib.parse
    params = {
        "action": "query",
        "titles": "File:" + img_name,
        "prop": "imageinfo",
        "format": "json",
        "iiprop": "url"
    }
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)

    with urllib.request.urlopen(url) as res:
        js = json.loads(res.read().decode("utf-8"))
        print(js["query"]["pages"]["347935"]["imageinfo"][0]["url"])


if __name__ == "__main__":
    main()
