#!/usr/bin/env python

import numpy as np
from sklearn.cluster import KMeans

# p96の国名ベクトルをk-meansクラスタリング
# k=5
#
# http://pythondatascience.plavox.info/scikit-learn/%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E5%88%86%E6%9E%90-k-means



def main():
    with open("p96_countries.txt", "r", encoding="utf-8") as text:
        lines = text.readlines()
        cs = []
        vs = []
        for line in lines:
            print(line)
            spl = line.split()
            cs.append(spl[0])
            vec = np.array([float(v) for v in spl[1:]])
            vs.append(vec)


        pred = KMeans(n_clusters=5).fit_predict(vs)
        for i,country in enumerate(cs):
            print("{0} {1}".format(country,pred[i]))









if __name__ == "__main__":
    main()
