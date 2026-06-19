def transfer(self, amount, receiver_account):
        if amount <= 0:
            print("Invalid transfer amount")
        
        elif amount > self.balance:
            print("Insufficient funds for transfer")

        else:
            self.balance -= amount
            receiver_account.balance += amount
            print(f"{amount} transferred from {self.name} to {receiver_account.name}.")

def transfer(self, amount, receiver_account):
        if amount <= 0:
              print("Invalid transfer amount")

        elif amount > self.balance:
              print("Insufficient funds for transfer")

        else:
              self.balance -= amount
              receiver_account.balance += amount
              print(f"{amount} transferred from {self.name} to {receiver_account.name}.")


a