# def f():
#     def x(a,b):
#         return a+b
#     return x

# val = f()(3,4)
# print(val)

# function ke andar ek dusra function as a input
"""function ke andar function"""
# def a():
#     print("a")
# def b(z):
#     print("c")
#     return z()
# print(b(a))

# functions are first class citizes  means they act like datatypes

# benefits of function:- 
# code modularity
# code readibility
# code reusability

"""Lamda Function"""
# chhota anonymus function and lambda keywords creates the lambda function
# a = lambda x:x**2
# print(a(8))
# b = lambda x,y : x+y
# print(b(10,8))

# lambda function has no name it's ananomyous 
# it returns function not value
# lambda always written in one lines
# lambda function is made to use only one Time
# it is used with higher order function


# check if l exists in hello
# c = lambda x,y: y in x
# print(c("hello","u"))

# d = lambda x: x%2==0
# print(d(9))

# e = lambda x: "even" if x%2==0  else "odd"
# print(e(8))

'''higher order function:- those return the other function or the function that recieves the input as a function ,,,, ex: map()'''

#print the square of each element in the list

a = list(map(lambda x : x**2,[8,9,20]))
print(a)

#print even and odd in place of their respective numbers
l = [1,2,3,4,5,6]
eo = list(map(lambda x : 'even' if x%2==0 else 'odd',l))
print(eo)

'''filter :- higher order function and does filter on a list on the given conditions'''
# fruits = ['apple','banana','citrus']
# f = list(filter(lambda x : x.startswith('a'),fruits))
# print(f)


'''reduce :- imported using functools '''
import functools
n = functools.reduce(lambda x , y:x+y,[1,2,3,4,5,6])
print(n)


#find min
min = functools.reduce(lambda x,y: x  if x<y else y,[1,2,3,4,5,50,0])
print(min)

#find max
max = functools.reduce(lambda x,y: x  if x>y else y,[1,2,3,4,5,50,0])
print(max)