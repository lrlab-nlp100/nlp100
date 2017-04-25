# 05. n-gram


def chara_ngram(text, n):
    results = []
    text = text.replace(' ', '')
    if len(text) >= n:
        for i in range(len(text)-n+1):
            results.append(text[i:i+n])
    return results


def word_ngram(text, n):
    results = []
    t = text.split()
    for i in range(len(t)):
        if i < len(t)-1:
            results.append([t[i], t[i+1]])
    return results


origin_text = "I am an NLPer"

print(chara_ngram(origin_text, 2))
print(word_ngram(origin_text, 2))
