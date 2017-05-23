import nltk
import random

random_sent=''

sent="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words=nltk.word_tokenize(sent)

for word in words:
    if len(word)<4:
        random_sent +=' '+word

    else:
        word1=word[1:-1]
        word2=list(word1)
        random.shuffle(word2)
        word1=''.join(word2)
        word=word.replace(word[1:-1],word1)#replace的具体用法
        random_sent += ' ' + word

print (random_sent)