# coding: UTF-8
# 25. テンプレートの抽出

import re
import extract_from_json

temp_dict = {}
lines = re.split(r"\n[\|}]", extract_from_json.extract("イギリス"))

for line in lines:
    temp_line = re.search("^(.*?)\s=\s(.*)", line)
    if temp_line is not None:
        temp_dict[temp_line.group(1)] = temp_line.group(2)

for k, v in sorted(temp_dict.items(), key=lambda x: x[0]):
    print(k, ':', v)
