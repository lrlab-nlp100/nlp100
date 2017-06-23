# -*- coding: utf-8 -*-
import re
with open('corpus.txt','r') as f:
    for line in f:
        word_list = re.split(' ',line[:-1])
        for word in word_list:
            
