import nltk
word_url=[]

with open("hightemp.txt","r") as file:
    for line in file.readlines():
        word = nltk.word_tokenize(line)
        word_url.append(str(word[0]).replace('\n',' '))

    word_url=set(word_url)
    print(word_url)