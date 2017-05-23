with open("hightemp.txt", encoding="utf-8") as f,\
     open("col1.txt", "wb") as col1,\
     open("col2.txt", "wb") as col2:
     # writeの改行文字変更を避けるためbytesで書き込む
    for line in f:
        col1.write((line[0]+"\n").encode("utf-8"))
        col2.write((line[1]+"\n").encode("utf-8"))


 # cut -b 1-3 hightemp.txt
 # cut -b 4-6 hightemp.txt
