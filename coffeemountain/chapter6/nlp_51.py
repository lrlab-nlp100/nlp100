def split_text_to_sentence(input_file):
    with open(input_file, encoding='utf-8') as text:
        sentences = []
        deliminators = ['.', ';', ':', '?', '!']
        for line in text:
            if line != '\n':
                split_num = 0
                for i in range(len(line)):
                    if line[i] in deliminators and line[i+1] == ' ' and line[i+2].isupper():
                            sentences.append(line[split_num:i+1])
                            split_num = i+2
                
                sentences.append(line[split_num:-1])
    return sentences


if __name__ == '__main__':
    nlp_sentences = split_text_to_sentence('nlp.txt')
    for sent in nlp_sentences:
        print(sent)