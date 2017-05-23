#! /usr/bin/env python
import sys

import re
from stemming.porter2 import stem

from chapter8.p71 import gen_stop_word_checker
from chapter8.class_logistic_regression import LogisticRegression


def main():
    with open("p76_result.txt", "r", encoding="utf-8")as f:
        lines = f.readlines()

    result = list(map(lambda l:l[:-1].split("\t"),lines))#結果
    correct_result = list(filter(lambda res:res[0]==res[1],result))#正解
    positive = list(filter(lambda res:res[0]=="+1",result))#正例
    correct_positive = list(filter(lambda res:res[0]==res[1],positive))#正解の正例
    estimated_positive = list(filter(lambda res:res[1]=="+1",result))#正例と予測

    rate = len(correct_result)/len(result)#正解率
    recall_rate = len(correct_positive)/len(positive)#再現率
    precision_rate = len(correct_positive)/len(estimated_positive)#適合率
    f1 = (2*recall_rate*precision_rate)/(recall_rate+precision_rate)

    print(rate)
    print(recall_rate)
    print(precision_rate)
    print(f1)






if __name__ == "__main__":
    main()
