import math
from collections import defaultdict

# reference to http://qiita.com/Masaaki_Inaba/items/ddb687daf9e67461a3f7


class LogisticRegression:
    def __init__(self):
        self.weights = defaultdict(float)  # 重みベクトル

    def predict(self, _features: list) -> float:
        """
        識別関数: 重みベクトルと素性リストをインプットとして、肯定的レビューである可能性を予測する
        :param _features レビュー文毎にまとめられた素性のリスト
        :return 肯定的レビューである確率
        """
        # 重みベクトルと素性リストの内積
        x = sum([self.weights[feature] for feature in _features])

        # シグモイド関数
        return 1.0 / (1.0 + math.exp(-x))

    def update(self, _features: list, _label: int, _eta: float) -> None:
        """
        重みベクトルを更新する.
        :param _features レビュー文毎にまとめられた素性のリスト
        :param _label    レビュー文につけられたラベル (肯定的レビュー：+1 / 否定的レビュー：-1)
        :param _eta      学習率
        """
        # 識別関数によって予測した答え (肯定的レビューである確率)
        predict_answer = self.predict(_features)

        # 実際に肯定的レビューであるかどうか (ラベルを確率に変換する (-1 => 0.0000, 1 => 1.0000))
        actual_answer = (float(_label) + 1) / 2

        # 重みベクトルの更新
        for _feature in _features:
            _dif = _eta * (predict_answer - actual_answer)

            # 差が0に近づきすぎたら更新しない
            if 0.0002 > abs(self.weights[_feature] - _dif):
                continue

            # print("update f:{0} diff:{1}".format(_feature,_dif))
            self.weights[_feature] -= _dif

    def calc_weights(self, eta0: float = 0.6, etan: float = 0.9999, sentiments: list = None) -> None:
        """
        重みベクトルを計算
        :param eta0 初期学習率
        :param etan 学習率減少率
        :param sentiments レビューのラベル、文章、素性リストを含む辞書のリスト
        """
        for idx, sentiment in enumerate(sentiments):
            self.update(sentiment['features'], sentiment['label'], eta0 * (etan ** idx))

    def save_weights(self, file_name: str) -> None:
        """
        重みベクトルをファイルに書き出す (ソートしておきます)
        :param file_name ファイル名
        """
        with open(file_name, mode='w', encoding='utf-8') as output:
            for k, v in sorted(self.weights.items(), key=lambda x: x[1]):
                output.write('{}\t{}\n'.format(k, v))

    def restore_weights(self, file_name: str) -> None:
        """
        重みベクトルをファイルから復元する
        :param file_name 重みベクトルが保存されているファイル名
        :return 重みベクトル
        """
        weights = {}
        with open(file_name, encoding='utf-8') as input_file:
            for line in input_file:
                key, value = line.split("\t")
                weights[key] = float(value)

        self.weights = weights
