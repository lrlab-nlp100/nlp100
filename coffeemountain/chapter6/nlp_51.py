from nlp_51 import split_text_to_sentence

def text_tokenizer(input_file):
    sents = split_text_to_sentence(input_file)
    tokens_list = []
    for sent in sents:
        tokens = sent.split()
        tokens.append(" ")
        tokens_list.append(tokens)
    return tokens_list

if __name__ == '__main__':
    tokens_list = text_tokenizer('nlp.txt')
    for tokens in tokens_list:
        for token in tokens:
            print(token)