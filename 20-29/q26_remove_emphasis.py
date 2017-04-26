# 26. 強調マークアップの除去

import re
from q25_extract_template import extract_template

def remove_emphasis(text):
    kubetsu_pat = re.compile("(.*?[^\'])\'{2}([^\'].*?)\'{2}([^\'].*?)")
    kyoutyou_pat = re.compile("(.*?[^\'])\'{3}([^\'].*?)\'{3}([^\'].*?)")
    yataikyou_pat = re.compile("(.*?[^\'])\'{5}([^\'].*?)\'{5}([^\'].*?)")
    text = re.sub(kubetsu_pat, r'\1\2\3', text)
    text = re.sub(kyoutyou_pat, r'\1\2\3', text)
    text = re.sub(yataikyou_pat, r'\1\2\3', text)
    return text


if __name__ == "__main__":
    temp_dict = extract_template()

    for k, v in temp_dict.items():
        temp_dict[k] = remove_emphasis(v)

    for k, v in sorted(temp_dict.items(), key=lambda x: x[0]):
        print(k, ':', v)
