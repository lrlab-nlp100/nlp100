#!/usr/bin/env python


from typing import Mapping, Sequence, Callable
from p03 import spl_word


def window(src: Sequence, n: int, f: Callable[[Sequence, int], any]) -> None:
    for i in range(len(src) - n + 1):
        f(src[i:i + n], i)


def n_gram(src: str, n: int) -> Mapping[str, int]:
    gram = {}

    def f(s: str, index: int):
        if s in gram:
            gram[s] = gram[s] + 1
        else:
            gram[s] = 1

    window(src, n, f)
    return gram


def word_n_gram(src: str, n: int):
    gram = {}

    def f(s: Sequence[str], index: int) -> None:
        j = ",".join(s)
        if j in gram:
            gram[j] = gram[j] + 1
        else:
            gram[j] = 1

    window(list(spl_word(src)), n, f)
    return gram


def main():
    s = "I am an NLPer"
    print(n_gram(s, 2))
    print(word_n_gram(s, 2))


if __name__ == "__main__":
    main()
