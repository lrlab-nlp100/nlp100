from nlp_30 import *

all = mecab_map("neko.txt.mecab")

for sent in all:
    for keita_dict in sent:
        if keita_dict["pos"] == "動詞":
            print(keita_dict["base"])

