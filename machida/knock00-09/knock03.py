# -*- coding: utf-8 -*-

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

res = []
for s in str.split(" "):
    s = s.replace(",", "").replace(".", "")
    res.append(len(s))

print(res)
