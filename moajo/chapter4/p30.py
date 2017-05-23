#! /usr/bin/env/python

def line_to_obj(line):
    obj = {}
    a = line.split("\t")
    if len(a) != 2:
        return None
    obj["surface"] = a[0]
    data_ = a[1].split(",")
    obj["base"] = data_[6]
    obj["pos"] = data_[0]
    obj["pos1"] = data_[1]
    return obj


def read_parsed_data():
    list_ = []
    with open("neko.txt.mecab", encoding="utf-8") as f:
        s = f.readlines()
        for l in s:
            obj = line_to_obj(l)
            if obj is None:
                continue
            list_.append(obj)
    return list_


def main():
    list_ = read_parsed_data()
    for a in list_:
        print(a)


if __name__ == "__main__":
    main()
