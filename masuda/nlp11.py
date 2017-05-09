with open("hightemp.txt", "r", encoding = "utf-8") as souce,\
     open("hightempedited.txt", "w", encoding = "utf-8") as dest:
    for line in souce:
        dest.write(line.replace("\t", " "))
