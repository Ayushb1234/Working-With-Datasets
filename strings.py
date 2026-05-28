# # strings  = sequence of characters

# name = "Ayush"

# print(type(name))

# # --------------------
# # Accessing characters using indexing

# s = "python"

# print(s[0])
# print(s[2])
# print(s[-1])
# print(s[-2])

# --------------------

# slicing

# print(s[0:3])
# print(s[3:])
# print(s[:4])
# # print(s[::-1]) // reverse a string

# # --------------------
# # lower and uppercase

# print(s.lower())
# print(s.upper())

# strip spaces
# --------------

# str = " hello Ayush "

# print(str.strip())

# ------------------

# replace

# s = "I like Java"

# print(s.replace("Java","Python"))

# ---------------------------------

# Split

# sx = "a,b,c,d"

# print(sx.split(","))

# ------------------

# arr = ['a','b','c','d']

# print("-".join(arr))

# # Count
# # -------

# x = "banana"

# print(x.count("a"))

# -------------------

# Find
# ------------------

# y = "python"

# print(y.find("t"))
# print(y.find("x"))

# -----------------------

# s = "resume.pdf"

# # print(s.endswith(".pdf")) // check if string ends with .pdf
# print(s.startswith("xyz"))

# -------------------------- strings are immutable

# s = "hello"

# s[0] = "H"

# print("H" + s[1:])



# for i in s:
#     print(i)
    
# memberhip operator
# ----------------------

# s = "python"

# print("py" in s)     
# print("java" in s)    

# F - Strings
# -------------------
# benefit of f strings is that it allows us to embed expressions inside string literals, using curly braces {}. This makes it easier to format strings and include variable values directly within the string.


# name = "Ayush"
# age = 22

# print(f"My name is {name} and age is {age}")
# print("My name is",name,"and age is",age)

# reverse a string
# -------------------

# s = "Elytespark"

# print(s[::-1])

# # Palindrome
# # -------------

# str = "madam"

# print(str == str[::-1])


# # count vowels
# # ---------------

# count = 0

# for ch in s:
#     # count uppercase/lowercase characters

#     if ch.islower():
#         count += 1
# print(count)

# # reverse words

# x = "I love python"

# # python love I i want this is my output

# ans  = x.split()[::-1]
# print(" ".join(ans))

# # first non -repeating charcater

# input  = "aabbcddee"

# for ch in input:
#     if input.count(ch) == 1:
#         print(ch)
#         break
    
# -------------------

m = "listen"
n = "silent"

if sorted(m) == sorted(n):
    print("true")
else:    
    print("false")
    
    
    