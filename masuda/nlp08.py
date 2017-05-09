import re

def cipher(str):
    ret = []
    for char in str:
        if re.match(r'[a-z]', char):
            ret.append(chr(219-ord(char)))
        else:
            ret.append(char)

    return "".join(ret)


str = "abcdefg"
str = cipher(str)
print(str)
str = cipher(str)
print(str)
