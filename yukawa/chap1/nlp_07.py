# -*- coding: utf-8 -*-

def sent(x,y,z):
    s = ""
    s += str(x)
    s += "時の"
    s += str(y)
    s += "は"
    s += str(z)
    return s

s = sent(12,"気温",22.4)
print(s)

