def addition(a,b):
    print("addition ")
    return a+b
def subtraction(a,b):
    print("subtraction")

    return a-b
def division(a,b):
    print("division")
    return a/b
def multiplication(a,b):
    print("multiplication")
    return a*b
def average(a,b):
    print("average")
    return (a+b)/2
nums = [1.2,4,5,5]
squares = list(map(lambda n:n**2,nums))
print(squares)
even = list(filter(lambda n:n%2==0))
print(even)
odd=list(filter(lambda n:n%2!=0))
print(odd)


print("iteration number 5")
print(addition(4,6))

print(subtraction(8,6))

print(division(4,2))

print(multiplication(4,6))
print(average(5,9))
# print("ddd",average(5,7))

