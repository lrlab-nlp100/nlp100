import sys

#N = sys.argv[1]
with open("hightemp.txt", "r") as f:
    for line in f.readlines()[:-int(sys.argv[1])]:
        print(line)
    #print(line for line in f.readlines()[:int(sys.argv[1])])

