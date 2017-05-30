# -*- coding: utf-8 -*-
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def hoge(x, y, z):
    return str(x) + "時の" + str(y) + "は" + str(z)

print(hoge(12, "気温", 22.4))
