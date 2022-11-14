# Create a set
thisset = {"apple", "banana", "cherry"}
print("create a set : ", thisset)  #{'banana','cherry' ,'apple'}

# Duplicates Not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print("Duplicate Set is not allowed: ", thisset) #{'banana', 'cherry', 'apple'}

# Get a length of set
thisset = {"apple", "banana", "cherry"}
print("Get a length of set: ", (len(thisset))) # 3

# Set of Items
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print("set of fruits name: ", set1) #{'banana', 'cherry', 'apple'}
print("set of variable name: ", set2) # {1, 3, 5, 7, 9}
print("set of Boolean value: ", set3) # {False, True}

# Set contain different data type
set1 = {"abc", 34, True, 40, "male"}
print("Set contain different data type:", set1) #{True, 34, 40, 'male', 'abc'}

# Data Type of set
myset = {"apple", "banana", "cherry"}
print("Data Type of set:", (type(myset))) #<class 'set'>

# Set constructor
thisset = set(("apple", "banana", "cherry"))
print("Set of constructor", thisset) # {'cherry', 'banana', 'apple'}
