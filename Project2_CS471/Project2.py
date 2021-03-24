# Importing necessary dependencies
from functools import total_ordering
import itertools

class Process:
    # Auto increment pid
    newPID = itertools.count()

    def __init__(self, pid = None, size = None):
        self.pid = next(Process.newPID)
        self.size = size
    def __str__(self):
        return "Process #" + str(self.pid) + " - " + "Size: " + str(self.size) + "KB"


class Dispatcher():

    ProcessRequest = []

    def populateProcessRequest(cls):
        P1 = Process(size = '302')
        P2 = Process(size = '170')
        P3 = Process(size = '620')
        P4 = Process(size = '800')
        P5 = Process(size = '430')
        
        cls.ProcessRequest.append(P1)
        cls.ProcessRequest.append(P2)
        cls.ProcessRequest.append(P3)
        cls.ProcessRequest.append(P4)
        cls.ProcessRequest.append(P5)

    def displayProcessRequest(cls):
        
        for Process in cls.ProcessRequest:
            print(Process)

D = Dispatcher()
D.populateProcessRequest()
D.displayProcessRequest()