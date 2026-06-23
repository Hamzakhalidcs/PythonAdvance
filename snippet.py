class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
print(car1.brand)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1  = Employee("Hamza", 50000)
print(emp1.name)
print(emp1.salary)

emp2 = Employee("Ali", 60000)
print(emp2.name)
print(emp2.salary)


# AtM Servce Project

class BankAccount:
    def __init__ (self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} Deposited. Balance : {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Invalid withdrwal amount")
        else:
            self.balance = self.balance - amount
            print(f"{amount} withdrawn. Balance : {self.balance}")

    def transfer(self, amount, receiver_account):
        if amount <= 0:
            print("Invalid transfer amount")
        
        elif amount > self.balance:
            print("Insufficient funds for transfer")

        else:
            self.balance -= amount
            receiver_account.balance += amount
            print(f"{amount} transferred from {self.name} to {receiver_account.name}")

    def show_balance(self):
        print(f"{self.name}: {self.balance}")


acc1 = BankAccount("Hamza", 10000)
acc2 = BankAccount("Ali", 5000)

acc1.transfer(3000, acc2)
acc1.show_balance()

acc2.show_balance()
