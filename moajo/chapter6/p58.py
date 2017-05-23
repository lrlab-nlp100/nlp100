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


def extract_target_dep(dep):
    dict = {}
    for dep in dep:
        t = dep.get('type')
        governor = dep.find('governor')
        dependent = dep.find('dependent')
        p_id = governor.get("idx")
        if t == "nsubj":  # 主語関係
            if p_id not in dict:
                dict[p_id] = [governor.text, (dependent.get("idx"), dependent.text), None]
            else:
                dict[p_id][1] = (dependent.get("idx"), dependent.text)
        if t == "dobj":  # 述語関係
            if p_id not in dict:
                dict[p_id] = [governor.text, None, (dependent.get("idx"), dependent.text)]
            else:
                dict[p_id][2] = (dependent.get("idx"), dependent.text)
    for v in filter(lambda v: v[1][1] is not None and v[1][2] is not None, dict.items()):
        print("{0}\t{1}\t{2}".format(v[1][1][1], v[1][0], v[1][2][1]))


def main():
    with open("p56_parsed.xml", "r", encoding="utf-8") as f:
        s = f.read()
        xml = ET.fromstring(s)
        sentences = xml.find("document/sentences")
        for sentence in sentences:
            collapsed_dependencies = sentence.find('dependencies[@type="collapsed-dependencies"]')
            extract_target_dep(collapsed_dependencies)


if __name__ == "__main__":
    main()
