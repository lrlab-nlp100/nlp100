#! /usr/bin/env/python

from p30 import read_parsed_data
import collections
import ast
from matplotlib import pyplot
from matplotlib import font_manager


def main():
    list_ = read_parsed_data()
    counter = collections.Counter(map(lambda l: str(l), list_))
    top10 = counter.most_common(10)
    height = list(map(lambda c: c[1], top10))
    label = list(map(lambda c: ast.literal_eval(c[0])["surface"], top10))
    fp = font_manager.FontProperties(fname=r'/Library/Fonts/ipaexg.ttf', size=14)
    pyplot.bar(list(range(10)), height, align="center")
    pyplot.xticks(range(len(label)), label, fontproperties=fp)
    pyplot.xlabel("x axis")
    pyplot.ylabel("y axis")
    pyplot.grid(True)
    pyplot.show()


if __name__ == "__main__":
    main()
