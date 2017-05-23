#! /usr/bin/env/python

from p30 import read_parsed_data
import collections
import ast
from matplotlib import pyplot
from matplotlib import font_manager
from math import log


def main():
    list_ = read_parsed_data()
    counter = collections.Counter(map(lambda l: str(l), list_))
    x = list(map(lambda c: c[1], counter.most_common()))

    pyplot.hist(x, bins=100, range=(50, 9000))
    pyplot.show()


if __name__ == "__main__":
    main()
