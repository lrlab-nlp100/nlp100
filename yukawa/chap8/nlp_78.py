# -*- coding: utf-8 -*-
from sklearn.linear_model import LogisticRegression
import re
import nlp_73
import pickle
from stemming.porter2 import stem
import nlp_74
import nlp_77
def cross_validation(th):
    alpha = ['a','b','c','d','e']
    for i in alpha:
        nlp_73.train('train'+i,th)
        with open('model.pickle',mode='rb') as f:
            ret = pickle.load(f)
        lr = ret[0]
        feature = ret[1]
        with open('crossa'+i,'r') as g,open('label'+i,'w') as h:
            for line in g:
                r = nlp_74.estimate(line[3:])
                if r[0] == 1:
                    h.write(str(line[0:2])+'\t+1\t'+str(r[1][0][1])+'\n')
                else:
                    h.write(str(line[0:2])+'\t-1\t'+str(r[1][0][0])+'\n')
    l = []
    for i in alpha:
        l.append(nlp_77.hyoka('label'+i))
    return l

if __name__ == '__main__':
    l = cross_validation(0.001)
    print(list(map(lambda x:x/5,list(map(lambda v,w,x,y,z:v+w+x+y+z,l[0],l[1],l[2],l[3],l[4])))))
