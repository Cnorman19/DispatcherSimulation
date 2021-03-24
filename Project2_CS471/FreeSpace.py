# Importing necessary dependencies
import itertools

class Partition:

	# Auto incrementing partition id 
	newPID = itertools.count()

	def __init__(self, partitionID = None, partitionSize = None, prevPartition = None, nextPartition = None):

		self.partitionID = next(Partition.newPID)
		self.partitionSize = partitionSize
		self.prevPartition = prevPartition
		self.nextPartition = nextPartition

	# Getters and Setters for Partition Node
	def getNextPartition(self):
		return self.nextPartition
	
	def setNextPartition(self, nextPartition):
		self.nextPartition = nextPartition

	def getPrevPartition(self):
		return self.prevPartition
	
	def setPrevPartition(self, prevPartition):
		self.prevPartition = prevPartition

	def __str__(self):
		return "Partition #" + str(self.partitionID) + " Partition Size: " + str(self.partitionSize) + "KB"

# Free Memory(Singly Linked List)
class FreeMemory:
	
	def __init__(self, head = None):
		self.head = head

	# Insert partition at head of the list
	def insert(self, partitionSize):
		newPartition = Partition(partitionSize = partitionSize)
		newPartition.setNextPartition(self.head)
		self.head = newPartition

	# Print all partitions
	def display(self):
		current = self.head
		# Incase memory hasn't been populated at time of display call()
		if current != None:
			while current.nextPartition != None:
				print(current)
				current = current.nextPartition
		else: 
			return

	# Populate Free Memory with generic partition sizes
	def populateFreeMemory(cls):
		cls.insert(None)
		cls.insert(415)
		cls.insert(605)
		cls.insert(810)
		cls.insert(200)
		cls.insert(107)

F = FreeMemory()
F.populateFreeMemory()
F.display()
