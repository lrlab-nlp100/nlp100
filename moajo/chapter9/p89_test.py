#! /usr/bin/env python

from typing import List
import random,math,sys
sys.path.append('..')
import numpy as np
from sklearn.decomposition import PCA,TruncatedSVD
from scipy.sparse import lil_matrix, csr_matrix
from chapter9.p88 import get_similar_word
from chapter9.p87 import load_word_index,get_word_index,load_vectors,get_word_voctor



def main():
    vectors = load_vectors()

    while True:
        print("1?")
        read = input()
        print("2?")
        read2 = input()
        print("3?")
        read3 = input()

        print(read,read2,read3)


        v_spain = vectors[read]
        v_madrid = vectors[read2]
        v_athens = vectors[read3]

        sim_list = get_similar_word(v_spain - v_madrid + v_athens,vector_list,index_dict,10)

        for i,t in enumerate(sim_list):
            index = t[0]
            cos = t[1]
            word = index_dict[index]
            print(i,"{0} cos:{1}".format(word,cos))

if __name__ == "__main__":
    main()
