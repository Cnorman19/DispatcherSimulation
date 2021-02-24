from queue import PriorityQueue
from functools import total_ordering

# Process Object to add to ReadyQueue and BlockedList
@total_ordering
class Process:
	def __init__(self, name, status, priority):
		self.name = name
		self.status = status 
		self.priority = priority

	def __lt__(self, other):
		return self.priority < other.priority

	def __eq__(self,other):
		return self.priority == other.priority

	def __str__(self):
		return self.name + " - " + " Status: " + self.status + " - " + " Priority: " + self.priority

class Dispatcher:
	
	# Initialize ReadyQueue and BlockedList Priority Queues
	ReadyQueue = PriorityQueue()
	BlockedList = PriorityQueue()

	# Add processes to ReadyQueue and BlockedList
	def addProcess(cls):
		P1 = Process("Process 1", "Ready", '1')
		P2 = Process("Process 2", "Working", '2')
		P3 = Process("Process 3", "Terminated", '3')

		B1 = Process("Blocked Process 1", "BLOCKED", '3')
		B2 = Process("Blocked Process 2", "BLOCKED", '1')

		cls.ReadyQueue.put(P1)
		cls.ReadyQueue.put(P2)
		cls.ReadyQueue.put(P3)

		cls.BlockedList.put(B1)
		cls.BlockedList.put(B2)
	
	# Print contents of ReadyQueue
	def printQueues(cls):
		while not cls.ReadyQueue.empty():
			next_item = cls.ReadyQueue.get()
			print(next_item)

		# Print contents of BlockedList
		while not cls.BlockedList.empty():
			next_blocked_item = cls.BlockedList.get()
			print(next_blocked_item)
