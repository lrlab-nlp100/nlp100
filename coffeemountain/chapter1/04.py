sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = sent.replace(".","").split(" ")

single = [0, 4, 5, 6, 7, 8, 14, 15, 18]

word_dict = {}
for i in range(len(words)):
    if i in single:
        word_dict[words[i][:2]] = words[i]
    else:
        word_dict[words[i][:1]] = words[i]

print(word_dict)