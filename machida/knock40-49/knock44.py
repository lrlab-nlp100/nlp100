# -*- coding: utf-8 -*-
import knock41
import pydot

sentences = knock41.sentences
def graph(sentence):
    edges = []
    for s in sentence:
        if s.srcs != -1:
            if s.rm_symbol_phrase() == '':
                continue
            pair = (s.rm_symbol_phrase(), sentence[s.srcs].rm_symbol_phrase())
            edges.append(pair)
    g=pydot.graph_from_edges(edges, directed=True)
    g.write_jpeg('knock44.jpg', prog='dot')

graph(sentence=sentences[4])
