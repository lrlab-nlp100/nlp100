#!/usr/bin/env python

from p90_88 import get_similar_word
from typing import List
import random,math,sys
import numpy as np
from sklearn.decomposition import PCA,TruncatedSVD
from scipy.sparse import lil_matrix, csr_matrix

def load_vectors():
    with open("../chapter9/p85_result2.csv","r",encoding="utf-8")as text:
        vector_dict = {}
        for i,line in enumerate(text):
            if i==0:
                continue #skip line 1
            sys.stdout.write("\rloading... {0}".format(i))
            sys.stdout.flush()
            spl = line.split(" ")
            vec = [float(i) for i in spl[1:-1]]
            vector_dict[spl[0]]=np.array(vec)
    print("")
    return vector_dict


def main():
    vectors = load_vectors()
    with open("p91_family.txt", "r", encoding="utf-8")as f:
        with open("p92_family_from_85.txt", "w", encoding="utf-8") as w:
            for i,line in enumerate(f):
                spl = line.split()
                print("processing.... {0}-{1}+{2}".format(spl[1],spl[0],spl[2]))
                sim_list = get_similar_word(vectors[spl[1]]-vectors[spl[0]]+vectors[spl[2]],vectors,5)

                print("similers: ")
                for a in ["\t{0}\t{1}".format(t[0],t[1]) for t in sim_list]:
                    print(a)

                t= sim_list[0]
                cos = t[1]
                word = t[0]
                print("{2}: {0} cos:{1}".format(word,cos,i))
                w.write(" ".join(spl)+" {0} {1}\n".format(word,cos))
                print("")


if __name__ == "__main__":
    main()
