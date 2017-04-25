# 20. JSONデータの読み込み

import json

with open('england.txt', "w", encoding='utf-8') as fw:
    with open('jawiki-country.json', "r", encoding='utf-8') as f:
        for line in f:
            jsonData = json.loads(line)
            if jsonData['title'] == 'イギリス':
                print(jsonData['text'])
                fw.write(jsonData['text'])
