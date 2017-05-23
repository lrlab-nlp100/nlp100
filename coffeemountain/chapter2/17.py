with open("hightemp.txt") as f:
    print(list(set([line.split("\t")[0] for line in f])))