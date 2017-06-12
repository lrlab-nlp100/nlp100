import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
from nlp_36 import *

fp = FontProperties(fname='C://Users\//USER//Desktop//ipag.ttf')
"""
word_freq_dict = word_freq(all)
sorted_word_dict = {k: v for k, v in sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)}
i

values_top = []
keys_top = []

for i in range(10):
    values_top.append(values[i])
    keys_top.append(keys[i])


fig = plt.figure()
left = [1,2,3,4,5,6,7,8,9,10]
height = np.array(values_top)
#plt.bar(left, height, tick_label=values_top, align="center", FontProperties=fp)
plt.plot(left, height, FontProperties=fp)
plt.show()
"""

fig = plt.figure()

