import re

with open("england.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        if "Category" in line:
            print(line)