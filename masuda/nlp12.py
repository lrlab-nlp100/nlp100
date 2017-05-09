with open("hightemp.txt", encoding="utf-8") as f,\
     open("col1.txt", "w", encoding="utf-8") as col1,\
     open("col2.txt", "w", encoding="utf-8") as col2:
    col1.write(f.readline())
    col2.write(f.readline())

