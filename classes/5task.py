class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        self.Deposit = int(input())
        self.balance += self.Deposit
        print(f"Mr./Mrs.{self.owner}, your balance has been replenished by: {self.Deposit}. Your balance: {self.balance}")
    def withdraw(self):
        self.Withdraw = int(input())
        self.balance -= self.Withdraw
        print(f"Mr./Mrs. {self.owner} {self.Withdraw} was withdrawn from your balance. Your balance: {self.balance}")
