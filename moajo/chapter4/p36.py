#! /usr/bin/env/python

from p30 import read_parsed_data
import collections


def main():
    list_ = read_parsed_data()
    counter = collections.Counter(map(lambda l: str(l), list_))
    for v in counter.most_common():
        print(v)


if __name__ == "__main__":
    main()
