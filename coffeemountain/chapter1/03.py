sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = sent.replace(",","").replace(".","").split(" ")

word_count = []
for word in words:
    word_count.append(len(word))

print(word_count)