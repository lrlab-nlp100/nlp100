#連想配列
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

s = s.replace('.','')
words = s.split()
#print(words)
words_index = {}#dict型

for i, word in enumerate(words):
    n = i + 1
    l = 1 if n in[1,5,6,7,8,9,15,16,19] else 2
    words_index[word[:l]] = n #辞書オブジェクト[キー] = オブジェクト

print(words_index)
