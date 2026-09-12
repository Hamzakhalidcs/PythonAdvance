"""
A decorator is a fucntion that takes another function as an argument, add some functionanlity to it,
and returs a new function. It's a way to "wrap" or "modify" a function with out changing its actual code. 
Think of it 
The gift = your original Function 
The wrapper = The docorator
The final Package = the decorated function 
*args collects positional arguments in tuple.(Tuple)
**kwargs is similar but it handles keyword arguments. (dictionary)

**kwargs while receiving        
collect
        
dictionary
        
**kwargs while calling
        
unpack
        
keyword arguments
"""


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")

    return wrapper
    # print("Hello from decorator")

@my_decorator
def greet(name, age):
    print(f"Hello {name}, you are {age}")

@my_decorator
def add(a,b):
    print(a+b)

greet("Hamza", age=29)
# greet(name="Hamza", age=29)
