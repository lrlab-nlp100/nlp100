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

    #generate table
    c_hash={}
    index=0
    print("generate table...")
    with open("p84_mat.txt", "r", encoding="utf-8") as text:
        with open("p85_table.txt", "w", encoding="utf-8") as w:
            for i,line in enumerate(text):
                print("gen",i)
                spl = line.split()
                c = spl[1]
                if c in c_hash:
                    continue
                c_hash[c] = index
                index+=1
            for k,v in c_hash.items():
                w.write("{0} {1}\n".format(k,v))


if __name__ == "__main__":
    main()
