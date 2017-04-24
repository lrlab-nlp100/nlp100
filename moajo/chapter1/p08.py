#!/usr/bin/env python


import re


def cipher_08(src: str):
    lower_reg = re.compile(r'^[a-z]+$')

    if len(src) == 0:
        return ""
    for s in src:
        if lower_reg.match(s) is not None:
            return bytes([219 - s.encode()[0]]).decode() + cipher_08(src[1:])
        else:
            return s + cipher_08(src[1:])


def main():
    print(cipher_08("abc"))
    print(cipher_08(cipher_08("abc")))


if __name__ == "__main__":
    main()
