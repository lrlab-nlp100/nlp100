import re

with open("text_about_england.txt", encoding="utf-8") as f:
    p = re.compile(r"(?<=\[\[Category:).*(?=\]\])")
    for line in f:
        m = p.search(line) # matchは(?<=)を使えない
        if m is not None:
            print(m.group(0))
