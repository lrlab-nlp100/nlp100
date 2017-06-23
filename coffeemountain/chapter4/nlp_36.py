from nlp_30 import *

all = mecab_map("neko.txt.mecab")


def word_freq(keita_list):
    word_freq = {}
    for sent in keita_list:
        for keita_dict in sent:
            word_freq[keita_dict["surface"]] = word_freq.get(keita_dict["surface"], 0) + 1

    return word_freq

if __name__ == "__main__":
    word_freq_dict = word_freq(all)
    for k, v in sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True):
        print("%s: %d" % (k, v))