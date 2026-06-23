# Encapsulation means controlling access to data and methods inside a class. 

#  by default everthing in python is public,
#  but we can use a single underscore (_) to indicate 
# that a variable or method is intended for internal use only.    

# protected attribute by using a single underscore 

# class Employee:
#     def __init__(self, name):
#         self._name = name


# emp1 = Employee("Hamza")
# print(emp1._name)

# still works but what is the use of this underscore
# it tells developers that do not access this directly, it is intended for internal use only.
# it's a convention, not a restiction.
#  private variable 

# class Employee:
#     def __init__(self, salary):
#         self.__name = salary


# emp2 = Employee(50000)
# print(emp2.__name) # this will give an error because __name is a private variable and cannot be accessed directly from outside the class.
# what if we try 

# print(emp2.__salary)
# this will also give an error because __salary is a private variable and cannot be accessed directly from outside the class.


# Then how we do access to the private variable 
# just add a method inside the class 


class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


obj1 = Employee(50000)
print(obj1.get_salary()) # this will work because we are accessing the private variable through a public method.