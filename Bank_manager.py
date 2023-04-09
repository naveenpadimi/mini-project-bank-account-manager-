from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class CheckingAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")

class SavingsAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        self.interest_rate = 0.02

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

class BusinessAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")

class ATM:
    def __init__(self):
        self.checking = CheckingAccount(1000.0)
        self.savings = SavingsAccount(5000.0)
        self.business = BusinessAccount(20000.0)

    def run(self):
        while True:
            print("1. Checking Account")
            print("2. Savings Account")
            print("3. Business Account")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("1. Deposit")
                print("2. Withdraw")

                option = int(input("Enter your option: "))

                if option == 1:
                    amount = float(input("Enter amount to deposit: "))
                    self.checking.deposit(amount)
                    print(f"New balance: {self.checking.balance}")
                elif option == 2:
                    amount = float(input("Enter amount to withdraw: "))
                    self.checking.withdraw(amount)
                    print(f"New balance: {self.checking.balance}")

            elif choice == 2:
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Add Interest")

                option = int(input("Enter your option: "))

                if option == 1:
                    amount = float(input("Enter amount to deposit: "))
                    self.savings.deposit(amount)
                    print(f"New balance: {self.savings.balance}")
                elif option == 2:
                    amount = float(input("Enter amount to withdraw: "))
                    self.savings.withdraw(amount)
                    print(f"New balance: {self.savings.balance}")
                elif option == 3:
                    self.savings.add_interest()
                    print(f"New balance: {self.savings.balance}")

            elif choice == 3:
                print("1. Deposit")
                print("2. Withdraw")

                option = int(input("Enter your option: "))

                if option == 1:
                    amount = float(input("Enter amount to deposit: "))
                    self.business.deposit(amount)
                    print(f"New balance: {self.business.balance}")


atm = ATM()
atm.run()
