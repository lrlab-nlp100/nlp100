# coding: UTF-8
# 27. 内部リンクの除去

import re
import extract_from_json

text = extract_from_json.read().split("\n")

kiji = []
kijihyou = []
kijihushi = []

for line in text:
    kiji_line = re.search('[^\[]\[{2}([^\[]*?)\'{2}[^\]]', line)
    if kiji_line is not None:
        kiji.append(kiji_line.group(1))

    kijihyou_line = re.search('[^\']\'{3}([^\']*?)\'{3}[^\']', line)
    if kijihyou_line is not None:
        kijihyou.append(kijihyou_line.group(1))

    kijihushi_line = re.search('[^\']\'{5}([^\']*?)\'{5}[^\']', line)
    if kijihushi_line is not None:
        kijihushi.append(kijihushi_line.group(1))

print(kiji)
print(kijihyou)
print(kijihushi)