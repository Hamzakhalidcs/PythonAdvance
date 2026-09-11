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
    def wrapper(*args):
        print("Before")
        func(*args)
        print("After")

    return wrapper
    # print("Hello from decorator")

@my_decorator
def greet(name, age):
    print(f"Hello {name}, you are {age}")

@my_decorator
def add(a,b):
    print(a+b)

greet("Hamza", 29)
add(10, 20)

def show_number(*args):
    print(args)

show_number(10, 20, 30)

# *kwargs example 
def show_info(**kwargs):
    # print(kwargs)     print the whole dictionary 
    print(kwargs.get("name"))  # if we want to get only name or any single argument

show_info(name="Hamza", Age=29, City="Nowshera")
# **kwargs means collect keywords argument into a dictioanry. 
# but when calling another function 
def greet_name(name, age):
    print(f"Hello {name}, you are {age}")

data = {
    "name" : "Hamza",
    "age" : 29
}

greet_name(**data)