# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et
tree = et.parse('nlp.txt.xml')
root = tree.getroot()
collist = root.findall(".//*[@type='collapsed-dependencies']")
for col in collist:
    sublist = col.findall(".//*[@type='nsubj']")
    doblist = col.findall(".//*[@type='dobj']")
    for sub in sublist:
        for dob in doblist:
            if sub[0].attrib['idx'] == dob[0].attrib['idx']:
                print(sub[1].text+'\t'+sub[0].text+'\t'+dob[1].text)
