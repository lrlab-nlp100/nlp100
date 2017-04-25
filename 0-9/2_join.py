# coding: UTF-8
# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」

str1 = 'パトカー'
str2 = 'タクシー'

print(''.join([a + b for a, b in zip(str1, str2)]))
