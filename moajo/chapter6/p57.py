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


def dep_to_dot(dep):
    body = ""
    for dep in dep:
        governor, dependent, label = dep.find('governor').text, dep.find('dependent').text, dep.get('type')
        body += '"{gov}" -- "{dep}" [label = "{label}"];\n'.format(gov=governor, dep=dependent, label=label)
    return """graph "g" {{
        node [fontname="arialuni.ttf", fontsize=10]
          edge [
            dir = forward,               //エッジの矢印を指定する
          ];
          {0}
        }}""".format(body)


def generate_graph(sentence, out):
    collapsed_dependencies = sentence.find('dependencies[@type="collapsed-dependencies"]')
    dot = dep_to_dot(collapsed_dependencies)
    with open('temp.dot', 'w', encoding="utf-8") as f:
        f.write(dot)

    os.system("dot -Kneato -Tjpg temp.dot -o " + out)


def main():
    with open("p56_parsed.xml", "r", encoding="utf-8") as f:
        s = f.read()
        xml = ET.fromstring(s)
        sentences = xml.find("document/sentences")
        sentence = sentences[4]
        generate_graph(sentence, "p57_test_3.jpeg")


if __name__ == "__main__":
    main()
