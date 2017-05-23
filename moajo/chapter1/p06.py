#!/usr/bin/env python

from p05 import n_gram


def to_set(h):
    s = set([])
    for elem in h:
        s.add(elem)
    return s


def main():
    x = to_set(n_gram("paraparaparadise", 2))
    y = to_set(n_gram("paragraph", 2))

    print(x.union(y))
    print(x.difference(y))
    print(x.intersection(y))

    print("se" in x)
    print("se" in y)


if __name__ == "__main__":
    main()
