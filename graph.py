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
        
    ### Initializing ###
        
    def addEdge(self, inp, out, weight = None, digraph = False):
        self.vertices.update([inp, out])
        self.edges[inp][out] = weight
        
        if not digraph:
            self.edges[out][inp] = weight
            
    def addEdgeSet(self, d):
        self.vertices.update(d.keys())
        for k in d:
            self.edges[k].update(d[k])          
            self.vertices.update(d[k].keys())
            
            
    ### Searching ###
            
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
    
    ### Properties ###
    
    def alledges(self):
        edges = set()
        
        for i in self.edges:
            for j in self.edges[i]:
                edges.add((i,j,self.edges[i][j]))
                
        return edges



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
                
        
        
def floydwarshall(graph):
    out = {i: {o: np.inf for o in graph.vertices} for i in graph.vertices}
    
    edges = graph.alledges()
    
    for i, j, d in edges:
        out[i][j] = d
        
    for i in graph.vertices:
        out[i][i] = 0
        
    for k in graph.vertices:
        for i in graph.vertices:
            for j in graph.vertices:
                if out[i][j] > out[i][k] + out[k][j]:
                    out[i][j] = out[i][k] + out[k][j]
    
    return out
        
    
def bellmanford(g, source):
    dist = defaultdict(lambda:np.inf)
    pred = defaultdict(lambda:None)
    
    dist[source] = 0
    
    edges = g.alledges()
    
    for i in range(len(g.vertices)):
        for i, o, d in edges:
            if dist[i] + d < dist[o]:
                dist[o] = dist[i] + d
                pred[o] = i
            
    return dist
        
        
        