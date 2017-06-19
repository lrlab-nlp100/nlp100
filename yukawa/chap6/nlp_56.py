# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et
tree = et.parse('nlp.txt.xml')
root = tree.getroot()
corelist = root.findall(".//coreference")
sentlist = root.find('.//sentences').findall(".//sentence")
repl = {}
for core in corelist:
    rep_men = core[0][4].text
    menlist = core.findall(".//mention")
    for men in menlist:
        if len(men.keys()) == 0:
            men_text = '['+rep_men+']('+men[4].text+')'
            sentence = men[0].text
            start = men[1].text
            repl.update({(sentence,start):men_text})
for sent in sentlist:
    tokenlist = sent.findall(".//token")
    for token in tokenlist:
        if (sent.attrib['id'],token.attrib['id']) in repl.keys():
            print(repl[(sent.attrib['id'],token.attrib['id'])]+' ',end='')
        else:
            print(token[0].text+' ',end='')
    print()
