# coding: UTF-8
# 26. 強調マークアップの除去

import re
import extract_from_json

text = extract_from_json.read().split("\n")

kubetsu = []
kyoutyou = []
syataikyou = []

for line in text:
    kubetsu_line = re.search('[^\']\'{2}([^\']*?)\'{2}[^\']', line)
    if kubetsu_line is not None:
        kubetsu.append(kubetsu_line.group(1))

    kyoutyou_line = re.search('[^\']\'{3}([^\']*?)\'{3}[^\']', line)
    if kyoutyou_line is not None:
        kyoutyou.append(kyoutyou_line.group(1))

    syataikyou_line = re.search('[^\']\'{5}([^\']*?)\'{5}[^\']', line)
    if syataikyou_line is not None:
        syataikyou.append(syataikyou_line.group(1))

print(kubetsu)
print(kyoutyou)
print(syataikyou)
