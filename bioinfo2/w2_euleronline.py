# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:50:02 2020

@author: Presh
"""

# Python3 program to print Eulerian circuit in given 
# directed graph using Hierholzer algorithm 
def printCircuit(adj): 

	# adj represents the adjacency list of 
	# the directed graph 
	
	if len(adj) == 0: 
		return # empty graph 

	# Maintain a stack to keep vertices 
	# We can start from any vertex, here we start with 0 
	curr_path = [0] 

	# list to store final circuit 
	circuit = [] 

	while curr_path: 

		curr_v = curr_path[-1] 
		
		# If there's remaining edge in adjacency list 
		# of the current vertex 
		if adj[curr_v]: 

			# Find and remove the next vertex that is 
			# adjacent to the current vertex 
			next_v = adj[curr_v].pop() 

			# Push the new vertex to the stack 
			curr_path.append(next_v) 

		# back-track to find remaining circuit 
		else: 
			# Remove the current vertex and 
			# put it in the curcuit 
			circuit.append(curr_path.pop()) 

	# we've got the circuit, now print it in reverse 
	for i in range(len(circuit) - 1, -1, -1): 
		print(circuit[i], end = "") 
		if i: 
			print(" -> ", end = "") 

# Driver Code 
if __name__ == "__main__": 

	# Input Graph 1 
#	adj1 = [[] for _ in range(3)] 

	# Build the edges 
#	adj1[0].append(1) 
#	adj1[1].append(2) 
#	adj1[2].append(0) 
#	printCircuit(adj1) 
#	print() 

	# Input Graph 2 
	adj2 = [[] for _ in range(7)] 

	adj2[0].append(1) 
	adj2[0].append(6) 
	adj2[1].append(2) 
	adj2[2].append(0) 
	adj2[2].append(3) 
	adj2[3].append(4) 
	adj2[4].append(2) 
	adj2[4].append(5) 
	adj2[5].append(0) 
	adj2[6].append(4) 
	printCircuit(adj2) 
	print() 
