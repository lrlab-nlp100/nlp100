# -*- coding: utf-8 -*-
import pickle
from sklearn.linear_model import LogisticRegression
with open('model.pickle',mode='rb') as f:
    ret = pickle.load(f)
f = ret[1]
lr = ret[0]
w = lr.coef_[0]
d = list(zip(f,w))
d = sorted(d,key=lambda x:int(x[1]))
print(d[-10:-1][::-1])
print(d[0:10])
