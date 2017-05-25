#!/usr/bin/env python

from p90_87 import load_vectors
from p90_88 import get_similar_word


def main():
    vectors = load_vectors()
    with open("p91_family.txt", "r", encoding="utf-8")as f:
        with open("p92_family_from_90.txt", "w", encoding="utf-8") as w:
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
