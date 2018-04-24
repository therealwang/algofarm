# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:30:28 2018

@author: yuwan
"""

'''
AhoCorasick algorithm for finding words in a given text.

output prints the index at which any word ends in a given text

Sample usage:
a = AhoCorasick()
a.createAlgo(['hi','bye','hihi'])
a.search('hi my name is hihi wow byehihihi')

out:
1: set(['hi'])
15: set(['hi'])
17: set(['hi', 'hihi'])
25: set(['bye'])
27: set(['hi'])
29: set(['hi', 'hihi'])
31: set(['hi', 'hihi'])
'''
from collections import defaultdict, deque

class AhoCorasick:
    def __init__(self):
        self.transitions = defaultdict(lambda: len(self.transitions) + 1)
        self.chars = defaultdict(set)
        self.failure = defaultdict(lambda: 0)
        self.outputs = defaultdict(set)
        
    def createAlgo(self, wordlist):
        if type(wordlist) != list:
            return
        else:
            for word in wordlist:
                self.addWord(word)
            self.addFailures()
        
    def addWord(self, word):
        state = 0
        
        for char in word:
            self.chars[state].add(char)
            state = self.transitions[state,char]
            
        self.outputs[state].add(word)
        
    def addFailures(self):
        q = deque(self.transitions[0, char] for char in self.chars[0])
        
        while q:
            state = q.popleft()
            
            for char in self.chars[state]:
                failstate = self.failure[state]
                while failstate and (failstate, char) not in self.transitions:
                    failstate = self.failure[failstate]
                
                    
                nextstate = self.transitions[state, char]
                
                self.failure[nextstate] = self.transitions[failstate, char] if \
                            (failstate, char) in self.transitions else 0
                self.outputs[nextstate].update(self.outputs[self.failure[nextstate]])
                
                q.append(nextstate)
                
        
    def search(self, text):
        state = 0
        
        for i, char in zip(range(len(text)), text):
            while state and (state, char) not in self.transitions:
                state = self.failure[state]
            state = self.transitions[state, char] if (state, char) in self.transitions else 0
            if self.outputs[state]:
                print '{}: {}'.format(i, self.outputs[state])
