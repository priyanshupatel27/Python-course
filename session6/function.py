# create a even function
#to print the documentation of any function use :)  .__doc__     example:) print(print.__doc__)   this will print the documentation of the  print function
def even(i):   #this i is parameter
    """here we are going to check for even number
        if number is divided by 2 and remainder is 0 then it is even
            else it is odd"""
    if type(i)==int:
     if i%2==0:
        return "even"
     else:
        return "odd"
    else:
       return "pagal hai kya be "
print(even(4))  # this is argument
"""jab function create kar rhe ho tab wo parameter hota hai
jab function ko call karte ho tab jo value pass karte ho toh wo argument hota hai """



'''there are 3 types of argument
1. default argument:- agar parameters ko missing arguments provide naa kiya jaye toh defalt parameter work aata hai taki error naa aaye
2. positional argument:- follows the order of the parameter
3. keyword argument:- arguments pass karte waqt parameters ko define kar ke bhi arguments pass kiya jaa sakta hai .  while calling a function in main body ,,,, multiply(a=8,b=9)                        '''

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")

def multiply(a=1,b=1):
   return a*b

#args vs kwargs
# args:- allows us to pass a variable number of ("non-keyword") arguments to a function , jab pata hi naa ho ki user kitne number of inputs dega
# isko fark nahi padta user kitne inputs de raha
# * iska matlb python samajh jata hai ki user multiple numbber of inputs dene wala hai 
def args_multiply(*args):
   product = 1
   for i in args:
      product = product*i
   print(args)  #args store values in tuple , and args can be replaced by any other name like patel , sonu , etc , its user defined only * is important to define args
   return product

print(args_multiply(1,3,4))

# another example of args but name is different 
def addition(*add):
   sum = 0 
   for i in add:
      sum = sum+i
   print(add)
   return sum
print(addition(1,2,3,4,5,6))

# print(args_multiply.__doc__)
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")

# __________________
#   KWARGS :) kwargs allows us to pass any number of keywords arguments .    Keywords arguments means that they contain a key-value pair, like a python dictionary.
# __________________

# ** is used to define kwargs

# create a function to print the countries with their capital 
def display(**kwargs):
   for (key,value) in kwargs.items():
      print(key,"->",value)

print(display(india = "delhi", srilanka = "colombo",nepal = "katmandu"))

#the words args and kwargs are user defined names

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")

# how functions operate in memory level
#nested function


