with open("hightemp.txt", "r", encoding = "utf-8") as souce:
     # open("hightempedited.txt", "w", encoding = "utf-8") as dest:
    for line in souce:
        # dest.write(line.replace("\t", " ").replace("\r\n", "\n")
        # writeは勝手に改行コードを変える.printも変えるらしい
        print(line.replace("\t", " "), end="")

# sed -e "s/\t/ /g" hightemp.txt 置換
# cat hightemp.txt | tr "\t" " " 一括置換
# expand -t 1 hightemp.txt タブスペース変換
