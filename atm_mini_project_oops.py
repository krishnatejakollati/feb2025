#Day 14: ATM mini project using OOPS concept

class atm_machine():
    def __init__(self,bankname,location,branchname,balance=0):
        self.bankname=bankname
        self.location=location
        self.branchname=branchname
        self.balance=balance
        #self.amount=amount
    def display_menu(self):
        print("\nPlease enter the choice from the below: ")
        print("1. Credit")
        print("2. Debit")
        print("3. Display Balance")
        print("4. Exit")
    def enter_choice(self):
        #choice_val=int(input("Enter your choice: "))
        return int(input("Enter your choice: "))
    def credit(self,amount):
        #global balance
        if amount<0:
            print("Enter positive amount")
        else:
            self.balance+=amount
            print(f"The credited amount is {amount} and the available balance is {self.balance} \n This transaction is processed in the ATM corresponding to {self.bankname} in the location {self.location} and in the branch {self.branchname}")
    def debit(self,amount):
        #global balance
        if amount<0:
            print("Enter positive amount")
        elif amount>=self.balance:
            print(f"The debit amount {amount} is greater than the avaiable balance {self.balance}, Hence this request cannot be processed due to insufficient funds")
        else:
            self.balance-=amount
            print(f"The debited amount is {amount} and the available balance is {self.balance} \n This transaction is processed in the ATM corresponding to {self.bankname} in the location {self.location} and in the branch {self.branchname}")
    def display_balance(self):
        print(f"The available balance is {self.balance}")
    def exit(self):
        print(f"The user is now exited from this ATM transactions happened at {self.bankname} ATM in the location {self.location} and in the branch {self.branchname}")        
    def invalid_choice(self):
        print(f"Please enter a valid choice")
    def atm(self):
        while True:
            self.display_menu()
            choice=self.enter_choice()
            if choice==1:
                amount=int(input("Enter the credit amount: "))
                self.credit(amount)
            elif choice==2:
                amount=int(input("Enter the debit amount: "))
                self.debit(amount)
            elif choice==3:
                self.display_balance()
            elif choice==4:
                self.exit()
                break
            else:
                #print("Now let us exit")
                self.invalid_choice()

icici=atm_machine("ICICI","Hyderabad","Hafeezpet")
icici.atm()



    



