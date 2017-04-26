# 26. 強調マークアップの除去

import re

text = "あい[[ぬ！]]うえ[[ふふ|おかか]]きくこ"
t1 = "あい[[ぬ！]]うえ"
t2 = "え[[ふふ|おかか]]きくこ"

interlink_pat = re.compile("(.*?)\[{2}([^|]*?)\]{2}(.*?)")
interlink2_pat = re.compile("(.*?)\[{2}.*?\|(.*?)\]{2}(.*?)")
#interlink_pat = re.compile("(.*?)\[{2}.*?\|?(.*?)?\]{2}(.*?)")
text2 = re.sub(interlink_pat, r'\1\2\3', text)
text2 = re.sub(interlink2_pat, r'\1\2\3', text2)

