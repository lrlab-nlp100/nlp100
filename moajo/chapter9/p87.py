#! /usr/bin/env python

from typing import List
import random,math,sys
import numpy as np
from sklearn.decomposition import PCA,TruncatedSVD
from scipy.sparse import lil_matrix, csr_matrix

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

def load_vectors():
    with open("p85_result.csv","r",encoding="utf-8")as text:
        vector_dict = []
        for i,line in enumerate(text):
            vec = [float(i) for i in line.split(",")]
            vector_dict.append(np.array(vec))
    return vector_dict


def get_word_index(word:str,word_dict):
    for k,v in word_dict.items():
        if word==k:
            return v

def get_word_voctor(index:int,vector_dict):
    return vector_dict[index]

def main():
    t = load_word_index()
    index_dict = t[0]
    word_dict = t[1]

    index_us = get_word_index("U.S",word_dict)
    index_united_states = get_word_index("United_States",word_dict)
    print(index_us)
    print(index_united_states)

    vector_dict = load_vectors()
    v_us = get_word_voctor(index_us,vector_dict)
    v_united_states = get_word_voctor(index_united_states,vector_dict)

    cos_sim = (np.dot(v_us,v_united_states)/(np.linalg.norm(v_us)*np.linalg.norm(v_united_states)))
    print("cos_sim: {0}".format(cos_sim))

    return

    with open("p85_result.csv", "r", encoding="utf-8") as text:
        for i,line in enumerate(text):
            if i==256:
                vec = list(map(lambda s:float(s),line.split(",")))
                print(vec)

if __name__ == "__main__":
    main()
