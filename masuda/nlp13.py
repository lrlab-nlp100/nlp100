with open("col1.txt", encoding="utf-8") as col1,\
     open("col2.txt", encoding="utf-8") as col2,\
     open("col12.txt", "w", encoding="utf-8") as col12:
    col12.write(col1.read()[:-1] + "\t" + col2.read())
