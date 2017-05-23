import nltk

list=[]
with open('hightemp.txt', 'r') as f:
    for line in f:
        list.append(line.split('\t')[0])

rank=nltk.FreqDist(list)
print(rank.most_common())
