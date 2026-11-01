#Generatlity to Specificity
# OOP:) it gives programmer to create their own datatypes

# Class:) it is a blueprint

# l = [1,2,3]
# list is a class and l is the object 
# the rules are defined in the list class and the objject is following rules
# l.reverse()
# print(l)

# class :) 1. data or property    2. functions or behaviour
#object is the instance of the class


# Syntax to create an objecct4
# objectname = classname()

# like :)  l = list()   or s = str() 

"""create a code for an atm machine"""
# there are two types of classes in python :- 1> Built-in Classes    2> User-defined Classes

class Atm:
    #  constructor
    def __init__(self):
        self.pin = ''   #variable pin
        self.balance = 0     #variable balance
        print("mai to execute ho gaya")
    def menu(self):
        user_input = input('''
Hi how can i help you?
1. press 1 to create pin
2. press 2 to change pin
3. press 3 to check balance
4. press 4 to withdraw
5. Anything to exit''')  
        if user_input == '1':
             #create pin
             
             self.create_pin()
        elif user_input == '2':
            #change pin
            pass
        elif user_input == '3':
            #check balance 
            pass
        elif user_input == '4':
            #withdraw
            pass
        else:
            exit()
    def create_pin(self):
        user_pin = input("enter your pin")
        self.pin = user_pin
        user_balance = int(input("enter balance"))
        self.balance = user_balance
        print("pin created successfully")
    def change_pin(self):
        old_pin = int(input("enter existing pin"))
        if(old_pin==self.pin):
            new_pin = int(input("enter new pin" ))
            self.pin = new_pin
            print("print change successfull")
            self.menu()
        else:
            print("Enter correct pin")
            self.menu()
    def check_balance(self):
        

        
7
# print(type(obj)

