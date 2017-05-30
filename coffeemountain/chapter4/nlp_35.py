from nlp_30 import *

all = mecab_map("neko.txt.mecab")

for sent in all:
    meishis = []
    for i in range(len(sent)):
        if sent[i]["pos"] == "名詞":
            meishis.append(sent[i]["surface"])

        elif sent[i-2]["pos"] == "名詞" and sent[i-1]["pos"] == "名詞":
            #print(sent[i]["pos"])
            #print(meishi)
            print("".join(meishi for meishi in meishis))

        else:
            meishis = []