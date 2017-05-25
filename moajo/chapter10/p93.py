#!/usr/bin/env python

from p90_87 import load_vectors
from p90_88 import get_similar_word

def main():
    with open("p92_family_from_90.txt", "r", encoding="utf-8")as f:
        lines = f.readlines()

        spl = [line.split() for line in lines]
        filterd = [a for a in spl if a[3]==a[4]]
        print(len(filterd))
        print("rate:",float(len(filterd))/float(len(lines)))
    with open("p92_family_from_85.txt", "r", encoding="utf-8")as f:
        lines = f.readlines()

        spl = [line.split() for line in lines]
        filterd = [a for a in spl if a[3]==a[4]]
        print(len(filterd))
        print("rate:",float(len(filterd))/float(len(lines)))


if __name__ == "__main__":
    main()
