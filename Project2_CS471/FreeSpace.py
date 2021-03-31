# Importing necessary dependencies
import itertools
import gc

class Partition:

	# Auto incrementing partition id 
	newPID = itertools.count()

	def __init__(self, partitionID = None, partitionSize = None, prevPartition = None, nextPartition = None):

		self.partitionID = next(Partition.newPID)
		self.partitionSize = partitionSize
		self.prevPartition = prevPartition
		self.nextPartition = nextPartition

	# Getters and Setters for Partition Node
	def setNextPartition(self, nextPartition):
		self.nextPartition = nextPartition
		
	def setPrevPartition(self, prevPartition):
		self.prevPartition = prevPartition

	def __hash__(self):
		return hash(str(self))

	def __str__(self):
		return "Partition #" + str(self.partitionID) + " Partition Size: " + str(self.partitionSize) + "KB"

	def __repr__(self):
		return "Partition #" + str(self.partitionID) + " Partition Size: " + str(self.partitionSize) + "KB"

# Free Memory(Singly Linked List)
class FreeMemory:
	
	def __init__(self, head = None, tail = None):
		self.head = head
		self.tail = tail

	# Insert partition at head of the list
	def insert(self, partitionSize):
		newPartition = Partition(partitionSize = partitionSize)
		newPartition.setNextPartition(self.head)
		newPartition.setPrevPartition(self.tail)
		if self.head is not None:
			self.head.prevPartition = newPartition
		self.head = newPartition

	# Delete partition
	def delete(self, dele):
		# Base Case
		if self.head is None or dele is None:
			return

		# If node to be deleted is head node
		if self.head == dele:
			self.head = dele.nextPartition
 
		# Change next only if node to be deleted is NOT the last node
		if dele.nextPartition is not None:
			dele.nextPartition.prevPartition = dele.prevPartition

		# Change prev only if node to be deleted is NOT the first node
		if dele.prevPartition is not None:
			dele.prevPartition.nextPartition = dele.nextPartition

		# Finally, free the memory occupied by dele
		gc.collect()
			 

	# Print all partitions
	def displayFreeSpace(self):
		
		current = self.head
		# Incase memory hasn't been populated at time of display call()
		if current != None:
			while current.nextPartition != None:
				print(current)
				current = current.nextPartition
		else: 
			print("Currently no free space! Must Populate!")

	# Populate Free Memory with generic partition sizes
	def populateFreeMemory(cls):

		if cls.head is None:
			cls.insert(None)
			cls.insert(415)
			cls.insert(605)
			cls.insert(810)
			cls.insert(200)
			cls.insert(107)
			print("Free Space Initialized")
		else:
			print("Free Space Already Initialized!")
			return