# -*- coding: utf-8 -*-
import re
pa = re.compile(r'<mention representative=\"true\">')
pa_co = re.compile(r'<coreference>')
with open('nlp.txt.xml','r') as f:
    for line in f:

