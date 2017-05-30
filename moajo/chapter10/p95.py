#!/usr/bin/env python

import numpy as np

# p94の２つのモデルの結果をそれぞれ評価する
# スピアマン順位相関係数で評価する
# http://kusuri-jouhou.com/statistics/soukan.html

# love,sex,6.77,0.36284199184106003
#

def spearman(ranks):
    l = []
    for k,v in ranks.items():
        d = v["rank"]-v["human"]
        l.append(d*d)
    n = len(l)
    s = sum(l)
    return 1-(6*s/(n*n*n-n))



def main():
    with open("p94_combined.csv", "r", encoding="utf-8")as f1,\
         open("p94_combined_85.csv", "r", encoding="utf-8") as f2:
        f1_lines = [[a.strip() for a in l.split(",")] for l in f1.readlines()]
        f2_lines = [[a.strip() for a in l.split(",")]for l in f2.readlines()]

        # calculate rank by model
        f1_lines.sort(key=lambda a:float(a[3]),reverse=True)
        f2_lines.sort(key=lambda a:float(a[3]),reverse=True)

        print("model_90 ranks:")
        f1_rank={}
        for i,l in enumerate(f1_lines):
            print("{0}: {1} {2} {3}".format(i,l[0],l[1],l[3]))
            f1_rank["{0} {1}".format(l[0],l[1])]={"rank":i}

        print("model_85 ranks:")
        f2_rank={}
        for i,l in enumerate(f2_lines):
            print("{0}: {1} {2} {3}".format(i,l[0],l[1],l[3]))
            f2_rank["{0} {1}".format(l[0],l[1])]={"rank":i}

        # calculate rank by human
        f1_lines.sort(key=lambda a:float(a[2]),reverse=True)
        f2_lines.sort(key=lambda a:float(a[2]),reverse=True)

        for i,l in enumerate(f1_lines):
            f1_rank["{0} {1}".format(l[0],l[1])]["human"]=i

        for i,l in enumerate(f2_lines):
            f2_rank["{0} {1}".format(l[0],l[1])]["human"]=i

        print("f1 spearman: {0}".format(spearman(f1_rank)))
        print("f2 spearman: {0}".format(spearman(f2_rank)))









if __name__ == "__main__":
    main()
