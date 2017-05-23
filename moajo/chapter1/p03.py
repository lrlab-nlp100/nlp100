#!/usr/bin/env python


def spl_word(s):
    return map(lambda x: x[:-1] if x[-1] == "," or x[-1] == "." else x, s.split(" "))


def main():
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print("".join(map(lambda x: str(len(x)), spl_word(s))))


if __name__ == "__main__":
    main()
