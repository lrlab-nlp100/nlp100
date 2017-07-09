# 72

from nltk.stem.porter import PorterStemmer
from stopword import is_stopword

stemmer = PorterStemmer()

def stemming(sentiments):
	ret = []
	for sent in sentiments:
		ret.append(list(map(stemmer.stem, sent)))
		#for w in sent:
			#w = stemmer.stem(w)
			#if not is_stopword(w):
			#sent.append(w)
	return ret

def read_posneg(filename):
	with open(filename, 'rb') as f:
		pos = []
		neg = []
		for line in f:
			l = line.decode('utf-8', 'ignore').split(' ')
			if l[0] == '+1':
				pos.append(l)
			elif l[0] == '-1':
				neg.append(l)
			else:
				print('okasi')
		return pos, neg

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


if __name__ == '__main__':
	sentiments = read_file('sentiment.txt')
	stemmed = stemming(sentiments)
	write_file(stemmed, "sentiment2.txt")