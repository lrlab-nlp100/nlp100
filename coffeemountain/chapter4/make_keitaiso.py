from janome.tokenizer import Tokenizer
from functools import partial

open_with_utf8 = partial(open, encoding='utf8')

t = Tokenizer()
g = open_with_utf8("neko.txt.mecab", "w")
def get_tokens(input_file):
    with open_with_utf8(input_file, "r") as f:
        for line in f:
            tokens = t.tokenize(line)
            for token in tokens:
                g.write('{}\n'.format(token))


        return tokens_list

            

print(get_tokens("neko.txt"))

if __name__ == "main":
    get_tokens("neko.txt")