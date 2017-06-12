#! /usr/bin/env python

from typing import List
import random,math,sys
import numpy as np
from sklearn.decomposition import PCA,TruncatedSVD
from scipy.sparse import lil_matrix, csr_matrix

# 主成分分析で300次元に圧縮。
#
# 圧縮してできたベクトルのデータにラベリングする


# obtain hash map index->word,word->index
def load_word_index():
    with open("p85_vec_index_uniq.txt", "r", encoding="utf-8") as text:
        index_dict = {}
        word_dict = {}
        for line in text:
            spl = line.split()
            index = int(spl[1])
            word = spl[0]
            index_dict[index] = word
            word_dict[word]=index
    return index_dict,word_dict

def main():
    t = load_word_index()
    index_dict = t[0]

    with open("p85_result.csv", "r", encoding="utf-8") as text,\
        open("p85_result2.csv", "w", encoding="utf-8") as w:

        for i,line in enumerate(text):
            print("processing...",i)
            w.write("{0} {1}".format(index_dict[i]," ".join(line.split(","))))





if __name__ == "__main__":
    main()
