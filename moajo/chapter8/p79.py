#! /usr/bin/env python
import sys

import re
from stemming.porter2 import stem

from chapter8.p71 import gen_stop_word_checker
from chapter8.class_logistic_regression import LogisticRegression
from chapter8.p76 import show_result
from matplotlib import pyplot as plt


def main():
    lr = LogisticRegression()
    lr.restore_weights("p73_weights.txt")

    with open("p72_feature.txt", "r", encoding="utf-8")as f:
        lines = f.readlines()

    res = show_result(lines,lr)
    ps = list(map(lambda r: (r.split("\t")[0], float(r.split("\t")[2])), res))
    # for e in ps:
    #     print(e)
    # return

    rates=[]
    precision_rates = []
    recall_rates = []
    f1s=[]
    thresholds = [t / 20 for t in range(20)]
    for threshold in thresholds:
        correct = list(filter(lambda res:res[0]==("+1" if res[1]>threshold else "-1"),ps))#正解
        positive = list(filter(lambda res:res[0]=="+1",ps))#正例
        correct_positive = list(filter(lambda res:res[0]==("+1" if res[1]>threshold else "-1"),positive))#正解の正例
        estimated_positive = list(filter(lambda res:res[1]>threshold,ps))#正例と予測

        rate = len(correct)/len(ps)#正解率
        recall_rate = len(correct_positive)/len(positive)#再現率
        precision_rate = len(correct_positive)/len(estimated_positive)#適合率
        f1 = (2*recall_rate*precision_rate)/(recall_rate+precision_rate)

        rates.append(rate)
        precision_rates.append(precision_rate)
        recall_rates.append(recall_rate)
        f1s.append(f1)
    # print(thresholds)
    # print(precision_rates)
    # print(recall_rates)
    # print(f1s)

    plt.plot(thresholds, precision_rates, label="precision", color="red")
    plt.plot(thresholds, recall_rates, label="recall", color="blue")
    plt.plot(thresholds, f1s, label="f1", color="green")
    plt.plot(thresholds, rates, label="correct_rate", color="black")

    plt.xlabel("threshold")
    plt.ylabel("rate")
    plt.xlim(-0.05, 1.0)
    plt.ylim(0, 1)
    plt.title("Logistic Regression")
    plt.legend(loc=3)

    plt.show()


if __name__ == "__main__":
    main()
