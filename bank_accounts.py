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
