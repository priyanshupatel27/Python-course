# # lists is a data type where you can store multiple items under 1 name. More technically, lists act like dynamic arrays which means you can add more items on the fly. 
# L = [20,'Jessa',35.5,[30,40,50]]
# print(L[3])

# #arrays:- fixed size , homogeneous , contigous  memory, faster than lists , takes less memory space as compared to list
# print(id(L))  # id() :- gives the address of the values where they are stored8i

# #characteristics of list:- ordered , changeble/mutable , heterogenous , can have duplicates , are dynamic , can be nested , items can be accessed , can contain any kind of objects in python

# #  creation of a list
# E = [] #empty list or print([])
# # 1D array
# print([1,2,3,4,5])

# #2d list or nested list
# print([1,3,4,[4,5]])  # this is heterogeneous because it has 4 elements 123 as numbers and a list[4,5]

# #3d list
# print([[[1,6],[6,9]],[[4,5],[5,6]]])  

# #type conversion
# print(list("hello"))

# # indexing and slicing
# indexing is same as string it has both positive and negative indexing
# if out of range it will show error , list out of range
# l = [2,3,4,5,6]
# print(l[0])
# print(l[-1])

# #  for 2d list

# l = [2,3,4,[5,6,9,0,89]]
# print(l[-1][-1])  #yaha pe  first -1 matlab list[5,6] and second -1 matlab 6
# print(l[3][0])


# Slicing :- this is also same as string
# print(l[0:])
# print(l[3][1:4])
# print(l[::-1])
# print(l[-1:])
# print(l[::])

# #operation  in list

# #append :- add items in list at last
# l.append(True)
# l.append(["multiple","Elements"])
# print(l)
# # extend :- add multiple elements in list at last
# l.extend([6,90,False])
# print(l)
# l.extend("delhi")
# print(l)

l = [2,3,4,[5,6,9,0,89]]
#insert :- insert elements at any position by giving index and value
# l.insert(1,100)
# print(l)
# l.insert(3,[4,6])
# l.insert(5,[99,00])
# print(l)


# how to edit existing elements in a list

# l[2]=400
# print(l)
# l[-1][0]=500
# # by using slicing
# l[0:3]=200,300,400
# print(l)

# deleting a list :- del , remove , pop , clear
# del l   #this will delete the complete list
# print(l)  # this will give error because the list has already been deleted


# del l[0]
# print(l)
# del l[0:2]
# print(l)

# remove:- benefit is it can delete by value , use if the index is not known and i want to delete it by using the value
# l.remove(4)
# print(l)

#pop :- this can be used by 2 types 
# 1st :-  by giving index so it will remove according to the index
#2nd :- by not giving anything so it's default behavious is to remove the last element

# l.pop(0) # by giving the index
# l.pop()  #by not giving any index so it will remove the last element by default
# print(l)

# clear :- it clears  the whole list at once
# l.clear()
# print(l)

"""DIfference between delete and clear 
delete :- completly removes the whole list with the existance of the list itself means no list is present with that name 
clear :- it remove the data inside the list means the list is present only it's values/datas are gone/cleared"""

"""operators in list 
that are :- 
1. Arithemtic operator + *
2. Membership  in/not in
3. loop"""
