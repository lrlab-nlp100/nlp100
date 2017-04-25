# 08. 暗号文


def cipher(str):
    lst = list(str)
    for i, s in enumerate(lst):
        if s.islower():
            lst[i] = chr(219 - ord(s))
    return ''.join(lst)


a = cipher('dRagogon-one')
b = cipher(a)
print(a)
print(b)
