# 25. テンプレートの抽出

import re
from extract_from_json import extract


def extract_template():
    temp_dict = {}
    lines = re.split(r"\n[|}]", extract("イギリス"))

    for line in lines:
        temp_line = re.search("^(.*?)\s=\s(.*)", line)
        if temp_line is not None:
            temp_dict[temp_line.group(1)] = temp_line.group(2)
    return temp_dict

if __name__ == '__main__':
    temp_dict = extract_template()
    for k, v in sorted(temp_dict.items(), key=lambda x: x[0]):
        print(k, ':', v)
