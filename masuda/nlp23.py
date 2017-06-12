import re

with open("text_about_england.txt", encoding="utf-8") as f:
    p = re.compile(r"(={2,})([^=]*)(={2,})")
    for line in f:
        m = p.search(line)
        if m is not None:
            print(m.group(2), end=" ")
            print("level " + str(len(m.group(1)) - 1))
