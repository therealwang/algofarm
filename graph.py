# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:20:21 2018

@author: yuwan
"""

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(dict)
        
    def addEdge(self, inp, out, weight = None, digraph = False):
        self.vertices.update([inp, out])
        self.edges[inp][out] = weight
        
        if not digraph:
            self.edges[out][inp] = weight
            
    def BFS(self, inp, out):
        if inp == out:
            return True
        
        q = deque(self.edges[inp])
        visited = set()
        
        while q:
            nextvert = q.popleft()
            visited.add(nextvert)
            if nextvert == out:
                return True
            q.extend([k for k in self.edges[nextvert] if k not in visited])
            
        return False
    
    def DFS(self, inp, out):
        if inp == out:
            return True
        
        q = deque(self.edges[inp])
        visited = set()
        
        while q:
            nextvert = q.pop()
            visited.add(nextvert)
            if nextvert == out:
                return True
            q.extend([k for k in self.edges[nextvert] if k not in visited])
            
        return False
