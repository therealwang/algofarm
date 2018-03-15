# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:30:28 2018

@author: yuwan
"""

from collections import defaultdict, deque

class AhoCorasick:
    def __init__(self):
        self.transitions = defaultdict(lambda: len(self.transitions) + 1)
        self.chars = defaultdict(set)
        self.failure = defaultdict(lambda: 0)
        self.outputs = defaultdict(set)
        
    def addWord(self, word):
        state = 0
        
        for char in word:
            self.chars[state].add(char)
            state = self.transitions[state,char]
            
        self.outputs[state].add(word)
        
    def addFailures(self):
        q = deque(self.transitions[0, char] for char in self.chars[0])