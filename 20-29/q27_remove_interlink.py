# 27. 内部リンクの除去

import re
from q25_extract_template import extract_template
from q26_remove_emphasis import remove_emphasis


def remove_interlink(text):
    interlink_pat = re.compile("(.*?)\[{2}([^|]*?)\]{2}(.*?)")
    interlink2_pat = re.compile("(.*?)\[{2}.*?\|(.*?)\]{2}(.*?)")
    text = re.sub(interlink_pat, r'\1\2\3', text)
    text = re.sub(interlink2_pat, r'\1\2\3', text)
    return text


if __name__ == "__main__":
    temp_dict = extract_template()

    for k, v in temp_dict.items():
        temp_dict[k] = remove_emphasis(v)
        temp_dict[k] = remove_interlink(v)

    for k, v in sorted(temp_dict.items(), key=lambda x: x[0]):
        print(k, ':', v)