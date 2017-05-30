import re

with open("england.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

    for line in lines:
        if "ファイル" in line or "File" in line:
            print(re.findall("(File|ファイル):(.*?)\|+?",line)[0][1])
