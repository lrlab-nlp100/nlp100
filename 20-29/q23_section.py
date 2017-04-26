# 23. セクション構造

import re
from extract_from_json import extract

text = extract('イギリス').split("\n")

pattern = r'^(=+)\s*(.*?)\s*(=+)$'
repatter = re.compile(pattern)
for line in text:
    section_name = repatter.search(line)
    if section_name is not None and len(section_name.group(1)) == len(section_name.group(3)):
        print(section_name.group(2), len(section_name.group(1)))
