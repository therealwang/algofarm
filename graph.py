# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:20:21 2018

@author: yuwan
"""

from collections import defaultdict, deque
import numpy as np

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



def dijkstra(graph, start, end):
    if start not in graph.vertices or end not in graph.vertices:
        return -1
    
    unvisited = set()
    unvisited |= graph.vertices
    
    shortestpath = {v: np.inf if v != start else 0 for v in graph.vertices}
    
    while unvisited:
        temp = {k: v for k, v in shortestpath.items() if k in unvisited}
        nextvert = min(temp, key = temp.get)
        if shortestpath[nextvert] == np.inf:
            return -1
        elif nextvert == end:
            return shortestpath[end]
        
        unvisited.remove(nextvert)
        
        for neighbor in graph.edges[nextvert]:
            templen = graph.edges[nextvert][neighbor] + shortestpath[nextvert]
            if templen < shortestpath[neighbor]:
                shortestpath[neighbor] = templen
                
        
                
        
        