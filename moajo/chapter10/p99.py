#!/usr/bin/env python

from scipy.cluster.hierarchy import dendrogram,ward,leaves_list
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

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

        t_sne_result = TSNE().fit_transform(vs)
        fig, ax = plt.subplots()
        ax.scatter(t_sne_result[:, 0], t_sne_result[:, 1])
        for index, label in enumerate(cs):
            ax.annotate(label, xy=(t_sne_result[index, 0], t_sne_result[index, 1]))
        plt.savefig('p99_tsne.png')











if __name__ == "__main__":
    main()
