import sys
from sys import argv
from heapq import heappush, heappop



def search(graph, s, goal, heuristic):
	# define variables for use
	fringe = []
	visit = {}
	previous = {}

	# using heap for mainitng a queue
	heappush(fringe,(0,s,None,0))
	# mark all visited and previous nodes False and None
	for nodes in graph:
		visit[nodes] = False
		previous[nodes] = None
		
	i = 1
	count=0
	temp=0
	c_node_h_val=0
	d_track=0

	while len(fringe) != 0:
		# sorting asc order
		l2 = []
		for k in fringe:
			l2.append(k[0])
			l2.sort()
			l4 = []
		for k in l2:
			for j in fringe:
				if(k == j[0]):
					l4.append(j)
		fringe = l4
		i = i+1 
		d_track= d_track+1
		count = count + 1
		# pop the least cost node from heap and analyse it
		total_cost, current_node, prev_node, link_cost = heappop(fringe)
		if visit[current_node] == False:
			visit[current_node] = True
			previous[current_node] = []
			previous[current_node].append(prev_node)
			previous[current_node].append(link_cost)
				
			# if goal return the total route and append final node traversal to it
			if current_node == goal:
				final = []
				while current_node != s:
					temp = []
					temp.append(current_node)
					for i in previous[current_node]:
						temp.append(i)
					final.append(temp)
					current_node = previous[current_node][0]
				final.reverse()
				d_track = d_track + 1
				# return total cost and final path
				return total_cost,count,final
			# else explore neighbours
			for neighbors, ncost in graph[current_node].items():
				# if heurisitic, then get into this if condition, so to add corresponding heurisitic value to its node, which can be later used for comparing and sorting into to asc order based on it. Also, if heurisitic then add the value else 0 will be passed to variable.

				if heuristic != "":
					for rec in heuristic:
						if((rec[0].find(current_node) != -1) & (d_track > 1)):
							c_node_h_val=rec[1]
						if(rec[0].find(neighbors)!=-1):
							temp=rec[1]
				this_link_cost = ncost
				# f(n) cost which will be used for comparison
				new_cost = total_cost + ncost + int(temp) - int(c_node_h_val)
				heappush(fringe, (new_cost, neighbors, current_node, ncost))
				
	# return none if no path found

	return count
	pass

def main():
	# checking arguments for processing
	flag=False
	filedata1=""
	try:
		filename=sys.argv[1]
		source=sys.argv[2]
		desti=sys.argv[3]
	except IndexError:
		print ('Insufficient argument')
		return
	# open file and make data ready for analysis
	try:
		hueristicfile=sys.argv[4]
		flag=True
		file = open(hueristicfile, 'r')
		filedata1 = file.readlines()
		# make a dictionary of graph
		filedata1 = [x.strip().split() for x in filedata1]
		if filedata1[-1:][0][0] == 'END':
			filedata1.pop()	
	except IndexError:
		pass
	
	file = open(filename, 'r')
	filedata = file.readlines()
	# make a dictionary of graph
	filedata = [x.strip().split() for x in filedata]
	if filedata[-1:][0][0] == 'END':
		filedata.pop()

	# empty graph
	graph = {}
	for rec in filedata:
		src = rec[0]
		dest = rec[1]
		cst = rec[2]
		if src not in graph:
			graph[src] = {}
		if dest not in graph:
			graph[dest] = {}
		# create src and dest nodes with its length from input file
		graph[src][dest] = int(cst)
		graph[dest][src] = int(cst)

	# call the search function
	result = search(graph,source,desti,filedata1)
	# print stmts
	n_expand = "nodes expanded: "
	distance = "distance: "
	if isinstance(result,int):
		print("%s%i"%(n_expand,result))
		print("distance: infinity")
		print("route: ")
		print("none")
	else:
		print("%s%i"%(n_expand,result[1]))
		print("%s%i km"%(distance,result[0]))
		print("route: ")
		for line in result[2]:
			print ("%s to %s, %s km" % (line[1],line[0],line[2]))
		print ("")

	pass

main()
