from nlp_30 import *

all = mecab_map("neko.txt.mecab")

for sent in all:
    for i in range(len(sent)):
        if sent[i-2]["pos"] == "名詞" and sent[i]["pos"] == "名詞" and sent[i-1]["surface"] == "の":
            print(sent[i-2]["surface"]+sent[i-1]["surface"]+sent[i]["surface"])