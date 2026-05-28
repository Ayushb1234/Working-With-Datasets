# MODULE 5: DICTIONARIES (Most Powerful Python DS)

# A dictionary stores data in key : value pairs.

# d = {"name": "Ayush", "age": 22}

# Use cases:

# Frequency counting
# Hash maps
# Fast lookup O(1)
# Caching
# Grouping data
# JSON/API handling
# 1. Create Dictionary
# d1 = {}
# d2 = {"a": 1, "b": 2}
# d3 = dict(name="Ayush", age=22)
# 2. Access Values
# d = {"name":"Ayush", "age":22}

# print(d["name"])      # Ayush

# ⚠️ Missing key gives error.

# Safer:

# print(d.get("salary"))      # None
# print(d.get("salary", 0))   # 0
# 3. Add / Update
# d = {"a":1}

# d["b"] = 2
# d["a"] = 99

# print(d)
# # {'a':99, 'b':2}
# 4. Remove Items
# pop()
# d = {"a":1,"b":2}

# d.pop("a")
# del
# del d["b"]
# clear()
# d.clear()
# 5. Looping
# d = {"a":1,"b":2}

# for key in d:
#     print(key)

# for key,val in d.items():
#     print(key,val)
# 6. Important Methods
# keys()
# d.keys()
# values()
# d.values()
# items()
# d.items()
# 7. Membership
# d = {"a":1,"b":2}

# print("a" in d)   # True

# Checks keys.

# 8. Frequency Count (Interview Gold)
# s = "banana"

# freq = {}

# for ch in s:
#     freq[ch] = freq.get(ch,0) + 1

# print(freq)

# Output:

# {'b':1,'a':3,'n':2}
# 9. Using Counter (Advanced Shortcut)
# from collections import Counter

# print(Counter("banana"))
# 10. Nested Dictionary
# student = {
#     "name":"Ayush",
#     "marks":{"math":90,"python":100}
# }

# print(student["marks"]["python"])
# 11. Dictionary Comprehension
# sq = {x:x*x for x in range(5)}

# print(sq)

# Output:

# {0:0,1:1,2:4,3:9,4:16}
# 12. Merge Dictionaries
# a = {"x":1}
# b = {"y":2}

# c = a | b
# print(c)
# 13. Sorting Dictionary
# d = {"a":3,"b":1,"c":2}

# print(sorted(d.items(), key=lambda x:x[1]))

# Sort by values.

# 14. Interview Patterns
# First Non-Repeating Character
# s = "aabbcdde"

# freq = {}

# for ch in s:
#     freq[ch] = freq.get(ch,0)+1

# for ch in s:
#     if freq[ch] == 1:
#         print(ch)
#         break
# Two Sum
# nums = [2,7,11,15]
# target = 9

# mp = {}

# for i,n in enumerate(nums):
#     if target-n in mp:
#         print(mp[target-n], i)
#     mp[n] = i
# Group Words by Length
# words = ["hi","cat","go","apple"]

# d = {}

# for w in words:
#     d.setdefault(len(w), []).append(w)

# print(d)
# 15. Time Complexity
# get/set = O(1) avg
# delete = O(1) avg
# search key = O(1) avg

# Python interviewers love this.

# Practice Set
# Easy
# Create dict with name, age
# Print value of key "name"
# Add city key
# Medium
# Count frequency of numbers in [1,2,1,3,2,1]
# Find max value key in dict
# Merge two dicts
# Hard
# First unique character in string
# Two Sum problem using dict
# Group anagrams using dict