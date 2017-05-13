import random


def shuffle_word(word):
    mid_word = word[1:-1]
    if len(word) >= 4:
        return word[0] + "".join(random.sample(mid_word, len(mid_word))) + word[-1]
    else:
        return word

def shuffle_sent(sent):
    words = sent.split(" ")
    shuffle_words = []

    for word in words:
        shuffle_words.append(shuffle_word(word))

    return " ".join(word for word in shuffle_words)

print(shuffle_sent("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))