from nlp30 import load_mecab

morph_list = load_mecab("neko.txt.mecab")
flag = 0
for morph in morph_list:
    if flag == 0 & morph["pos"] == "名詞":
        noun_phrase = morph["surface"]
        flag = 1
    if flag == 1 & morph["surface"] == "の":
        noun_phrase += "の"
        noun_phrase
