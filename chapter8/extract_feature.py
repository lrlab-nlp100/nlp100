# 72

import nltk
from stopword import is_stopword

stemmer = nltk.stem.SnowballStemmer('english')

def stemming(sentiments):
	ret = []
	for sent in sentiments:
		#ret.append(list(map(stemmer.stem, sent)))
		stemmed = []
		for w in sent:
			#ストップワード排除
			if is_stopword(w):
				continue
			#ステミング
			w = stemmer.stem(w)
			# !と?以外の1文字削除
			if w != '!' and w != '?' and len(w) <= 1:
				continue
			# 改行削除
			if w[-1::] == '\n':
				w = w[:-1:]
			stemmed.append(w)
		ret.append(stemmed)
	return ret

# def read_posneg(filename):
# 	with open(filename, 'rb') as f:
# 		pos = []
# 		neg = []
# 		for line in f:
# 			l = line.decode('utf-8', 'ignore').split(' ')
# 			if l[0] == '+1':
# 				pos.append(l)
# 			elif l[0] == '-1':
# 				neg.append(l)
# 			else:
# 				print('okasi')
# 		return pos, neg

def read_file(filename):
	with open(filename, 'rb') as f:
		ret = []
		for line in f:
			l = line.decode('utf-8', 'ignore').split(' ')
			ret.append(l)
		return ret


def write_file(file, filename):
	with open(filename, 'w') as f:
		for line in file:
			f.write(' '.join(line))
			f.write("\n")


if __name__ == '__main__':
	sentiments = read_file('sentiment.txt')
	stemmed = stemming(sentiments)
	write_file(stemmed, "sentiment_snow.txt")




