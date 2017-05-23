#! /usr/bin/env/python

from p30 import read_parsed_data


def main():
    list_ = read_parsed_data()
    for a in filter(lambda obj: obj["pos"] == "動詞", list_):
        print(a["surface"])


if __name__ == "__main__":
    main()
