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

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def recursive_sum(numbers):
    if len(numbers)==1:
        return numbers[0]
    
    return numbers[0] + recursive_sum(numbers[1:])

number_list = [10,20,30,40]
print(recursive_sum(number_list))
    