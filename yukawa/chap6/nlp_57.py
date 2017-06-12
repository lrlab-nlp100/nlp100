# -*- coding: utf-8 -*-
import re
import pydot
pa = re.compile(r'collapsed-dependencies')
pa_go = re.compile(r'<governor idx=(.+?)>(.+?)</governor>')
pa_de = re.compile(r'<dependent idx=(.+?)>(.+?)</dependent>')
cnt = 0
edge = set()
with open('nlp.txt.xml','r') as f:
    for line in f:
        if pa.search(line) is not None:
        	cnt += 1
        	g = pydot.graph_from_edges(edge,directed=True)
        	g.write_jpeg('graph'+str(cnt)+'.jpg',prog='dot')
        	edge = set()
        go = pa_go.search(line)
        if go is not None:
        	a = go.group(2)
        de = pa_de.search(line)
        if de is not None:
        	b = de.group(2)
        	edge.add((a,b))
