import re

with open("text_about_england.txt", encoding="utf-8") as f:
    p = re.compile(r"(?<=\[\[File:)[^|]*(?=|)")
    for line in f:
        m = p.search(line)
        if m is not None:
            print(m.group(0))
