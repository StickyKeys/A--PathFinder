class Node:
	def __init__(self, location, parent, fromNode, toGoal):
		self.location = location
		self.parent = parent
		self.fromNode = fromNode
		# USING MANHATTAN DISTANCE
		self.toGoal = toGoal
		self.totalCost = self.fromNode + self.toGoal

	def setFromNode(value):
		self.fromNode = value
		self.totalCost = self.fromNode + self.toGoal
	
	def setToGoal(value):
		self.toGoal = value
		self.totalCost = self.fromNode + self.toGoal
