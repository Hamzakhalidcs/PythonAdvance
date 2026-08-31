"""
A Data Structure is a specialized way of organizing, storing and managing data on computer 
so that it can be accessed and modified efficiently.
Stack is a Data Structure that follows LIFO(Last IN FIRST OUT)
if there are plates in stack first A then B then C, so if you want A so you have to took out 
C and B first then you will get A. 
Added A->B->C
Removed C->B->A
The last item you put in the first item you take out.

Python list can be behave like stack 

The important stack operation is 
stack.append("A")   # Push 
stack.pop()         #Pop

The Time complexity for stack is 
append() O(1) average 
pop()   O(1) average
peek    O(1) average i.e look for item like stack[-1] give you the last item.

Stacks are usful when the most recents things should be handle first. 
Example 
. Undo Operation
. Browser history concept
. Function Call stack 
. Expression Parsing.
. Backtracking 
. DFS(Depth first search)
"""

stack = []

stack.append("A")
stack.append("B")
stack.append("C")
stack[-1]

# Now stack is ["A", "B", "C"], to remove the top item you have to remove C first 
stack.pop()
# this will remove C and then will B and in the last it will be A . 

def stack_operation():
    # Create empty stack using list 
    stack = []

    # Push item in stack 
    stack.append("Python")
    stack.append("Java")
    stack.append("C++")

    # print the stack 
    print(f"Stack after pushes: {stack}")

    # remove the item from stack 
    removed_item = stack.pop()

    # print the remove item
    print(f"removed item: {removed_item}")

    # print the final stack
    print(f"Final Stack : {stack}")


print(stack_operation())



