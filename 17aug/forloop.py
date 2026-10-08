                   # sum to  n 
# n = int(input("enter number"))
# sum = 0
# for i in range(1,n+1,1):
#     sum = sum+i
# print(sum)

        
                    # factorial of n 

# n = int(input("enter number"))
# factorial = 1
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)


            #    print elements in a list 

list = [19, 39, 48, 89]

n = int(input("Enter number to search: "))

found = False

for i in range(len(list)):
    if list[i] == n:
        found = True
        break

if found:
    print("yes")
else:
    print("no")