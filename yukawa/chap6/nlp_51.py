# -*- coding :utf-8 -*-
import sys
import re
txt = ''
for line in sys.stdin:
    txt += str(line)
txt = re.sub('\s','\n',txt)
txt = re.sub('\,|\?|\"','',txt)
txt = re.sub('\.','\n',txt)
print(txt)
