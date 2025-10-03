class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance = {self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance = {self.balance}")
        else:
            print("Insufficient funds! Withdrawal denied.")

    def __str__(self):
        return f"Account owner: {self.owner}\nBalance: {self.balance}"


acc = Account("Nurdana", 100)   
print(acc)

acc.deposit(50)    
acc.withdraw(30)   
acc.withdraw(200)  