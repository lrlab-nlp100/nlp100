#! /usr/bin/env python

from typing import List
import random,math,sys
import numpy as np
from sklearn.decomposition import PCA,TruncatedSVD
from scipy.sparse import lil_matrix, csr_matrix

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

    #ベクトル列作って、sklearnにつっこむ
    n = 3806151 #p84_matの行数
    # vec =[None]*n
    a=lil_matrix((136732,n))

    index=-1
    current_word=""
    with open("p85_vec.txt", "r", encoding="utf-8") as text:
        with open("p85_vec_index.txt", "w", encoding="utf-8") as vec_file:
            for i,line in enumerate(text):
                sys.stdout.write("\rload {0}".format(i))
                sys.stdout.flush()
                spl = line.split()
                w = spl[0]
                if current_word!=w:
                    current_word=w
                    index+=1

                # vec[i]=[int(spl[1]),float(spl[2])]#[index]
                a[index,int(spl[1])]=float(spl[2])
                vec_file.write("{0} {1}\n".format(w,index))
    print("\nindex:",index)
    csr = a.tocsr()

    print(csr.shape)
    print(csr.ndim)

    decomp = TruncatedSVD(n_components=300)
    decomp.fit(csr)

    print(decomp.explained_variance_ratio_)
    transformed = decomp.fit_transform(csr)
    # print(transformed.shape)
    np.savetxt("p85_result.csv", transformed, delimiter=",")







if __name__ == "__main__":
    main()
