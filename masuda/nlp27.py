import re

with open("text_about_england.txt", encoding="utf-8") as f:
    flag = 0
    dic = {}
    line = f.readline()
    while "基礎情報" not in line:
        line = f.readline()

    str = f.readline()[:-1]
    for line in f:
        if re.match(r"\||\}\}", line) is not None:
            temp = re.split(r"=", str[1:], 1)
            temp2 = re.sub(r"'{2,}", "", temp[1])
            temp2 = re.sub(r"\[\[[^|\]]*\||\]\]", "", temp2)
            temp2 = re.sub(r"\[\[", "", temp2) # 左側のマッチが優先されるので[[はあとから除去
            dic.update({temp[0].strip(): temp2.strip()})
            str = ""
            if re.match(r"\}\}", line) is not None:
                break

        str += line[:-1]

    for key in dic:
        print(key, end="")
        print(" : ", end="")
        print(dic.get(key))

# pprint.pprint()はバグで最後まで表示されない??
