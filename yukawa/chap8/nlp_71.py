# -*- coding: utf-8 -*-
from nltk.corpus import stopwords
def is_stop(l):
    if l in stopwords.words('english'):
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_stop('an'))
    print(is_stop('ant'))


