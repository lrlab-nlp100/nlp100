def load_mecab(mecab_file_name):
    import re

    with open(mecab_file_name, encoding="utf-8") as f:
        morph_list = []
        reg = re.compile(r"[\t,]")
        for line in f:
            if "EOS" in line:
                continue
            else:
                morph = reg.split(line)
                morph_dic = ({"surface":morph[0],
                              "base":morph[7],
                              "pos":morph[1],
                              "pos1":morph[2]})
                morph_list.append(morph_dic)

        return morph_list

if __name__ == "__main__":
    load_mecab("neko.txt.mecab")
    print("load success")
