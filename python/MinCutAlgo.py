from sys import argv
import random
import copy

#select a random edge from adjacency list given as hash map
def randomEdge(graph_map) :
	vertex1 = graph_map.keys()[random.randint(0, len(graph_map)-1)]
	vertex2 = graph_map[vertex1][random.randint(0, len(graph_map[vertex1])-1)]
	return vertex1, vertex2

#min cut algorithm based on Krager's algorithm
def min_cut(graph_map):

	while len(graph_map) > 2 :
		vertex1, vertex2 = randomEdge(graph_map)

		#add list of vertex2 to vertex1
		graph_map[vertex1].extend(graph_map[vertex2])

		temp = []
		#remove vertex2 entry from hash map
		for entry in graph_map[vertex2] :
			temp = graph_map[entry]

			for i in range(0, len(temp)) :
				if temp[i] == vertex2 :
					temp[i] = vertex1
			graph_map[entry] = 	temp	

		#remove self loops
		while vertex1 in graph_map[vertex1] :
			graph_map[vertex1].remove(vertex1)

		#delete entry for second vertex	from hash map
		del graph_map[vertex2]
	#checks commented	
	#if len(graph_map[graph_map.keys()[1]]) < 5 :
	#	print graph_map[graph_map.keys()[0]]
	return len(graph_map[graph_map.keys()[1]])

# read from file		
script, filename = argv
graph_map = { }
for line in open(filename,'r').readlines():	
	inputstr = []
	inputstr = line.split()
	x = inputstr.pop(0)
	graph_map[x] = inputstr

#print graph_map

#min cut print
minimum_cut_value =  min_cut(copy.deepcopy(graph_map)) 
#looping for sample
for i in range(1, 100) : 	
	x = min_cut(copy.deepcopy(graph_map))	
	if x < minimum_cut_value :
		minimum_cut_value = x

print minimum_cut_value
