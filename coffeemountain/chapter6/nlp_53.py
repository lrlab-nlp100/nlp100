from nltk.stem.porter import PorterStemmer
from nlp_52 import *

if __name__ == '__main__':
    tokens_list = text_tokenizer('nlp.txt')
    stemmer = PorterStemmer()
    for tokens in tokens_list:
        for token in tokens:
            print("%s\t%s" % (token, stemmer.stem(token)))