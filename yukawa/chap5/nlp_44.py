# -*- coding: utf-8 -*-
import pydot
import nlp_41
import CaboCha
import re
from collections import defaultdict
s = input('')
c = CaboCha.Parser()
tree = c.parse(s)
res = tree.toString(CaboCha.FORMAT_LATTICE)
l = []
lm = []
ch = []
d = defaultdict(list)
f = res.split('\n')
for line in f:
    word = re.split(r'\,|\t|\s',line)
    if len(word) == 10 or len(word) == 8:
    	lm.append(nlp_41.nlp_40.Morph(word[0],word[7],word[1],word[2]))
    elif len(word) == 5:
        d[int(word[2][:-1])].append(int(word[1]))
        ch.append(nlp_41.Chunk(int(word[2][:-1]),d[int(word[1])]))
        if len(lm) != 0:
            ch[-2].set(lm)
            lm = []
    elif word[0] == 'EOS':
    	if len(lm) != 0:
            ch[-1].set(lm)
            lm = []
            l.append(ch)
            ch = []
            d = defaultdict(list)
edge = []
for s in l:
    for c in s:
        if c.dst != -1:
            edge.append((c.mtoc(c),c.mtoc(s[c.dst])))
g = pydot.graph_from_edges(edge,directed=True)
g.write_jpeg('graph.jpg',prog='dot')
