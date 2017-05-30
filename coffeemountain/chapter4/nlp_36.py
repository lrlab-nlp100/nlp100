from nlp_30 import *

all = mecab_map("neko.txt.mecab")

word_freq = {}
for sent in all:
    for keita_dict in sent:
        word_freq[keita_dict["surface"]] = word_freq.get(keita_dict["surface"], 0) + 1

sorted_word_freq = {k: v for k, v in sorted(word_freq.items(), key=lambda x: x[1], reverse=True)}

list = sorted_word_freq.items()

print(list[i][0] + " " + str(list[i][1]) for i in range(len(list)))
#print(sorted_word_freq[i].key() + " ") + sorted_word_freq[i].value() for i in range(len(sorted_word_freq)))