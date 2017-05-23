from nlp30 import load_mecab

morph_list = load_mecab("neko.txt.mecab")
for morph in morph_list:
    if morph["pos"] == "動詞":
        print(morph["surface"])
