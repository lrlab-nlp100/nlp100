#! /usr/bin/env python

from chapter8.class_logistic_regression import LogisticRegression


# 73. 学習
# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
def calc_weights(lines) -> LogisticRegression:
    lr = LogisticRegression()
    sentiments = []
    for line in lines:
        spl = line[:-1].split("\t")
        label = spl[0].split(" ")[0]
        features = spl[1].split(" ")
        sentiments.append({"features": features, "label": label})

    lr.calc_weights(sentiments=sentiments)
    return lr


def main():
    with open("p72_feature.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    lr = calc_weights(lines)

    lr.save_weights("p73_weights.txt")


if __name__ == "__main__":
    main()
