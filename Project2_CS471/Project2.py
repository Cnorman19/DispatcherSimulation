# Importing necessary dependencies
from functools import total_ordering
import itertools
from FreeSpace import *
import pprint as p

class Process:
    # Auto increment pid
    newPID = itertools.count(start = 1)

    def __init__(self, pid = None, size = None):
        self.pid = next(Process.newPID)
        self.size = size

    def __eq__(self , other):
        return self.size == other.size

    def __hash__(self):
        return hash(self.pid)

    def __str__(self):
        return "Process #" + str(self.pid) + " - " + "Size: " + str(self.size) + "KB"

    def __repr__(self):
        return "Process #" + str(self.pid) + " - " + "Size: " + str(self.size) + "KB" + " - Located in Memory Partition -> "


class Dispatcher():
    # Creating necessary list and dictionary for Process request and running memory
    ProcessRequest = []
    RunningMemory = {}

    def populateProcessRequest(cls):
        
        # Adding initialized processes to ProcessRequest list
        if not cls.ProcessRequest:

             # Generating Process Objects for Process Request list 
            P1 = Process(size = '100')
            P2 = Process(size = '170')
            P3 = Process(size = '620')
            P4 = Process(size = '800')
            P5 = Process(size = '430')

            cls.ProcessRequest.append(P1)
            cls.ProcessRequest.append(P2)
            cls.ProcessRequest.append(P3)
            cls.ProcessRequest.append(P4)
            cls.ProcessRequest.append(P5)

            print("Process Request Generated!")
        
        else: 
            print("Already Populated!")

    def displayProcessRequest(cls):
        # Loop through Proccesses in ProcessRequest List and print them
        if not cls.ProcessRequest:
            print("No Process Request! Must Populate!")
            return

        print("Processes awaiting allocation: ")
        for Process in cls.ProcessRequest:
            print(Process)

    def allocate(cls):
        # Creating an instance of free memory

        MemoryFreeSpace = FreeMemory()

        if cls.RunningMemory:
            return

        if not cls.ProcessRequest:
            cls.populateProcessRequest()

        # Populating memory in order to carry out first fit allocation
        if MemoryFreeSpace.head is None: 
            MemoryFreeSpace.populateFreeMemory()

        # Loop through process request
        for i in cls.ProcessRequest:
            current = MemoryFreeSpace.head
            while current.nextPartition is not None:
                # Comparing Process from Process Request list to current Partition size in order to determine allocation
                if int(i.size) <= current.partitionSize:
                    cls.RunningMemory[i] = current
                    print("Process Allocated!")
                    MemoryFreeSpace.delete(current)
                    break
                current = current.nextPartition
            else:
                print("Not enough free space available to fit process -> " + str(i) + " - Moving to garbage!")
    def deallocate(cls):
        return
    def DisplayRunningMemory(cls):
        p.pprint(cls.RunningMemory)
