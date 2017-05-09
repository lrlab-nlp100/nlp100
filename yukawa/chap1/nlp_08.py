# -*- coding: utf-8 -*-

def cipher(s):
    ret = ""
    for w in s[::1]:
        if w.isalpha() and w.islower():
            ret += chr(219 - ord(w))
        else:
            ret += w
    return ret

print(cipher("Hello,world-z!!"))
print(cipher(cipher("Hello,world-z!!")))
