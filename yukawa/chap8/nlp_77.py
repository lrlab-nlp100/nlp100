# -*- coding: utf-8 -*-
import re
def hyoka(fname):
    with open(fname,'r') as f:
        cnt_a = 0
        cnt_p = 0
        cnt = 0
        cnt_pa = 0
        cnt_par = 0
        cnt_pr = 0
        for line in f:
            cnt += 1
            l = re.split('\t',line)
            if l[0] == l[1]:
                cnt_a += 1
            if l[0] == '+1':
                cnt_p += 1
                if l[1] == '+1':
                    cnt_pa += 1
            if l[1] == '+1':
                cnt_pr += 1
                if l[0] == '+1':
                    cnt_par += 1
    recall = cnt_pa/cnt_p
    pre = cnt_par/cnt_pr
    F = 2*pre*recall/(recall+pre)
    return [cnt_a/cnt,pre,recall,F]

if __name__ == '__main__':
    print(hyoka('label.txt'))
