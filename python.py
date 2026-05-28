import numpy as np
import time

a = [1,2,3,4,5,6] * 100000
start = time.time()
for i in range(len(a)):
    a[i] = a[i] * 3
print("\n time taken for list:",time.time()-start)


# Vectorization - It is a process of converting all the available data into array and with the help of it  we can perform operations on entire array at once, here we can perform operations without loops as well.add()

# concatination - merging two strings or values together.

# vstack and hstack - vstack is used to stack arrays in vertical direction and hstack is used to stack arrays in horizontal direction.

# dtype - it is used to specify the type of data that we want to store in an array.

# astype - it is used to convert the data type of an array to another data type.


arr = np.array(a)
new_arr = arr.astype(np.int64)
print(new_arr.dtype)


arr = np.array([10,240,50])
result = np.where(arr>20,"pass","fail") 
print(result)

a= np.array([1,2,3,4,5,6])
reshaped_arr = a.reshape(2,3)
print(reshaped_arr)

# Write a program for an employee for his details employee_id,name,salary,ep,etc and the condition is if a particular employee has ep of 5 yrs he will receive salary and bonus of 5 or 2 % .


# Pandas -> It is a library in python that is used for data manipulation and analysis. It provides data structures like Series and DataFrame which are very useful for handling and analyzing data.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
