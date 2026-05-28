
# A list = ordered, mutable, allows duplicates.

arr = [10, 20, 30, 40]

# c = list("python")     # ['p','y','t','h','o','n']

# print(c)

# arr.append([5,10])
# print(arr)

# arr.extend([85,69,10])
# print(arr)

# arr[4].insert(1,200)
# print(arr)

# arr.pop()
# print(arr) //  deletee last element of list

# arr.pop(1) // delete element at index position
# print(arr)


# arr.remove(10) // finds that element and ten delete it
# print(arr)


# nums = [4,2,8,1]

# len(nums)      # 4
# max(nums)      # 8
# min(nums)      # 1
# sum(nums)      # 15
# sorted(nums)   # [1,2,4,8]



# nums = [10,20,30]

# 20 in nums        # True
# nums.index(30)    # 2
# nums.count(10)    # 1


# nums = [1,2,3,4]

# sq = [x*x for x in nums]
# # [1,4,9,16]


# even = [x for x in nums if x%2==0]
# # [2,4]


# arr = [4,1,7,2]

# arr.sort()                 # ascending
# arr.sort(reverse=True)     # descending


# words = ["apple","kiwi","banana"]

# words.sort(key=len)
# # ['kiwi','apple','banana']


# 15. Time Complexity Gold
# append() = O(1) avg
# pop() end = O(1)
# insert front = O(n)
# search = O(n)
# sort = O(n log n)


# Interviewers ask this.
# -----------------------


# Coding Practice Set

# Easy

# Find sum of [1,2,3,4,5]
# Reverse [10,20,30]
# Find max element

# Medium

# Remove duplicates from [1,2,2,3,1,4]
# Find second largest in [10,5,8,20,15]
# Count even numbers in list

# Hard

# Rotate list right by 2
# Input: [1,2,3,4,5]
# Output: [4,5,1,2,3]

# Move all zeros to end
# Input: [0,1,0,3,12]

# Find missing number from [1,2,4,5]