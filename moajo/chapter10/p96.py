#!/usr/bin/env python

import numpy as np

# 国名だけ抜き出す
# p８１参照



def main():
    with open("p81_countries.txt", "r", encoding="utf-8")as countries:
        hash_ =[ line[:-1].replace(" ", "_") for line in countries]
        with open("p90_vector.txt", "r", encoding="utf-8")as text:
            with open("p96_countries.txt", "w", encoding="utf-8") as w:
                for line in text:
                    c = [w.strip() for w in line.split(" ")][0]
                    if c=="United_States":
                        print(line)
                    if c in hash_:
                        print(c)
                        w.write(line)









if __name__ == "__main__":
    main()
