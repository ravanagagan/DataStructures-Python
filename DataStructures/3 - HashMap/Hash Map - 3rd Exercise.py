#!/usr/bin/env python
# coding: utf-8

# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
# You have to read this file in python and print every word and its count as show below. 
# Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
    # EX :-
        # 'diverged': 2,
        # 'in': 3,
        # 'I': 8

frequency = {}
with open('poem.txt', 'r') as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:       
            token=token.replace('\n','')
            if token in frequency:
                frequency[token] += 1
            else:
                frequency[token] = 1

print(frequency)


# In[ ]:




