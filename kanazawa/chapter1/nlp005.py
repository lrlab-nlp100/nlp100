#n-gram関数作成

def n_gram(seq, n):
    n_list = []
    last = len(seq)- n + 1
    for i in range(0, last):
        n_list.append(seq[i:i+n])
    return n_list

if __name__ == '__main__':
    char_seq = "I am NLPer"

    print("単語bi-gram")
    word_seq = char_seq.split()
    word_bi = n_gram(word_seq, 2)
    print(word_bi)

    print("文字bi-gram")
    char_bi = n_gram(char_seq, 2)
    print(char_bi)
