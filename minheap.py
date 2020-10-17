# WORKS SPECIFICALLY FOR INFORMED SEARCH NODES
import math

class minheap:

	def __init__(self):
		self.heap = []
		self.next = None
		self.root = None

	def getChildren(self, position):
		leftChild = (2 * position) + 1
		rightChild = (2 * position) + 2
		return [leftChild, rightChild]

	def getParent(self, position):
		return math.floor((position - 1)/2)

	def level(self, position):
		num_of_nodes = position+1
		return math.floor(math.log2(num_of_nodes))

	def isEmpty(self):
		return self.root == None

	def add(self, node):
		if(self.isEmpty()):
			self.root = node

		self.heap.append(node)
		self.trickleUp()

	def remove(self):
		if(self.isEmpty()):
			print("Heap Empty")
			return None
		elif(len(self.heap) - 1 == 0):
			self.root = None
			return self.heap.pop()
		else:
			temp = self.root
			self.heap[0] = self.heap[len(self.heap)-1]
			self.heap[len(self.heap)-1] = self.root
			result = self.heap.pop()
			self.trickleDown()
			return result

	def trickleUp(self):
		current = (len(self.heap)-1)
		parent = self.getParent(current)
		while True:
			temp = self.heap[current]
			if(self.heap[current].totalCost < self.heap[parent].totalCost):
				self.heap[current] = self.heap[parent]
				self.heap[parent] = temp
			else:
				self.root = self.heap[0]
				break

			if(parent == 0):
				self.root = self.heap[0]
				break

			current = parent
			parent = self.getParent(current)

	def trickleDown(self):
		current = 0
		children = self.getChildren(current)
		leftChild = children[0]
		rightChild = children[1]

		while True:

			if(rightChild <= (len(self.heap)-1)):
				if(self.heap[rightChild].totalCost 
					<= self.heap[leftChild].totalCost):
					if(self.heap[current].totalCost > self.heap[rightChild].totalCost):
						temp = self.heap[current]
						self.heap[current] = self.heap[rightChild]
						self.heap[rightChild] = temp
						
						current = rightChild
						children = self.getChildren(current)
						leftChild = children[0]
						rightChild = children[1]
					else:
						self.root = self.heap[0]
						break
						
						
				else:
					if(self.heap[current].totalCost > self.heap[leftChild].totalCost):
						temp = self.heap[current]
						self.heap[current] = self.heap[leftChild]
						self.heap[leftChild] = temp
						
						current = leftChild
						children = self.getChildren(current)
						leftChild = children[0]
						rightChild = children[1]
					else:
						self.root = self.heap[0]
						break
						

			elif(leftChild == (len(self.heap)-1)):
				if(self.heap[current].totalCost > self.heap[leftChild].totalCost):
					temp = self.heap[current]
					self.heap[current] = self.heap[leftChild]
					self.heap[leftChild] = temp
					
					current = leftChild
					children = self.getChildren(current)
					leftChild = children[0]
					rightChild = children[1]
				else:
					self.root = self.heap[0]
					break

			else:
				self.root = self.heap[0]
				break





