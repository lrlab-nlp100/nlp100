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
            dic.update({temp[0].strip(): temp[1].strip()})
            str = ""
            if re.match(r"\}\}", line) is not None:
                break

        str += line[:-1]

    print(dic)

