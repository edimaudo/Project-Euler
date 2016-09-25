# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 13:39:17 2016

@author: edima
"""

# turn the string of words into a list of python strings
with open('p042_words.txt','r') as f:
    words = f.read().split(',')
    words = [list(word.strip('\"')) for word in words]
    f.close()
 
# we should have an idea of how long the longest word is,
# giving us an idea of the magnitude of the triangle words
m = max([len(word) for word in words])
# form triangle numbers up to the given range
triangles = [n*(n + 1)/2 for n in range(1,2*m)]
 
# make a dictionary map for character values
vals = {}
s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for c in s:
    vals[c] = s.index(c) + 1
 
# count triangle words
triangle_words = 0
for word in words:
    if sum([vals[c] for c in word]) in triangles:
        triangle_words += 1
        
print(triangle_words)