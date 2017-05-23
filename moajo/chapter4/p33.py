#! /usr/bin/env/python

from p30 import read_parsed_data


def main():
    list_ = read_parsed_data()
    for a in filter(lambda obj: obj["pos1"] == "サ変接続", list_):
        print(a)


if __name__ == "__main__":
    main()
