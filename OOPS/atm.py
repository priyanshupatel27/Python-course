class Atm():
    # constructor 
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.count = 3
        self.menu()

#creating menu
    def menu(self):
        n = input("""
---------------------------------------

1. enter 1 to create a pin
2. enter 2 to check balance
3. enter 3 to add money
4. enter 4 to withdraw
5. enter 5 to change the pin 
6. enter anything to exit 
---------------------------------------
""")
        if n == '1':
             #create pin
            self.create_pin()
            self.menu()
           
        elif n == '2':
            # check balance
            self.check_balance()
            self.menu()
        elif n == '3':
            # add money
            self.add_money()
            self.menu()
        elif n == '4':
            #withdraw
            self.withdraw()
            self.menu()
        elif n =='5':
            self.change_pin()

        else:
            # exit
            self.exit()

#create  the  pin function
    def create_pin(self):
        n = int(input("enter the pin:- "))
        b = float(input("enter the balance:- "))
        self.pin  = n
        self.balance = b
        print("Pin created successfully")

#creating the function to check the balance
    def check_balance(self):
        print("Total Balance = ",self.balance)

        #creating the function to add money
    def add_money(self):
        money = float(input("Enter the amount you want to add: "))
        self.balance = self.balance + money
        print("total balance = ",self.balance)

        #creating the function to withdraw
    def withdraw(self):
        amount = int(input("enter the amount you want to withdraw"))
        if amount > self.balance:
            print("Money out of bound")
        else:
            print("money withdrawl successfully")
            self.balance = self.balance-amount
            print("current balance = ",self.balance)

        #creating the function to exit completely
    def exit(self):
        print("exited successfully")
        return
    def change_pin(self):
        old_pin = int(input("enter the old pin"))
        if old_pin == self.pin:
            new_pin = int(input("enter the new pin"))
            self.pin = new_pin
        else:
            self.count -= 1
            # print("enter the correct pin")
            if self.count > 0 :
                print("incorrect pin")
                print("you have ",self.count," chances remaining ")
                self.menu()
            else:
                print("your account has been blocked for 24 hrs")
                return
                
        
        

obj = Atm()

