#! /usr/bin/env python

from typing import List
import random,math,sys
import numpy as np
from sklearn.decomposition import PCA,TruncatedSVD
from scipy.sparse import lil_matrix, csr_matrix

# show vector of 'United_States'

def main():
    with open("p85_result2.csv", "r", encoding="utf-8") as text:
        for line in text:
            spl = line.split()
            word = spl[0]
            if word=="United_States":
                vec = list(map(lambda s:float(s),spl[1:]))
                print(vec)
                return

if __name__ == "__main__":
    main()
