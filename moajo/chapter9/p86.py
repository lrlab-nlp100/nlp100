#! /usr/bin/env python

from typing import List
import random,math,sys
import numpy as np
from sklearn.decomposition import PCA,TruncatedSVD
from scipy.sparse import lil_matrix, csr_matrix

# show vector of 'United_States'
#
# excecute `cat p85_vec_index_uniq.txt |grep [word]`
# to obtain index of the vector.

def main():
    with open("p85_result.csv", "r", encoding="utf-8") as text:
        for i,line in enumerate(text):
            if i==256:
                vec = list(map(lambda s:float(s),line.split(",")))
                print(vec)

if __name__ == "__main__":
    main()
