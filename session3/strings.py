# ============================================================
#                    PYTHON STRINGS
# ============================================================


# ------------------------------------------------------------
# 1. CREATING A STRING
# ------------------------------------------------------------

# Single quotes
s = 'hello'

# Double quotes
s = "hello"

# Triple single quotes
# Used mainly for multiline strings
s = '''hello'''

# Triple double quotes
# Also valid for multiline strings
s = """this is also valid"""

# Using str() function
s = str('hello')


# ------------------------------------------------------------
# 2. STRING INDEXING
# ------------------------------------------------------------

# Python automatically assigns an index to every character.

s = "Priyanshu Patel"

# Positive indexing:
# Starts from the left with 0
#
# P  r  i  y  a  n  s  h  u     P  a  t  e  l
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14

print(s[0])       # P

# Negative indexing:
# Starts from the right with -1
#
# P  r  i  y  a  n  s  h  u     P  a  t  e  l
#-15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(s[-1])      # l

# Negative indexing is useful when we don't know
# the exact length of the string.


# ------------------------------------------------------------
# 3. STRING SLICING
# ------------------------------------------------------------

s = "Priyanshu Patel"

# Syntax:
# string[start : stop : step]

# Stop index is NOT included.

print(s[0:5])

# If start is not given, Python starts from 0
print(s[:5])

# If stop is not given, Python goes till the end
print(s[3:])

# Step = 2
# It jumps 2 positions at a time
print(s[0:10:2])

# Negative step
# Moves from right to left
print(s[9:0:-2])


# ------------------------------------------------------------
# 4. REVERSING A STRING
# ------------------------------------------------------------

# [start : stop : step]
# Using -1 as step reverses the complete string.

print(s[::-1])


# Reverse the last 5 characters
print(s[-1:-6:-1])


# IMPORTANT:
# In normal slicing, start is usually smaller than stop
# when moving left to right.
#
# But when step is negative, we move right to left,
# so the starting index is generally larger than the stop index.


# ------------------------------------------------------------
# 5. EDITING A STRING / STRING IMMUTABILITY
# ------------------------------------------------------------

# Python strings are IMMUTABLE.
# This means we cannot directly change an existing character.

s = "Priyanshu"

# This is NOT allowed:
# s[0] = "A"

# String methods usually return a NEW string.

s = "Priyanshu"
new_s = s.replace("P", "A")

print(s)       # Priyanshu
print(new_s)   # A riyanshu


# ------------------------------------------------------------
# 6. DELETING A STRING
# ------------------------------------------------------------

s = "hello"

# del can delete the complete variable
del s

# print(s)
# This will give an error because s no longer exists.


# ------------------------------------------------------------
# 7. STRING CONCATENATION
# ------------------------------------------------------------

# We can join strings using +

print("delhi" + " mumbai")


# ------------------------------------------------------------
# 8. STRING COMPARISON
# ------------------------------------------------------------

print("delhi" == "mumbai")

# Strings are compared lexicographically.
# Comparison is based on Unicode/ASCII values of characters.

print("mumbai" > "pune")


# ------------------------------------------------------------
# 9. LOGICAL OPERATORS WITH STRINGS
# ------------------------------------------------------------

# IMPORTANT:
# Empty string "" is considered False.
# Non-empty string is considered True.


# ---------------- AND ----------------

print("hello" and "world")

# "hello" is True
# "world" is also True
# Therefore, the last value is returned.
# Output: world


# ---------------- OR ----------------

print("hello" or "world")

# "hello" is True
# OR stops as soon as it finds a True value.
# Output: hello


# ---------------- EMPTY STRING + AND ----------------

print("" and "hello")

# "" is False
# AND stops at the first False value.
# Output: ""


# ---------------- EMPTY STRING + OR ----------------

print("" or "hello")

# "" is False
# OR checks the next value.
# "hello" is True
# Output: hello


# ------------------------------------------------------------
# 10. LOOPING THROUGH A STRING
# ------------------------------------------------------------

# We can use a for loop to access each character.

for i in "hello":
    print(i)


# Check for a particular character

for i in "hello":
    if i == "h":
        print("kaam karta hai")


for i in "python":
    if i == "y":
        print("y mil gaya")


# ------------------------------------------------------------
# 11. MEMBERSHIP OPERATOR
# ------------------------------------------------------------

# 'in' checks whether a character/string exists.

print("D" in "Delhi")

# Output: True


# ------------------------------------------------------------
# 12. GENERAL STRING FUNCTIONS
# ------------------------------------------------------------

# len()
# Returns the length of the string.

print(len("hello bro"))


# max()
# Returns the character having the highest Unicode/ASCII value.

print(max("hello bro"))


# min()
# Returns the character having the lowest Unicode/ASCII value.

print(min("hello bro"))


# sorted()
# Returns a LIST containing sorted characters.

print(sorted("hello bro"))

# Reverse sorting
print(sorted("hello bro", reverse=True))


# IMPORTANT:
# sorted() returns a LIST, not a string.


# ------------------------------------------------------------
# 13. CHANGING CASE OF A STRING
# ------------------------------------------------------------

s = "new String&&*"


# capitalize()
# Makes the first character uppercase.

print(s.capitalize())


# title()
# Makes the first character of each word uppercase.

print(s.title())


# upper()
# Converts all alphabets to uppercase.

print(s.upper())


# lower()
# Converts all alphabets to lowercase.

print(s.lower())


# swapcase()
# Converts uppercase to lowercase
# and lowercase to uppercase.

print(s.swapcase())

print("hellO".swapcase())


# ------------------------------------------------------------
# 14. COUNTING CHARACTERS
# ------------------------------------------------------------

# count()
# Counts how many times a character/string occurs.

print("hello".count("l"))


# ------------------------------------------------------------
# 15. FINDING A CHARACTER / STRING
# ------------------------------------------------------------

s = "new String&&*"


# index()
# Returns the index of the first occurrence.
# Gives an ERROR if the value is not found.

print(s.index("e"))


# find()
# Returns the index of the first occurrence.
# Returns -1 if the value is not found.

print(s.find("p"))


# ------------------------------------------------------------
# 16. STARTSWITH() AND ENDSWITH()
# ------------------------------------------------------------

# endswith()
# Checks whether the string ends with a particular value.

print(s.endswith("o"))


# startswith()
# Checks whether the string starts with a particular value.

print(s.startswith("h"))


# Both return:
# True / False


# ------------------------------------------------------------
# 17. STRING FORMATTING USING format()
# ------------------------------------------------------------

a = 8
b = 9

print("at beginning {} at last {}".format(a, b))

# Values are inserted into {} according to their order.


# ------------------------------------------------------------
# 18. CHECKING STRING CONTENT
# ------------------------------------------------------------

# isalnum()
# True if all characters are alphabets or numbers.

print("uuu8888".isalnum())


# isalpha()
# True if all characters are alphabets.

print("88888".isalpha())


# isnumeric()
# True if all characters are numeric.

print("8uutu43".isnumeric())


# isidentifier()
# Checks whether the string is a valid Python identifier.

print("1num".isidentifier())


# ------------------------------------------------------------
# 19. SPLIT()
# ------------------------------------------------------------

# split()
# Breaks a string into a LIST.

# If nothing is passed:
# String is split based on whitespace.

print("hii my name is priyanshu patel".split())


# We can also specify the separator.

print("hii my name is priyanshu patel".split("i"))

# IMPORTANT:
# split() returns a LIST.


# ------------------------------------------------------------
# 20. JOIN()
# ------------------------------------------------------------

# join()
# Joins elements of a list/string using the given separator.

print("-".join([
    "hii",
    "my",
    "name",
    "is",
    "priyanshu",
    "patel"
]))

# Output:
# hii-my-name-is-priyanshu-patel


# ------------------------------------------------------------
# 21. REPLACE()
# ------------------------------------------------------------

# replace()
# Replaces one part of a string with another.

print("hii my name is priyanshu patel".replace("priyanshu", "sonu"))


# ------------------------------------------------------------
# 22. STRIP()
# ------------------------------------------------------------

# strip()
# Removes unwanted whitespace from BOTH ends of a string.

print("          hello            ".strip())

# Output:
# hello

# IMPORTANT:
# strip() does NOT remove spaces from the middle.

# Example:
# "hello     bro".strip()
# Result:
# "hello     bro"


# ------------------------------------------------------------
#                    END OF STRINGS
# ------------------------------------------------------------