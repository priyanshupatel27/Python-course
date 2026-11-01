# """a set is an unordered collection of items, every set element is unique no duplications and must be immutable  and can also be used to perform mathematical set operations like union intersections symmetric 
# characteristics:-
#                  unordered
#                  Mutable
#                  No duplicates
#                  can't containg mutable data types(no multidimensional sets)"""
# # s1 = set()  #empty set
# # print(type(s1))

# # s2 = {1,2,3,{4,5}}  # string can't have mutable  items
# # print(s2)
#  #this returns false , although the data types are same but the contents are different
# s1 = {1,2,3}
# # s2 = {4,5,6}
# # print(s1==s2)
# # #this returns true , although the elements are in unordered form it checks the if they are present or not in both set 
# # s3 = {1,2,3}
# # s4 ={3,2,1}
# # print(s3==s4)

# # in sets u can't do changing like slicing or indexing , but u can add new items 

# # s = {1,2,3,4}
# # s.add(5)  # adds only a single item
# # print(s)
# # s.update([6,7,8])#adds multiple items but , the items should be in list form 
# # print(s)  


# # deleting items

# s = {1,2,3,4}
# # del s[0] # this can't be done because a indexing is not possible so u can't delete a single item in a set
# # u can delete only a single item in the set
# # del s
# # print(s)


# # discard :- in this u tell which items to be deleted and don't through error if the element is not present in the set

# s.discard(4)
# print(s)

# s.remove(8)#in this u tell which items to be deleted  but it  throws an error if the element is not present in the set
# print(s)

# s.pop() # automatically deletes a value on its own
# print(s)

# s.clear() # clears the whole set


# ----------------
# sets operations
# ----------------

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# # union :- prints all the elements in both the sets only a single time
# print(s1|s2)   or s1.union(s2) 

# # intersection :- prints the common elements in both the sets
# print(s1&s2)

# #difference:- s2 ke wo item jo s1  me nahi h
# print(s1-s2)

# #symmetric difference :- prints the non common elements
# print(s1^s2)

# #membership operator
# print(1 in s1)
# print(78 not in s1)

# s = {3,4,5,6,6}
# len(s)
# sum(s)
# min(s)
# max(s)
# sorted(s)
# sorted(s,reverse=True)
