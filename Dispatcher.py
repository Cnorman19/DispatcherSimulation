# Importing necessary Dependencies
from queue import PriorityQueue
from functools import total_ordering
import itertools
from random import randrange

# Process Object to add to ReadyQueue and BlockedList
@total_ordering
class Process:

	# Auto Iterating ID
	newid = itertools.count()

	# Overloading Dunder Methods
	def __init__(self, name, status, priority):
		self.id = next(Process.newid)
		self.name = name
		self.status = status 
		self.priority = priority

	def __lt__(self, other):
		return self.priority < other.priority

	def __eq__(self,other):
		return self.priority == other.priority

	def __str__(self):
		return "ID: " + str(self.id) + " - " + self.name + " - " + " Status: " + self.status + " - " + " Priority: " + self.priority

class Dispatcher:
	
	# Initialize ReadyQueue and BlockedList Priority Queues
	ReadyQueue = PriorityQueue()
	BlockedList = PriorityQueue()
	RunningQueue = PriorityQueue()

	# Add processes to ReadyQueue and BlockedList
	def populateReadyQueue(cls):
		P1 = Process("Process 1", "Ready", '1')
		P2 = Process("Process 2", "Ready", '2')

		R1 = Process("Process 3", "Runnning", '1')

		B1 = Process("Process 4", "Blocked", '3')
		B2 = Process("Process 5", "Blocked", '1')

		cls.ReadyQueue.put(P1)
		cls.ReadyQueue.put(P2)

		cls.RunningQueue.put(R1)

		cls.BlockedList.put(B1)
		cls.BlockedList.put(B2)
		print("Queues have been populated!\nPlease proceed with context switch!")
	
	# Remove Process from ReadyQueue
	def removeProcess(cls):
		temp = cls.ReadyQueue.get()
		print("Process Terminated -> " + str(temp) + "\n")
		cls.printQueues() 


	# Switch status of Process
	def contextSwitch(cls):
		current = cls.ReadyQueue.get()
		current.status = "Running"
		cls.RunningQueue.put(current)

		current2 = cls.RunningQueue.get()
		current2.status = "Blocked"
		cls.BlockedList.put(current2)

		x = randrange(2)
		
		if x == 0: 
			print("Context Switch Initiated - Cause: Time Slice Exceeded!\n")

		if x == 1:
			print("Context Switch Initiated - Cause: Blocking Call! \n")

		cls.printQueues()

	# Print contents of both queues
	def printQueues(cls):

		# Iterators for print loop(s)
		indexReadyQueue,indexBlockedList,indexRunningQueue = 0,0,0

		# Print contents of ReadyQueue
		print("Ready Processes:")
		while indexReadyQueue != cls.ReadyQueue.qsize():
			print(cls.ReadyQueue.queue[indexReadyQueue])
			indexReadyQueue+=1

		# Print contents of RunningQueue
		print("Running Processes:")
		while indexRunningQueue != cls.RunningQueue.qsize():
			print(cls.RunningQueue.queue[indexRunningQueue])
			indexRunningQueue+=1
			
		# Print contents of BlockedList
		print("Blocked Processes:")
		while indexBlockedList != cls.BlockedList.qsize():
			print(cls.BlockedList.queue[indexBlockedList])
			indexBlockedList+=1
		print("\n")