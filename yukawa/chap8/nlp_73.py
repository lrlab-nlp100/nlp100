# -*- coding: utf-8 -*-
from sklearn.linear_model import LogisticRegression
import re
import pickle
def train(fname,th):
    with open(fname,'r',encoding='latin_1') as f:
        s = set()
        for line in f:
            for word in re.split('\s',line):
                if word != '' and word != '+1' and word != '-1':
                    s.add(word)
        s = list(s)
        s = sorted(s)
        v = []
        y = []
    with open(fname,'r',encoding='latin_1') as f:
        for line in f:
            v_line = [0]*len(s)
            for word in re.split('\s',line):
                if word == '+1':
                    y.append(1)
                elif word == '-1':
                    y.append(0)
                elif word in s:
                    v_line[s.index(word)] = 1
            v.append(v_line)
    lr = LogisticRegression(C=1000.0,tol=th)
    lr.fit(v,y)
    with open('model.pickle',mode='wb') as f:
        pickle.dump((lr,s),f)

if __name__ == '__main__':
    train('sentiment.txt',0.001)
