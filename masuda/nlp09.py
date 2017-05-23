import random

def typoglycemia(str):
    words = str.split()
    ret = []
    for word in words:
        if len(word) > 4:
            mid = word[1:len(word)-1]
            w = word[0] + "".join(random.sample(mid, k=len(mid))) + word[-1]
            ret.append(w)
        else:
            ret.append(word)
    return " ".join(ret)


print(typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
