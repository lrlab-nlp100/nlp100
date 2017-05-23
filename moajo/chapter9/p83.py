#! /usr/bin/env python

from typing import List
import random

# calculate only freq f(t,c) from p82_context.txt
# othert data is calculated by p83_a.py
def main():
    result={}
    with open("p82_context.txt", "r", encoding="utf-8") as text:
        for i,line in enumerate(text):
            print(line[:-1])
            spl = line.split("\t")
            w = spl[0].strip()
            cw = spl[1].strip()

            print("{0}: {1} {2}".format(i,w,cw))

            if w in result:
                res = result[w]
                if cw in res:
                    res[cw]+=1
                else:
                    res[cw]=1
            else:
                result[w]={cw:1}
    with open("p83_freq.txt", "w", encoding="utf-8") as w:
        for key,v in result.items():
            for c,count in v.items():
                w.write("{0} {1} {2}\n".format(key,c,count))


if __name__ == "__main__":
    main()
