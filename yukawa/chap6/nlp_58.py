# -*- coding: utf-8 -*-
import re
pa_d = re.compile(r'dep type=\"dobj\"')
pa_s = re.compile(r'dep type=\"nsubj\"')
pa_g = re.compile(r'<governor idx=(.+?)>(.+?)</governor>')
pa_de = re.compile(r'<dependent idx=(.+?)>(.+?)</dependent>')
pa_c = re.compile(r'collapsed-dependencies')
flag,s_flag,d_flag = 0,0,0
sub_p,dob_p,dob_c,sub_c = None,None,None,None
sub,dob,dobc,subc = '','','',''
with open('nlp.txt.xml','r') as f:
    for line in f:
        if pa_c.search(line) is not None:
            flag += 1
            s_flag = 0
            d_flag = 0
        if flag != 0 and pa_s.search(line) is not None:
            s_flag += 1
        if flag != 0 and pa_d.search(line) is not None:
            d_flag += 1
        if s_flag != 0:
            sub_p = pa_g.search(line)
            sub_c = pa_de.search(line)
            if sub_p is not None:
                sub = sub_p.group(2)
            if sub_c is not None:
                subc = sub_c.group(2)
                s_flag = 0
        if d_flag != 0:
            dob_p = pa_g.search(line)
            dob_c = pa_de.search(line)
            if dob_p is not None:
                dob = dob_p.group(2)
            if dob_c is not None:
                dobc = dob_c.group(2)
                d_flag = 0
        if sub != '' and subc != '' and dobc != '' and sub == dob: 
            print(subc+'\t'+sub+'\t'+dobc)
            s_flag = 0
            dob,sub,dobc,subc = '','','',''
            d_flag = 0
