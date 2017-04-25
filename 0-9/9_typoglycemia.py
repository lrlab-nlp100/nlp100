# 09. Typoglycemia
import random


def typoglycemia(str):
    lst = str.split()
    for i, s in enumerate(lst):
        if len(s) <= 4:
            continue
        word = [s[0:1]]
        word.extend(random.sample(list(s[1:-1]), len(s)-2))
        word.append(s[-1:])
        lst[i] = ''.join(word)
    return ' '.join(lst)

org_text = "I couldn't believe that" \
      " I could actually understand" \
      " what I was reading : the phenomenal" \
      " power of the human mind ."

print(typoglycemia(org_text))

