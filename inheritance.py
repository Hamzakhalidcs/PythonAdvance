# Using Super() method
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, grade):
        # When a child class has its own __init__(), 
        # the parent's __init__() is NOT automatically called.
        super().__init__(name)
        self.grade = grade

    
s1 =  Student("Hamza", "A")
print(s1.name, s1.grade)
  

# Sentence to remember forever
# super().__init__() calls the parent class's constructor
# so the child object also gets all the attributes initialized by the parent.

# Inheritance lets a child class use the parent's methods and attributes.
# super() lets the child class run the parent's constructor (__init__)
# so the parent's attributes are initialized in the child object.



# Method overriding
# Means the child class provide its own version of method i.e already exist in parent class . 
class Animal:
    def speak(self):
        print("Animal make sound")

class Dog(Animal):
    def speak(self):
        # what if we want both method 
        super().speak()   # call the parent method
        print("Dogs Bark")

dog  =Dog()
dog.speak()


# Method Resolution Order(MRO) is the order in which python searches for methods and attributes 
class Father:
    def skills(self):
        print("Driving")

class Mother:
    def skills(self):
        print("Cooking")

class child(Father, Mother):
    pass       


c1 = child()
c1.skills()

# Python follows the inheritance order from Left to Right, so it will search for Father first .