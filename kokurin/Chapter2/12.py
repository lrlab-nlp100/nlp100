import nltk
word1=''
word2=''


with open("hightemp.txt","r") as file,open('col1.txt','w') as f1,open('col2.txt', 'w') as f2:
    for line in file.readlines():
        words = nltk.word_tokenize(line)
        f1.write(words[0]+'\n')
        f2.write(words[1]+'\n')

with open('col1.txt','r') as f1,open('col2.txt', 'r') as f2:
    print ("col1\n",f1.read())
    print ("col2\n",f2.read())


'''
下面的代码快

with open("hightemp.txt") as f1, open("col1.txt","w") as f2, open("col1.txt","w") as f3:
    cols=list(zip(*[row.split("\t") for row in f1]))
    f2.write("\n".join(cols[0]))
    f3.write("\n".join(cols[1]))

'''