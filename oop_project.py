from bank_accounts import *  # import everything from bank_accounts file

John = BankAccount(2000, "Mr.John")
Doe = BankAccount(900, "Dr.Doe")
Gray = BankAccount(900, "Gray")
Bat = BankAccount(900, "Bat")

Doe.deposit(900)
Gray.deposit(94500)
Bat.deposit(1900)
John.withdraw(2300)

Gray.transfer(10000, Bat)
