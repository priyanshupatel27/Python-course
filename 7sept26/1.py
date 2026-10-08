#print the maximum and minimum number using functionho
# def show(n):
#     if(n==0):
#         return 0
    
#     print(n)
#     show(n-1)
# show(5)

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(4))

# double = lambda x:x*2

marks = [40,55,60,75,80]
result = list(map(lambda x: x+5 , marks))
print(result)
