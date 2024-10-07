class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def deposit(self,amount):
        self._balance += amount

    def withdraw(self,amount):
        if amount < self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self._balance

new_account = BankAccount(2000)
new_account.deposit(500)
print(new_account.get_balance())
new_account.withdraw(1000)
print(new_account.get_balance())
new_account.withdraw(2500)
