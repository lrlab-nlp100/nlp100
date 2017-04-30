#! /usr/bin/env python
import os
import re
from typing import List
from stemming.porter2 import stem
import pprint
import json
import corenlp
import re
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from chapter3.common import get_brace


def parse_s_formula(s: str):
    content = s.strip()[1:-1]
    items = []
    while content != "":
        if content[0] != "(":
            index = content.find(" ")
            if index == -1:
                items.append(content)
                break
            item = content[:index]
            items.append(item)
            content = content[index:].strip()
        else:
            n = get_brace(content, 0, begin="(", end=")")
            items.append(parse_s_formula(n))
            content = content[len(n):].strip()
    return items

def print_np(parsed_s):
    for i,elem in enumerate(parsed_s):
        if isinstance(elem,str):
            if elem =="NP":
                print(s_to_str(parsed_s[i:]))
        else:
            print_np(elem)
def s_to_str(parsed):
    buf=[]
    for elem in parsed[1:]:
        if isinstance(elem,str):
            buf.append(elem)
        else:
            buf.append(s_to_str(elem))
    return " ".join(buf)


def main():
    with open("p56_parsed.xml", "r", encoding="utf-8") as f:
        s = f.read()
        xml = ET.fromstring(s)
        sentences = xml.find("document/sentences")
        for sentence in sentences[:4]:
            parse = sentence.find('parse')
            parsed = parse_s_formula(parse.text)
            print_np(parsed)
            print("----------")
            # print(parsed)



if __name__ == "__main__":
    main()
