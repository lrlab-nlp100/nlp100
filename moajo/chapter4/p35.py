#! /usr/bin/env/python

from p30 import read_parsed_data

def get_articulated(list_):
    ret=[]
    idx = -1
    buf = ""
    for i,l in enumerate(list_):
        if l["pos"]=="名詞" and idx==-1:
            idx=i
            buf=l["surface"]
        elif l["pos"]=="名詞":
            buf = buf+l["surface"]
        elif l["pos"]!="名詞":
            if idx!=-1 and idx!=i-1:
                ret.append(buf)
                buf=""
                idx=-1
            else:
                buf = ""
                idx = -1
    return ret


def main():
    list_ = read_parsed_data()
    for v in get_articulated(list_):
        print(v)


if __name__ == "__main__":
    main()
