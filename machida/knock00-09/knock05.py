# -*- coding: utf-8 -*-

# ngramw->word, ngramc->character
def ngramw(str, n):
    res = []
    str = str.split(" ")
    for i in range(len(str) - n + 1):
        res.append(str[i:i+n])
    return res

def ngramc(str, n):
    res = []
    str = str.replace(" ", "")
    for i in range(len(str) - n + 1):
        res.append(str[i:i+n])
    return res

def main():
    str = "I am an NLPer"

    print("word", end="")
    print(ngramw(str, 2))
    print("character", end="")
    print(ngramc(str, 2))

if __name__ == '__main__':
    main()
