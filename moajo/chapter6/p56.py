#! /usr/bin/env python

import re
from typing import List
from stemming.porter2 import stem
import pprint
import json
import corenlp
import re
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


# see http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
# list of tagging of part of speech

def get_sentences(sentences):
    list_ = []
    for sentence in sentences.findall('sentence'):
        list_.append([word.text for word in sentence.findall('tokens/token/word')])
    return list_

def show_mention(mention,sentences):
    sentence_i = int(mention.find('sentence').text) - 1
    start_i = int(mention.find('start').text) - 1
    end_i = int(mention.find('end').text) - 1
    s = sentences[sentence_i]
    return " ".join(s[start_i:end_i])

def main():
    with open("p56_parsed.xml", "r", encoding="utf-8") as f:
        s = f.read()
        xml = ET.fromstring(s)
        sentences = get_sentences(xml.find("document/sentences"))
        coreferences = xml.find("document/coreference")
        for coref in coreferences.findall('coreference'):
            mentions = coref.findall('mention')
            represent = coref.find('mention[@representative="true"]')
            ss = show_mention(represent,sentences)
            # print("represent: "+ss)
            for mention in mentions:
                if mention != represent:
                    sentence_i = int(mention.find('sentence').text) - 1
                    start_i = int(mention.find('start').text) - 1
                    end_i = int(mention.find('end').text) - 2
                    sss = show_mention(mention,sentences)
                    # print("mention: "+sss)

                    target_sentence = sentences[sentence_i]
                    target_sentence[start_i] = ss.strip() + ' (' + target_sentence[start_i]
                    target_sentence[end_i] = target_sentence[end_i] + ')'
        for s in sentences:
            print(" ".join(s))

if __name__ == "__main__":
    main()
