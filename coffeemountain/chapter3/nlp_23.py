import re

with open("england.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

    for line in lines:
        if "==" in line:
            if "====" in line:
                print("3 " + re.findall("====(.*)====", line)[0])
            elif "===" in line:
                print("2 " + re.findall("===(.*)===", line)[0])
            else:
                print("1 " + re.findall("==(.*)==", line)[0])