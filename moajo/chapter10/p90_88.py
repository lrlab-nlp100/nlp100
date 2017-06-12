#!/usr/bin/env python

from typing import List
import random,math,sys
import numpy as np
from sklearn.decomposition import PCA,TruncatedSVD
from scipy.sparse import lil_matrix, csr_matrix
from p90_87 import load_vectors

def get_similar_word(vec,vectors,count):
    vec_normalized = vec/np.linalg.norm(vec)

    print("calculating cos sim...")
    cos_list = [None] * len(vectors)
    i=0
    for word, v in vectors.items():
        norm = np.linalg.norm(v)
        cos = np.dot(vec_normalized, v) / norm
        sys.stdout.write("\r{0}:\tcos:{1}".format(word, cos))
        sys.stdout.flush()
        cos_list[i] = (word, cos)
        i+=1
    cos_list.sort(key=lambda t: t[1], reverse=True)
    print("")

    return cos_list[:count]


def main():
    vectors = load_vectors()
    v_eg = vectors["England"]

    sim_list = get_similar_word(v_eg,vectors,10)

    for i,t in enumerate(sim_list):
        cos = t[1]
        word = t[0]
        print(i,"{0} cos:{1}".format(word,cos))

if __name__ == "__main__":
    main()
