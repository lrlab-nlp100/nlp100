def n_gram(n, seq):
    nGram = []
    for i in range(len(seq)):
        if i+n <= len(seq):
            nGram.append(seq[i:i+n])
    return nGram

if __name__ == "__main__":
    str = "I am an NLPer"
    print(n_gram(2, str.split()))
    print(n_gram(2, str))
