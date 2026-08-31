def countdown(n):
    if n==0 :
        return
    
    print(n)
    countdown(n -1)


"""
we will understand 
function call it self 
base case 
recursive case 
call stack
unwinding 

1. BaseCase if n==0:
        return 

    Basecase tells when recursion when to STOP. 

2. Recursive Case countdown(n -1)
   Recursive case tells recursion how to continue. 

There are two cases 
Going Down (I need someone below me to give an answer)
Coming Up  (I received answered, so now i can calculate my own answer)
"""

print(countdown(3))