# 22. カテゴリ名の抽出

import re
from extract_from_json import extract

text = extract('イギリス').split("\n")

pattern = r'^\[\[Category:(.*?)(|\|.*)\]\]$'
repatter = re.compile(pattern)
for i, line in enumerate(text):
    cate_name = repatter.search(line)
    if cate_name is not None:
        print(cate_name.group(1))