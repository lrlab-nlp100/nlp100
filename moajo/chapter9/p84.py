#! /usr/bin/env python

from typing import List
import random,math

# calculate matrix

def load_dict(file_name:str):
    dict_={}
    with open(file_name, "r", encoding="utf-8") as text:
        for i,line in enumerate(text):
            spl = line.strip().split()
            dict_[spl[0]]=int(spl[1])
            print("loading... {0} {2}:{1}".format(file_name,line[:-1],i))
    return dict_

def main():
    t_count=load_dict("p83_t_count.txt")#f(t,*)
    c_count=load_dict("p83_c_count.txt")#f(*,c)
    N=689556292 #p82_contextの行数

    with open("p83_freq.txt", "r", encoding="utf-8") as text:
        with open("p84_mat.txt", "w", encoding="utf-8") as w:
            for i,line in enumerate(text):
                print(i)
                spl = line.split()
                t = spl[0].strip()
                c = spl[1].strip()
                count = int(spl[2].strip())

                if count<10:
                    continue
                ppmi = max(math.log((N*count)/(t_count[t]*c_count[c])),0)
                if ppmi != 0:
                    w.write("{0} {1} {2}\n".format(t,c,ppmi))



if __name__ == "__main__":
    main()
