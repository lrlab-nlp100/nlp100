# coding: utf-8
u"""
自然言語処理100本ノック

19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

各行の1列目の文字列の出現頻度を求め，
その高い順に並べて表示せよ．

確認にはcut, uniq, sortコマンドを用いよ．


確認コマンド:

$ cut -f 1 hightemp.txt | sort | uniq -c |sort -r

date:2016/10/04
author:Fujita Soichiro
"""

import sys

def freq_str():
	try:
		file = sys.argv[1]
	except:
		file = "hightemp.txt"

	with open(file) as f:
		texts = f.readlines()
	dict = {}
	for i in texts:
		i = i.split('\t')
		if dict.has_key(i[0]):
			dict[i[0]] += 1
		else:
			dict[i[0]] = 1
	for j,k in sorted(dict.items(),key =lambda x:x[1],reverse = True):		#google先生は神
		print j,'\t',dict[j]

if __name__ == '__main__':
	freq_str()


"""
dictをvalueでソートする際は、
dict.items()でitemのリストをソートすればいい。
"""




