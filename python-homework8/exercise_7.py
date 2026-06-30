# 1. Define the Wallet class
class Wallet:
    def __init__(self, balance=0):
        self.balance = balance

    def add(self, amount):
        self.balance += amount

    def spend(self, amount):
        if amount > self.balance:
            print(f"Cannot spend {amount} — only {self.balance} left.")
        else:
            self.balance -= amount
            print(f"Spent {amount}. Balance: {self.balance}")


my_wallet = Wallet(50)
print(f"Balance: {my_wallet.balance}")

my_wallet.spend(20)

my_wallet.spend(100)