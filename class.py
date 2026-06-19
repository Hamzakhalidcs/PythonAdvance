# Class is basically a blueprint 
from pyclbr import Class


class Car:
    pass

car1 = Car()
print(car1)

# Constructor runs automatically when object is created
class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
print(car1.brand)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Hamza", 50000)
print(emp1.name)
print(emp1.salary)

emp2 = Employee("Ali", 60000)
print(emp2.name)
print(emp2.salary)


# Atm Servie project 
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} Deposited. Balance : {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount
            print(f"{amount} withdrawn. Balance : {self.balance}")

    def show_balance(self):
        print(f"Current balance is {self.balance}")

    def transfer(self, amount, receiver_account):
        if amount <= 0:
            print("Invalid transfer amount")
        
        elif amount > self.balance:
            print("Insufficient funds for transfer")

        else:
            self.balance -= amount
            receiver_account.balance += amount
            print(f"{amount} transferred from {self.name} to {receiver_account.name}.")


# account1 =BankAccount("Hamza", 10000)
# account1.deposit(50000)
# account1.withdraw(20000)
# account1.show_balance()

acc1 = BankAccount("Hamza", 5000)
acc2 = BankAccount("Ali", 3000)
acc1.transfer(1000, acc2)

