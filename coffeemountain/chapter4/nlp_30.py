from functools import partial

open_with_utf8 = partial(open, encoding='utf8')

def mecab_map(input_file):
    all_list = []
    sent_list = []
    with open_with_utf8(input_file, "r") as f:
        for line in f:
            keitaiso_dict = {}
            factor1, factor2 = line.split("\t")
            factor2 = factor2.split(",")
            keitaiso_dict["surface"] = factor1
            keitaiso_dict["base"] = factor2[6]
            keitaiso_dict["pos"] = factor2[0]
            keitaiso_dict["pos1"] = factor2[1]
            sent_list.append(keitaiso_dict)
            
            if keitaiso_dict["surface"] == "。":
                all_list.append(sent_list)
                sent_list = []

    return all_list

if __name__ == "__main__":
    all_list = mecab_map("neko.txt.mecab")
    for sent in all_list:
        print(sent)