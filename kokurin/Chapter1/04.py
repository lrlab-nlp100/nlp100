import nltk

sent="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words=nltk.word_tokenize(sent)

l=len(words)
dict={}
x=[1, 5, 6, 7, 8, 9, 15, 16, 19]
for word in words:
    if words.index(word) + 1 in x:
        dict.setdefault(word[0],words.index(word)+1) #dict.setdefault的用法
    else:
        dict.setdefault(word[0:2], words.index(word)+1)


print(sorted(dict.items(),key=lambda d:d[1])) #dic数据类型按值进行排序并输出