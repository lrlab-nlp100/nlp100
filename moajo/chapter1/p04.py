#!/usr/bin/env python
from p03 import spl_word


def main():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    ar = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    l = list(map(lambda x: (x[1][0], x[0] + 1) if x[0] + 1 in ar else (x[1][0:2], x[0] + 1), enumerate(spl_word(s))))

    def ind(lis):
        if len(lis) == 0:
            return {}
        nex = ind(lis[:-1])
        v = lis[-1]
        nex[v[0]] = v[1]
        return nex

    print(ind(l))


if __name__ == "__main__":
    main()
