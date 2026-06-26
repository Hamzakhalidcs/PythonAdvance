# polymorphism (means "One Interface many Forms")

# poly = many and morph means many

# one method can behave differently depending on the object called. 

class Animal:
    def speak(self):
        print("Animal make sound")

class Dog(Animal):
    def speak(self):
        print("Dog Bark")

class Cat(Animal):
    def speak(self):
        print("Meowww")


dog = Dog()
dog.speak()

cat = Cat()
cat.speak()

# Notice that the methos is same but behaviour is change depends on the object call.this is polym,orphism
