#! /usr/bin/env python

import re, sys
from stemming.porter2 import stem
from sklearn import svm
from pymongo import MongoClient
from chapter8.p71 import StopwordChecker
from sklearn.model_selection import KFold
import numpy as np
from typing import List


def read_data():
    """
    p70_concatをもんごに突っ込む。ただし既に入ってたら何もしない
    :return:
    """
    with open("p70_concat.txt", "r", encoding="utf-8")as f:
        lines = f.readlines()

    client = MongoClient("localhost:27017")
    c = client["chapter8"]["data"]

    count = c.count()
    if count > 10:
        print("data is already loaded!")
        return

    for l in lines:
        spl = l.strip()
        obj = {"label": spl[:2], "content": spl[3:]}
        c.insert_one(obj)


def extract_feature() -> None:
    """
    read_dataでつっこんだデータから特徴量となる単語を抽出してfeatコレクションに突っ込み直す。
    スキーマは、label,content,feat
    :return:
    """
    print("extracting features...")
    checker = StopwordChecker()
    client = MongoClient("localhost:27017")
    c = client["chapter8"]["data"]
    c_out = client["chapter8"]["feat"]
    if c_out.count() > 10:
        print("feat already extracted!")
        return
    reg = re.compile(r'[,.:;\s]')
    feats = []
    data_count = c.count()
    feat_set = set()
    for i, data in enumerate(c.find()):
        sys.stdout.write("\rextract... {0}/{1}".format(i, data_count + 1))
        # sys.stdout.flush()
        l = data["label"]
        content = data["content"]
        words = reg.split(content)
        stems = [stem(w) for w in words[1:] if w != "" and not checker.isStopword(w)]
        for s in stems:
            feat_set.add(s)
        feats.append({"label": l, "content": content, "feats": stems})
    c_out.insert_many(feats)
    print("")

    client["chapter8"].drop_collection("feat_index")
    c = client["chapter8"]["feat_index"]
    print("feat indexing...")
    for i, s in enumerate(feat_set):
        c.insert_one({"index": i, "feat": s})


def cross_validation()->None:
    """
    5分割交差検定して結果返す
    SVM!
    :return:
    """
    client = MongoClient("localhost:27017")
    c = client["chapter8"]["feat"]
    lr = svm.SVC(kernel="linear", verbose=True)
    X = []  # 1-hotな特徴ベクトル
    y = []  # 正解ラベル 0or1

    si = StemIndexer()
    for data in c.find():  # 抽出された特徴量から全データを学習
        label = data["label"]
        features = data["feats"]

        sparse = si.sentence_to_vec(features)  # 一万次元くらいのベクトル
        a = [0] * si.get_dimension()
        for t in sparse:
            a[t] = 1
        X.append(a)
        y.append(1 if label == "+1" else 0)

    X = np.array(X)
    y = np.array(y)
    print("learning...")
    for train_index, test_index in KFold(5, True).split(X):
        lr.fit(X[train_index], y[train_index])
        output = lr.predict(X[test_index])
        all_result = [[o,t] for o, t in zip(output, y[test_index])]#すべての結果
        correct_answer = [a for a in all_result if a[0] == a[1]]#正解
        positive = [a for a in all_result if a[1]==1]#正例
        correct_positive = len([a for a in positive if a[0]==a[1]])#正解の正例
        estimated_positive = len([a for a in all_result if a[0]==1])  # 正例と予測

        all_count = len(all_result)
        correct_count = len(correct_answer)
        recall_rate = correct_positive / len(positive)  # 再現率
        precision_rate = correct_positive / estimated_positive # 適合率
        f1 = (2 * recall_rate * precision_rate) / (recall_rate + precision_rate)
        print(all_count, correct_count, correct_count / all_count)
        print(f"再現率: {recall_rate}")
        print(f"適合率: {precision_rate}")
        print(f"F1スコア: {f1}")


class StemIndexer:
    def __init__(self):
        c = MongoClient("localhost:27017")["chapter8"]["feat_index"]
        self.stem_to_index = {}
        self.stem_list = [None] * c.count()
        for obj in c.find():
            i = obj["index"]
            s = obj["feat"]
            self.stem_list[i] = s
            self.stem_to_index[s] = i

    def get_index(self, s: str):
        return self.stem_to_index[s]

    def get_stem(self, i: int):
        return self.stem_list[i]

    def get_dimension(self):
        return len(self.stem_list)

    def sentence_to_vec(self, feats: List[str]):
        """
        特徴語幹列をインデックス列に
        :param feats:
        :return:
        """
        idx = [self.get_index(s) for s in feats]
        return idx


def main():
    read_data()
    extract_feature()
    # lr = calc_weights()
    # lr.save_weights("hogehoge33.txt")

    cross_validation()
    return

    lr, X, y = calc_weights2()

    coef = lr.coef_[0]

    top10 = sorted(enumerate(coef), key=lambda a: a[1], reverse=True)[:50]

    si = StemIndexer()
    for a in top10:
        st = si.get_stem(a[0])
        print(st, a[1])

    result = lr.predict_proba(X)


    # for i,res in enumerate(result):
    #     print(res[1],y[i])
    # lr.save_weights("hogehoge33.txt")


if __name__ == "__main__":
    main()
