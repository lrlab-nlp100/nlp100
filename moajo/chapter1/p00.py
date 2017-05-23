#!/usr/bin/env python


def rev_str(s):
    if len(s) == 0:
        return ""
    return rev_str(s[1:]) + s[0]


if __name__ == "__main__":
    print(rev_str("stressed"))
