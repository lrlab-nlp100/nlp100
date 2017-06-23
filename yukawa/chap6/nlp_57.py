# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et
import pydot
tree = et.parse('nlp.txt.xml')
root = tree.getroot()
collist = root.findall(".//*[@type='collapsed-dependencies']")
edge = []
for cnt,col in enumerate(collist):
    deplist = col.findall(".//dep")
    for dep in deplist:
        edge.append((dep[0].text,dep[1].text))
    g = pydot.graph_from_edges(edge,directed=True)
    g.write_jpeg('graph'+str(cnt)+'.jpg',prog='dot')
    edge = []
