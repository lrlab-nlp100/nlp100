from nlp_36 import *
import matplotlib.pyplot as plt
import numpy as np

word_freq_dict = word_freq(all)

sorted_word_dict = {k: v for k, v in sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)}


values = [value for value in sorted_word_dict.values()]
num_of_eachcount = []
"""
for i in range(values[0]):
    sum_count = 0
    for value in values:
        if i == value:
            sum_count += 1
    num_of_eachcount.append(sum_count)
"""

for i in range(50):
    sum_count = 0
    for value in values:
        if i == value:
            sum_count += 1
    num_of_eachcount.append(sum_count)

#left = np.array([x for x in range(values[0])])
left = np.array([x for x in range(50)])

height = np.array(num_of_eachcount)
plt.bar(left, height)
plt.show()
