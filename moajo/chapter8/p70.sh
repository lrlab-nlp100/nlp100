#!/usr/bin/env zsh

# 70. データの入手・整形
# 文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．
# rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
# rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
# 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
# sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

# p70_concatを生成。正解ラベルを付けてランダムに並び替える。
# (+-)1 (sentence)
cat rt-polaritydata/rt-polarity.pos| gsed -e "s/^/+1 /g" > rt-polaritydata/rt-polarity.pos.p70.txt
cat rt-polaritydata/rt-polarity.neg| gsed -e "s/^/-1 /g" > rt-polaritydata/rt-polarity.neg.p70.txt


cat rt-polaritydata/rt-polarity.pos.p70.txt rt-polaritydata/rt-polarity.neg.p70.txt | LC_ALL=C sort -R > p70_concat.txt

# 文字コード変換が必要ぽい？
nkf --ic=ISO-8859-1 -w p70_concat.txt > p70_concat.txt
