# -*- coding:utf-8 -*-
import knock50

sentence = knock50.sentence
words = []
for s in sentence:
    word = [w.strip('().,?:;') for w in s.split()]
    words.append(word)

def main():
    for word in words:
        for w in word:
            print(w)
        print()

if __name__ == '__main__':
    main()
