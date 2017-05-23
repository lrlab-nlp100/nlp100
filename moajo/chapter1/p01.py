#!/usr/bin/env python


def odd_str(s):
    if len(s) == 0:
        return ""
    return s[0] + odd_str(s[2:])


if __name__ == "__main__":
    print(odd_str("パタトクカシーー"))
