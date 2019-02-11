Name: Kailash Shankar Bhanushali
UTA ID: 1001398090
Programming Language: Python
Code Run Steps: 
	1. store input.txt, find_route.py, h_kassel.txt file in the same directory
	2. change directory using cd command where file is located
		ex: to access directory /home/k/ks/ksb8090/public_html/ai1/ass1, enter $cd /home/k/ks/ksb8090/public_html/ai1/ass1
	3. now run code using python (find_route.py works for both informed as well as uninformed search algorithm)
	4. To run the code, write:
		a. Uninformed Search: $python filename.py inputfile.txt source_node destination_node
			ex. $python find_route.py input.txt Bremen Kassel
		b. Informed Search: $python filename.py inputfile.txt source_node destination_node heurisiticfile.txt
			ex. $python find_route.py input.txt Bremen Kassel h_kassel.txt
	5. output is generated and you are good to go.
Code Structure:
	1. Called the main function
	2. using system argv, fetch the input from the command line and stored in the variable
	3. took the fourth argument (h_kassel.txt) within try catch block, as I am not aware, whether run command will be informed, if it will be uninformed, then it will throw error, so to avoid, it's written within try catch block.
	4. input file data is split and stored in matrix and passed to search funtion for results
	5. using heappush, enter the root node first with heuristic as zero and distance also as zero
	6. intialize visited_nodes and prev_nodes to false and none respectively
	7. now start the while loop until nodesQ(fringe) is empty
	8. extract the first node with segregating totalcost, currentnode, prevnode, linkcost to its specific variable
	9. now check whether current node is in visited list, if not, then add to visitednode, and append to prevnode also
	10. check further is the current node goal node?, if yes then add current node to list and reverse it to get the path, then return cost, count and final variable. so that we can use that to print the output as expected.
	11. If it's not goal node, then using .items(), explore neighbor node and store its cost in link cost, then newcost variable is used to add current neighbor cost with total cost, now here's a catch, if heuristic is not empty, then its informed, so, keep a track of dtrack, to check whether it's first element or not, if not then add to cnodehval and also if neighbor value which is in access right now in loop, is found in rec then store value of heuristic in temp, and which will be used in addition with g(n) as newcost.
	12. This way while loop will work unless currentnode equals goal node and value as told, will be returned and printed as expected output.
