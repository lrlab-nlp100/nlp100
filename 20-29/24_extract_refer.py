# coding: UTF-8
# 24. ファイル参照の抽出

import re
from extract_from_json import extract_from_json

text = extract_from_json(u'イギリス').split("\n")

for line in text:
    file_name = re.search(u'(ファイル|File):(.*?)\|', line)
    if file_name is not None:
        print(file_name.group(2))
