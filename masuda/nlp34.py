from nlp30 import load_mecab

morph_list = load_mecab("neko.txt.mecab")
for morph in morph_list:
    if morph["pos1"] == "サ変接続":
        print(morph["surface"])
