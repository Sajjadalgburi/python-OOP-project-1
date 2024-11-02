class BalanceExepction(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created. \n Balance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"Your balance is ${self.balance:.2f}")

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            print("\nMust pass a valid number")
        elif amount < 15:
            print("\nMinimum deposit amount is $15")
        else:
            self.balance += amount
            print(
                f"\nYou have successfully made a deposit.\nYour new balance is {self.balance}"
            )

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceExepction(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceExepction as error:
            print(f"\n Withdraw interuptted: {error}")

    def transfer(self, amount, account):
        try:
            print(f"\n**********\n\nbeginning transfer..")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\ntransfer complete\n\n**********")
        except BalanceExepction as error:
            print(f"\n Withdraw interuptted: {error}")
