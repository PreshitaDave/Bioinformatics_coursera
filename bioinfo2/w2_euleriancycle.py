# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:31:33 2020

@author: Presh
"""
def EulerianCycle(adj):
    if len(adj) == 0:
        return
        
    curr_path = [0]
    circuit = []
    while curr_path:
        curr_v = curr_path[-1]
        if adj[curr_v]:
            next_v = adj[curr_v].pop()
            curr_path.append(next_v) 
        else:
            circuit.append(curr_path.pop())

#print output
    for i in range(len(circuit) - 1, -1, -1): 
        print(circuit[i], end = "")
        if i: 
            print(" -> ", end = "") 
        

#input as dict   
adj = []
with open('w2_eulerianpath.txt', 'r') as file:
    graph = dict((line.strip().split(' -> ') for line in file))
    for k,v in graph.items():
        k = int(k)
        adj.append(v.split(','))   
    
    for v in adj:
        for i in range(0, len(v)):
            v[i] = int(v[i])
            
#adj = [[] for i in range(len(graph.keys()))]      

EulerianCycle(adj)