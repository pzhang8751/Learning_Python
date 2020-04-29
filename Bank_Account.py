class Account:
    def __init__(self, name, number, type, balance):
        self.name = name
        self.accountNumber = number
        self.accountType = type
        self.balance = balance


    def getBalance(self):
        print("Your current account balance is " + str(self.balance))

    def deposit(self):
        ammount = int(input("How much money would you like to deposit to your account? "))
        if ammount < 0:
            print("Sorry that transaction is not possible, please try again.")
        else:
            self.balance = self.balance + ammount
            self.getBalance()

    def withdrawl(self):
        ammount = int(input("How much money would you like to withdraw from your account? "))
        if ammount > self.balance:
            print("Sorry you do not have enough money to take out.")
        elif ammount < 0:
            print("Sorry that transaction is not possible, please try again.")
        else:
            self.balance = self.balance - ammount
            self.getBalance()

    def startUp(self):
        print("Hello, welcome to onlineBanking.")
        self.name = str(input("Please give me your first name."))
        self.accountNumber = str(input("Please give me your vault number."))
        self.accountType = str(input("What type of account do you want to access?"))
        self.balance = int(input("And how much money do you want to place into your account?"))
        answer = str(input("Would you like to deposit/withdrawl money or exit?"))
        if answer == "deposit":
            self.deposit()
        elif answer == "withdrawl":
            self.withdrawl()
        elif answer == "exit":
            print("Thank you for banking with us, we hope to see you again.")
        else:
            print("Im sorry that is not a valid option, please try again next time.")

    def getDetails(self):
        print("Account owner is " + self.name)
        print("Account number is " + self.accountNumber)
        print("Account type is " + self.accountType)
        print("Account balance is " + str(self.balance))

account1 = Account('Patrick', '567', 'savings', 75858)
account1.startUp()

