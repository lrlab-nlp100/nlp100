with open("col1.txt", encoding="utf-8") as col1,\
     open("col2.txt", encoding="utf-8") as col2,\
     open("col12.txt", "wb") as col12:
    for line1, line2 in zip(col1, col2):
        col12.write((line1[:-1] + "\t" + line2).encode("utf-8"))

# paste col1.txt col2.txt
