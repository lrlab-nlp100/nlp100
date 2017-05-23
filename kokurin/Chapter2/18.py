
import nltk

sent=[]
dict={}
with open('hightemp.txt', 'r') as f:
    for line in f:
        sent=nltk.word_tokenize(line)
        sent=sorted(sent)
        print(sent)
        sent=[]

