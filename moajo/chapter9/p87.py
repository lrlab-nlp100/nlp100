#! /usr/bin/env python

from typing import List
import random,math,sys
import numpy as np
from sklearn.decomposition import PCA,TruncatedSVD
from scipy.sparse import lil_matrix, csr_matrix

def load_vectors():
    with open("p85_result2.csv","r",encoding="utf-8")as text:
        vector_dict = {}
        for i,line in enumerate(text):
            sys.stdout.write("\rloading... {0}".format(i))
            sys.stdout.flush()
            spl = line.split()
            vec = [float(i) for i in spl[1:]]
            vector_dict[spl[0]]=np.array(vec)
    print("")
    return vector_dict

def main():
    vector_dict = load_vectors()
    v_us = vector_dict["U.S"]
    v_united_states = vector_dict["United_States"]

    cos_sim = (np.dot(v_us,v_united_states)/(np.linalg.norm(v_us)*np.linalg.norm(v_united_states)))
    print("cos_sim: {0}".format(cos_sim))

if __name__ == "__main__":
    main()
