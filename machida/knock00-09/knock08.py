# -*- coding: utf-8 -*-

def cipher(str):
    code = ""
    for s in str:
        if s.islower():
            code += chr(219-ord(s))
        else:
            code += s
    return code

str = "Tom is cool GUY."
ci = cipher(str)

print(ci)
print(cipher(ci))
