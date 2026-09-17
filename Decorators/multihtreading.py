"""
A thread is a part of execution inside a program.
why do we need thread. 
The flow is 
Task 1 -> Task 2 -> Task 3 (this is sequential execution.)

imagine your AI/Data Application has 
1. Download data from API A
2. Download data from API B.
3. Download data from API C. 
if you do them sequentially  API A done -> API B -> Done ->API C 
the thread can make progress independently,especially while one is waiting on I/O. 
Important thing to notice 
A process and thread are not the same thing. 
A process is the running program and the thread are execution paths with in that process. 
"""
import threading
import time

def task1():
    for i in range(3):
        print("Task 1", i)
        time.sleep(2)

def task2():
   for i in range(3):
       print("Task2", i)
       time.sleep(1)


thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)


thread1.start()
thread2.start()
 
thread1.join()
thread2.join()
# with join all the thread1, thread2. wait for thread1 and thread2 and then program finished. 
#. join() waits; it doesn't make threads sequential. 

# Thread run concurrently ; join() doesn't control their execution order - 
# it synchronizes the main thread with their completion. 

thread2.is_alive()

print("Program Fininshed")



