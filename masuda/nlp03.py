import re
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = re.split(' |,|\.', str)
# print(words)
lengths = []
for word in words:
    if len(word) != 0:
        lengths.append(len(word))
print(lengths)
