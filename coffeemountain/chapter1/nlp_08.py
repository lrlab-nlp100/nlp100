def cipher(sent):
    return "".join(chr(219 - ord(str)) if str.islower() else str  for str in sent)


sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(cipher(sent))

print(cipher(cipher(sent)))