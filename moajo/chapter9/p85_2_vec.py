#! /usr/bin/env python

from typing import List
import random,math
import numpy as np
from sklearn.decomposition import PCA

# 主成分分析で300次元に圧縮。
# scikit-learnを使う。
# まずp84_mat.txtをベクトル化するため、
# t c ppmi
# となっている各行の2行目に現れる単語をリストアップしてインデクシングし数値に変換、
# こうすれば各単語はcのユニークな個数次元のベクトルになる。
#
#
#
# 参考：
#
# pythonで主成分分析のブログ
# http://breakbee.hatenablog.jp/entry/2014/07/13/191803
#
# sklearn公式
# http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
#
# Python: scikit-learn で主成分分析 (PCA) してみる
# http://blog.amedama.jp/entry/2017/04/02/130530
#


def main():

    #load table
    c_hash={}
    with open("p85_table.txt", "r", encoding="utf-8") as text:
        for i,line in enumerate(text):
            print("table",i)
            spl = line.split()
            c_hash[spl[0]] = spl[1]

    #ベクトル列作って、sklearnにつっこむ
    n = 3806151 #p84_matの行数
    vec =[None]*n
    with open("p84_mat.txt", "r", encoding="utf-8") as text:
        with open("p85_vec.txt", "w", encoding="utf-8") as w:
            for i,line in enumerate(text):
                print("tovec",i,line[:-1])
                spl = line.split()
                c = spl[1]
                v = float(spl[2])
                index = c_hash[c]
                vec[i]=[index,spl[2]]#[index]
                w.write("{0} {1} {2}\n".format(spl[0],c_hash[spl[1]],spl[2]))


if __name__ == "__main__":
    main()
