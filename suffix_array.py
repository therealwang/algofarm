# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:53:10 2018

@author: yuwan

O(n log^2 n) implementation of a suffix array (good for 1e5 strings)

last row of suffixArray(word) gives the appropriately ordered suffix array
"""


from itertools import izip_longest

def findordering(l):
    ordering = {v: i for i, v in enumerate(sorted(set(l)))}
    return [ordering[ch] for ch in l]
    
def suffixArray(word):
    n = len(word)
    curr = findordering(word)
    out = [curr]
    k = 1
    while k < n:
        curr = findordering(list(izip_longest(curr, curr[k:], fillvalue = -1)))
        out.append(curr)
        k <<= 1
    return out
        
        
    
def LCP(word, index1, index2):
    #longest common prefix of 2 suffixes of a word
    arr = suffixArray(word)
    out = 0
    n = len(word)
    if index1 == index2:
        return n - index1
    curr1 = index1
    curr2 = index2
    for k in range(len(arr)-1, -1, -1):
        if curr1 >= n or curr2 >= n:
            return out
        if arr[k][curr1] == arr[k][curr2]:
            out += 1 << k
            curr1 += 1<< k
            curr2 += 1<<k
    return out