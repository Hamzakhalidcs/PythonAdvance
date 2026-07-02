# Abstraction means hiding unnecessary implementation details and showing the only essential features.
# you know what to do, but you dont need to know how it works internally . 

# python provides a module called abc i.e Abstract Base Class
# Its is a specaial class that can not be used to create object directly.
from abc import ABC, abstractmethod
 
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")


car = Car()
car.start()


# You cannot create an object of an abstract class.
# it will raise("TypeError: Can't instantiate abstract class Shape  with abstract method area")