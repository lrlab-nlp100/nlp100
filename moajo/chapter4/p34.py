#! /usr/bin/env/python

from p30 import read_parsed_data


def window(seq, n):
    l = []
    for i in range(len(seq) + 1 - n):
        l2 = []
        for k in range(n):
            l2.append(seq[i + k])
        l.append(l2)
    return l


def main():
    list_ = read_parsed_data()
    w = window(list_, 3)

    for a in filter(lambda t: t[1]["base"] == "の" and t[0]["pos"] == "名詞" and t[2]["pos"] == "名詞", w):
        print(a[0]["surface"] + a[1]["surface"] + a[2]["surface"])


if __name__ == "__main__":
    main()
