"""
WHAT YOU NEED TO DO IS 
USE POP INSTEAD OF lastPos
IN YOUR MINHEAP CODE.
"""



from Node import *
from Grid import *
from minheap import *

"""BONUS: Get user input for 
goal and current state"""

def main():
	grid = readGrid("grid.txt")

	print("Grid provided...")
	for row in grid:
		print(row)
	
	#start = [1,2]
	#goal = [2,5]
	print()
	print("PROVIDE ROW & COLUMN FOR START AND GOAL\n")
	start_row = input("row for start: ")
	start_col = input("column coordinate for start: ")
	print()
	goal_row = input("row coordinate for goal: ")
	goal_col = input("column coordinate for goal: ")
	print()

	algo = input("Which algorithm? (A* or greedy): ")

	s = [int(start_row), int(start_col)]
	g = [int(goal_row), int(goal_col)]

	print("Starting search, type: " + algo + " start: " + str(s) + " goal: " 
		+ str(g))

	path = informedSearch(grid, s, g)
	display_path = path[0]
	display_path.reverse()
	print("\nPATH")
	for i in display_path:
		print(i)
	print()
	print("Expanded: " + str(path[1]))
	print("Path Cost: " + str(path[2]))
	print()
	outputGrid(grid, s, g, path[0])

	print("Path written to file path.txt")

def informedSearch(grid, start, goal, search="A*"):
	dist = manhattanDist(start, goal)
	starting_node = Node(start, None, 0, dist)
	frontier = minheap()
	frontier.add(starting_node)
	visited = []
	expanded = 1
	path_cost = 0

	while True:

		current = frontier.remove()

		# DEBUG
		#print("Current Location: " + str(current.location))

		visited.append(current)

		# DEBUG
		#print("####VISITED####")
		#for el in visited:
		#	print(el.location)
		#print("###############")

		

		if current.location == goal:
			print("SUCCESS!")
			result = setPath(current)
			path_cost = len(result)
			return [setPath(current), expanded, path_cost]
		for node in expandNode(current, goal, grid, search):
			if(not inList(node, frontier.heap)
				and not inList(node, visited)):
				node.parent = current
				frontier.add(node)

		# DEBUG
		#print("----FRONTIER----")
		#for el in frontier.heap:
		#	print(el.location)
		#print("----------------")

		expanded+=1

		if frontier.isEmpty():
			print("FAILURE")
			return []

def getNeighbors(location, grid):
	neighbors = []
	
	# CHECK UP
	if(location[0]-1 > -1 and grid[location[0]-1][location[1]] != 0):
		neighbors.append([[location[0]-1, location[1]], grid[location[0]-1][location[1]]])

	# CHECK RIGHT
	if(location[1]+1 < len(grid[location[0]]) and grid[location[0]][location[1]+1] != 0):
		neighbors.append([[location[0], location[1]+1], grid[location[0]][location[1]+1]])

	# CHECK DOWN
	if(location[0]+1 < len(grid) and grid[location[0]+1][location[1]] != 0):
		neighbors.append([[location[0]+1, location[1]], grid[location[0]+1][location[1]]])

	# CHECK LEFT
	if(location[1]-1 > -1 and grid[location[0]][location[1]-1] != 0):
		neighbors.append([[location[0], location[1]-1], grid[location[0]][location[1]-1]])

	return neighbors

def expandNode(node, goal, grid, search):
	nodes = []
	neighbors = getNeighbors(node.location, grid)
	for pair in neighbors:
		dist = manhattanDist(pair[0], goal)
		if search == "A*":
			# Use step cost and manhattan distance
			nodes.append(Node(pair[0], node, pair[1], dist))
		if search == "greedy":
			# Set step cost to zero to not consider it
			# Now manhattan distance will only factor into
			# the decision
			nodes.append(Node(pair[0], node, 0, dist))
	return nodes

def setPath(current):
	path = [current.location]
	while(current.parent != None):
		path.append(current.parent.location)
		current = current.parent
	return path

def inList(node, nodes):
	for n in nodes:
		if(n.location[0] == node.location[0] 
			and n.location[1] == node.location[1]):
			return True
	return False

def manhattanDist(location, goal):
	return abs(location[0] - goal[0]) + abs(location[1] - goal[1])


if __name__ == "__main__":
	main();