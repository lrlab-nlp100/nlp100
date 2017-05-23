#! /usr/bin/env python
import sys

import re
from stemming.porter2 import stem

from chapter8.p71 import gen_stop_word_checker
from chapter8.class_logistic_regression import LogisticRegression
from chapter8.p73 import calc_weights
from chapter8.p76 import show_result

def show_score(lines):
    result = list(map(lambda l: l.split("\t"), lines))  # 結果
    correct_result = list(filter(lambda res: res[0] == res[1], result))  # 正解
    positive = list(filter(lambda res: res[0] == "+1", result))  # 正例
    correct_positive = list(filter(lambda res: res[0] == res[1], positive))  # 正解の正例
    estimated_positive = list(filter(lambda res: res[1] == "+1", result))  # 正例と予測

    rate = len(correct_result) / len(result)  # 正解率
    recall_rate = len(correct_positive) / len(positive)  # 再現率
    precision_rate = len(correct_positive) / len(estimated_positive)  # 適合率
    f1 = (2 * recall_rate * precision_rate) / (recall_rate + precision_rate)

    print("正解率:\t{0}".format(rate))
    print("再現率:\t{0}".format(recall_rate))
    print("適合率:\t{0}".format(precision_rate))
    print("f1スコア:\t{0}".format(f1))


def main():
    with open("p72_feature.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = list(filter(lambda l:l[:-1],lines))
    line_count = len(lines)//5
    line_array = [lines[:line_count],
                  lines[line_count:2*line_count],
                  lines[2*line_count:3*line_count],
                  lines[3*line_count:4*line_count],
                  lines[4*line_count:]]

    for i in range(5):
        ans = line_array[i]
        other = line_array[:i]+line_array[i+1:]
        lr = calc_weights([flatten for inner in other for flatten in inner])
        result = show_result(ans,lr)
        show_score(result)
        print("----------")
    return



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
