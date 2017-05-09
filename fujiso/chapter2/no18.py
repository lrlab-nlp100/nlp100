# coding: utf-8
u"""
自然言語処理100本ノック

18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ
（注意: 各行の内容は変更せずに並び替えよ）．

確認にはsortコマンドを用いよ
（この問題はコマンドで実行した時の結果と合わなくてもよい）．

確認コマンド:

$ sort -t$'\t' -k3,3 -r hightemp.txt

date:2016/10/04
author:Fujita Soichiro
"""

import sys

def sort_3column():
	try:
		file = sys.argv[1]
	except:
		file = "hightemp.txt"

	with open(file) as f:
		texts = f.readlines()

	for i in sorted(texts,key = lambda line:line.split()[2],reverse =True):
		print i,

if __name__ == '__main__':
	sort_3column()

"""
lambda関数
lambda x:y
x=引数 y=返り値　の形で記述される

"""
