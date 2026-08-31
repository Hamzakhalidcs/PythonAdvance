"""
A Queue is a Data structure that follows FIFO(FIRST IN FIRST OUT)
Thing aboout the people in line .
The person which arrived first, Served first as well.
Queues are useful when the things should be handled in arrival order. 
Examples 
. Print Job
. Task Processing
. Customer Service System
. Message Queues
. BFS(Breadth-first Search)
. Request Processing.  
"""

queue = []

queue.append("A")
queue.append("B")
queue.append("C")
queue.pop(0)

"""
But there is a problem 
pop(0) is O(n) because python has to shift the remaing elements. 
for real Queue, python provide
"""
from collections import deque

queue = deque()

queue.append("Python")
queue.append("JAVA")
queue.append("C++")

print("QUeue", queue)

removed_item = queue.popleft()

print("Removed", removed_item)

print("Final Queue", queue)

