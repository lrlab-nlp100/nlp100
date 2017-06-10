#!/usr/bin/env python

from p90_87 import load_vectors
from p90_88 import get_similar_word
import numpy as np


def get_sim(vec1,vec2,vectors):
    vec1_normalized = vec1/np.linalg.norm(vec1)
    vec2_normalized = vec2/np.linalg.norm(vec2)
    return np.dot(vec1_normalized,vec2_normalized)

def main():
    vectors = load_vectors()
    with open("wordsim353/combined.csv", "r", encoding="utf-8")as f:
        with open("p94_combined.csv", "w", encoding="utf-8") as w:
            #precedent,group,1.77
            for i,line in enumerate(f):
                if i==0:
                    continue
                spl = [w.strip() for w in line.split(",")]
                print("processing.... {0}-{1}+{2}".format(spl[1],spl[0],spl[2]))
                sim = get_sim(vectors[spl[0]],vectors[spl[1]],vectors)
                print("{0}: {1} {2} --- {3}".format(i,spl[0],spl[1],sim))
                w.write(",".join(spl)+",{0}\n".format(sim))


if __name__ == "__main__":
    main()
