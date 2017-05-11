# -*- coding: utf-8 -*-

def cipher(s):
    ret = ""
    #ret = []
    for w in s[::1]:
        if w.isalpha() and w.islower():
            ret += chr(219 - ord(w))
            #ret.append(chr(219-ord(w)))
        else:
            ret += w
            #ret.append(w)
    return ret
    #return ''.join(ret)

print(cipher("Hello,world-z!!"))
print(cipher(cipher("Hello,world-z!!")))
