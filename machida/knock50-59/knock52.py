# -*- coding:utf-8 -*-
import knock51
from nltk import stem
stemmer = stem.PorterStemmer()

words = knock51.words
stems = []
for word in words:
    for w in word:
        stems.append(w + '\t' + stemmer.stem(w))
def main():
    for s in stems:
        print(s)

if __name__ == '__main__':
    main()
