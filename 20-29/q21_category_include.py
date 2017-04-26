# 21. カテゴリ名を含む行を抽出

from extract_from_json import extract

text = extract('イギリス').split("\n")

for i, line in enumerate(text):
    if line.find('[[Category') >= 0:
        print(str(i + 1) + '行')
