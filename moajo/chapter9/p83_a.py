#! /usr/bin/env python

from typing import List
import random,sys


#calculate f(t,*),f(*,c)
# N is calculated by `wc -l p83_freq.txt`.
def main():
    buffer_={}
    with open("p83_freq.txt", "r", encoding="utf-8") as text:
        for i,line in enumerate(text):
            line = line.strip()
            spl = line.split()
            if len(spl)!=3:
                print("spl not equals 3")
                sys.stderr.write("spl not equals 3")
                print("{0} {1}".format(i,line))
                sys.stderr.write("{0} {1}".format(i,line))
                continue
            t = spl[0]
            c = spl[1]
            count = spl[2]

            print("{0}: {1} {2} {3}".format(i,t,c,count))
            if t in buffer_:
                buffer_[t][c]=int(count)
            else:
                buffer_[t]={c:int(count)}

    with open("p83_t_count.txt", "w", encoding="utf-8") as w:
        for t,v in buffer_.items():
            t_count=0 #f(t,*)
            for c,count in v.items():
                t_count+=count
            w.write("{0} {1}\n".format(t,t_count))
    with open("p83_c_count.txt", "w", encoding="utf-8") as w:
        c_count={}
        for t,v in buffer_.items():
            for c,count in v.items():
                if c in c_count:
                    c_count[c]+=count
                else:
                    c_count[c]=count
        for c,count in c_count.items():
            w.write("{0} {1}\n".format(c,count))


if __name__ == "__main__":
    main()
