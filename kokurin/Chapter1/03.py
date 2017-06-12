import nltk

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words=nltk.word_tokenize(str)
pi=[]
for word in words:
    pi.append(len(word))

print(pi)