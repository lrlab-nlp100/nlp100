sent = "I am an NLPer"


def make_ngram(n, input):
    n_gram = []
    for i in range(len(input)-n+1):
        n_gram.append(input[i:i+n])
    
    return n_gram

print(make_ngram(2, sent))
