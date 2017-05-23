#!/usr/bin/env python


def zip_str(s1, s2):
    if len(s1) == 0:
        return s2
    if len(s2) == 0:
        return s1
    return s1[0] + s2[0] + zip_str(s1[1:], s2[1:])


if __name__ == "__main__":
    print(zip_str("パトカー", "タクシー"))
