    #-*- coding:utf-8 -*-

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

count = []
words = s.split()
#print(words)

"""
for word in words:
    count.append(len(word) - word.count(',') - word.count('.'))
print(count)

pair = []#確認
pair = zip(words,count)
print(pair)
"""



#正規表現による置換
import re
print([len(re.sub('[.,]','',word)) for word in words])
