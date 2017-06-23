# -*- coding: utf-8 -*-
import pickle
import nlp_74
from sklearn.linear_model import LogisticRegression
with open('model.pickle',mode='rb') as f:
    ret = pickle.load(f)
f = ret[1]
lr = ret[0]
with open('sentiment.txt','r') as g,open('label.txt','w') as h:
    for line in g:
        r = nlp_74.estimate(line[3:])
        if r[0] == 1:
            h.write(str(line[0:2])+'\t+1\t'+str(r[1][0][1])+'\n')
        else:
            h.write(str(line[0:2])+'\t-1\t'+str(r[1][0][0])+'\n')
