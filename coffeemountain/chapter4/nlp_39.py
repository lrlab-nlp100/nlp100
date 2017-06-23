from nlp_36 import *
import matplotlib.pyplot as plt
import numpy as np

word_freq_dict = word_freq(all)

sorted_word_dict = {k: v for k, v in sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)}


values = [value for value in sorted_word_dict.values()]
num_of_eachcount = []

for i in range(values[0]):
    sum_count = 0
    for value in values:
        if i == value:
            sum_count += 1
    num_of_eachcount.append([i, sum_count])

sorted_num_of_eachcount = sorted(num_of_eachcount, key=lambda x:x[1], reverse=True)

left = np.array([x for x in range(values[0])])
height = np.array(sorted_num_of_eachcount)

plt.plot(left, height)
plt.yscale('log')
plt.xscale('log')

plt.show()