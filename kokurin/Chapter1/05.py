import nltk

sent='I am an NLPer'
words1=nltk.word_tokenize(sent)
words2=nltk.word_tokenize(sent)
words1.insert(0,'<s>')
words1.append('<\s>')

#単語のbigram

bi_words=list(nltk.bigrams(words1))
print(bi_words)

#文字のbigram

char=list(''.join(words2)) #将列表转为字符串再转为列表
char.insert(0,'<s>')
char.append('<\s>')
bi_char=list(nltk.bigrams(char))
print(bi_char)