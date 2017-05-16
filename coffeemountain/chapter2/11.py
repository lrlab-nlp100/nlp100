f = open("hightemp.txt", "r")

for line in f:
    line.replace("\t", " ")