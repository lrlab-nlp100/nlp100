# -*- coding: utf-8 -*-
import nlp_78
l = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
#with open('nlp_79.result','w') as f:
#    for i in l:
#        ret = nlp_78.cross_validation(i)
#        f.write(str(ret))

with open('nlp_79.result','r') as f:
    res = f.readlines()
    res = res[0]
    print(type(res[0]))
