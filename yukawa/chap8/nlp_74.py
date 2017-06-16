# -*- coding: utf-8 -*-
from sklearn.linear_model import LogisticRegression
import sys
from stemming.porter2 import stem
import pickle
import re
def estimate(s):
    with open('model.pickle',mode='rb') as f:
        ret = pickle.load(f)
        lr = ret[0]
        f = ret[1]
        l = list(filter(lambda w:len(w) > 0,re.split('\s|"|,|\.|\'|\(|\)|\-\-|:|;',s)))
        l = list(map(stem,l))
        v = [0]*len(f)
        for word in l:
            if word in f:
                v[f.index(word)] = 1
        p = lr.predict_proba(v)
    return (lr.predict(v),p)

if __name__ == '__main__':
    s = input()
    ret = estimate(s)
    if ret[0] == 1:
        print('+1',ret[1][0][1])
    else:
        print('-1',ret[1][0][0])
