import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

# determine count of each item in a dictionary and draw a histogram chart

# fname = input("Enter file name: ")
fname = "test.txt"
fhandle = open(fname)

wordDict = dict() # create dictionary for using as the histogram data

for line in fhandle:
    words = line.split() # get each line of text and split it into a list
    for word in words:
        wordDict[word] = wordDict.get(word,0) + 1   # increase word count or add new word to dictionary using .get() method

print(wordDict.items())

x = wordDict.keys()
y = wordDict.values()

ax = plt.axes()
ax.set_xticklabels(wordDict.keys())
plt.xticks(rotation=90)

plt.bar(wordDict.keys(), wordDict.values(), color='b')
plt.show()
