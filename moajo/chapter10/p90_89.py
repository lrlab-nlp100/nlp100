#!/usr/bin/env python

from typing import List
import random,math,sys
import numpy as np
from sklearn.decomposition import PCA,TruncatedSVD
from scipy.sparse import lil_matrix, csr_matrix
from p90_87 import load_vectors

sys.path.append('..')
from chapter10.p90_88 import get_similar_word



def main():
    vectors = load_vectors()
    v_spain = vectors["Spain"]
    v_madrid = vectors["Madrid"]
    v_athens = vectors["Athens"]

    sim_list = get_similar_word(v_spain - v_madrid + v_athens,vectors,10)

    for i,t in enumerate(sim_list):
        cos = t[1]
        word = t[0]
        print(i,"{0} cos:{1}".format(word,cos))

if __name__ == "__main__":
    main()
