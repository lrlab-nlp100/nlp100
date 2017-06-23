# -*- coding:utf-8 -*-

def mload():
    with open('neko.txt.mecab', 'r') as txt:
        sentence = []
        sentences = []
        for t in txt:
            if t == 'EOS\n':
                if len(sentence) > 0:
                    sentences.append(sentence)
                    sentence = []
            else:
                surface, feature = t.split('\t')
                feature = feature.split(',')
                dic = {
                    'surface' : surface,
                    'base' : feature[6],
                    'pos' : feature[0],
                    'pos1' : feature[1]
                }
                sentence.append(dic)
        return sentences

if __name__ == '__main__':
    ml = mload()
    for m in ml[0:3]:
        print(m) #確認用で3文出力
