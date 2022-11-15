print("--------------------------------------------------------------------")
# Create Empty Tuple
print("Create Empty Tuple")
emptyTuple = ()
# It will print type of variable
print(type(emptyTuple))
# output : <class 'tuple'>
print("--------------------------------------------------------------------")

# Create tuple With Items
print("Create tuple With Items")
tupleWithItems = ("apple", "banana", "cherry", "orange")
print(tupleWithItems)
# output : ('apple', 'banana', 'cherry', 'orange')

print("--------------------------------------------------------------------")

# Tuple items can be of any data type
print("Tuple items can be of any data type")
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
# output :
# <class 'tuple'>
# <class 'tuple'>
# <class 'tuple'>
print("--------------------------------------------------------------------")
# Len Function for Tuple

print("len() Function for Tuple")
tupleLen = (22, 45, 23, 78, 6.89)

# Convert integer into string and in store variable
length = str(len(tupleLen))
print("Length of Tuple " + length)
# output : Length of Tuple 5

print("--------------------------------------------------------------------")

# count() Function for Tuple
print("count() Function for Tuple")
tupleCount = (22, 45, 23, 78, 45, 6.89, 52, 69, 45, 23)

# count() function count the number of times an element is present in the tuple.
count = str(tupleCount.count(45))
print("Count of 45 in tuple5 is:- " + count)
# output : Count of 45 in tuple5 is:- 3

print("--------------------------------------------------------------------")

print("sort() Function for Tuple")
# sort() Function for Tuple
tupleSort = (22, 45, 23, 78, 45, 6.89, 52, 69, 45, 23)

# sorted() function sort element is present in the tuple.
sort = str(sorted(tupleSort))
unsortTuple = str(tupleSort)
print("Tuple Before Sorted :- " + unsortTuple)
print("Tuple After Sorted :-" + sort)

# output :
# Tuple Before Sorted :- (22, 45, 23, 78, 45, 6.89, 52, 69, 45, 23)
# Tuple After Sorted :-[6.89, 22, 23, 23, 45, 45, 45, 52, 69, 78]

print("--------------------------------------------------------------------")

# max() Function for Tuple

print("max() Function for Tuple")
tupleMax = (22, 45, 23, 78, 45, 6.89, 52, 69, 45, 23)

# max() function find maximum element is present in the tuple.
maxValue = str(max(tupleMax))
print("Maximum element is present in the tuple is :- " + maxValue)
# output : Maximum element is present in the tuple is :- 78

print("--------------------------------------------------------------------")

# min() Function for Tuple

print("min() Function for Tuple")
tupleMin = (22, 45, 23, 78, 45, 6.89, 52, 69, 45, 23)

# min() function find maximum element is present in the tuple.
minValue = str(min(tupleMin))
print("Minimum element is present in the tuple is :- " + minValue)

# output : Minimum element is present in the tuple is :- 6.89

print("--------------------------------------------------------------------")

print("sum() Function for Tuple")

# sum() Function for Tuple
tupleSum = (22, 45, 23, 78, 45, 6.89, 52, 69, 45, 23)

# sum() function find maximum element is present in the tuple.
sumValue = str(sum(tupleSum))
print("Sum of elements is present in the tuple is :- " + sumValue)

# output : Sum of elements is present in the tuple is :- 408.89

print("--------------------------------------------------------------------")

# MemberShip in tuple
# We can apply the ‘in’ and ‘not in’ operators on items. This tells us whether they belong to the tuple.
# sum() Function for Tuple

print("MemberShip in tuple")
tupleMember = (22, 45, 23, 78, 45, 6.89, 52, 69, 45, 23)

# in function tells us whether they belong to the tuple.
inValue = 22 in tuple(tupleMember)
invalue = 26 in tuple(tupleMember)
print(inValue)
print(invalue)

# Output :
# True
# False

print("--------------------------------------------------------------------")

# in function tells us whether they belong to the tuple.
notInValue = 22 not in tuple(tupleMember)
notinValue = 26 not in tuple(tupleMember)

print(notInValue)
print(notinValue)

# Output :
# False
# True
print("--------------------------------------------------------------------")

# Concatenation of tuple
print("Concatenation of tuple")
tupleConcatOne = (22, 45, 23, 78, 45, 6.89, 52, 69, 45, 23)
tupleConcatSecond = (25, 65, 78, 94, 12, 14, 86, 52, 51, 86, 64, 163, 504, 68, 16)

# + is used for concatenation of two tuple
concatenationTuple = tupleConcatOne + tupleConcatSecond

print(concatenationTuple)

# Output: (22, 45, 23, 78, 45, 6.89, 52, 69, 45, 23, 25, 65, 78, 94, 12, 14, 86, 52, 51, 86, 64, 163, 504, 68, 16)

print("--------------------------------------------------------------------")

# Iterating on a Python Tuple
print("Iterating on a Python Tuple")

for i in tupleConcatSecond:
    print(i)

# Output :
# 25
# 65
# 78
# 94
# 12
# 14
# 86
# 52
# 51
# 86
# 64
# 163
# 504
# 68
# 16

print("--------------------------------------------------------------------")

# Python3 code to demonstrate working of
# Tuple multiplication
# using zip() + generator expression
print("Tuple multiplication")
# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple multiplication
# using zip() + generator expression
res = tuple(ele1 * ele2 for ele1, ele2 in zip(test_tup1, test_tup2))

# printing result
print("The multiplied tuple : " + str(res))

# Output :
# The original tuple 1 : (10, 4, 5, 6)
# The original tuple 2 : (5, 6, 7, 5)
# The multiplied tuple : (50, 24, 35, 30)


print("--------------------------------------------------------------------")

print("Tuple Slicing")

tupSlice = (22, 3, 45, 4, 2.4, 2, 56, 890, 1)

# prints 2nd to 4th element
print("prints 2nd to 4th element")
print(tupSlice[1:4])

# Output:
# prints 2nd to 4th element
# (3, 45, 4)

# prints 1st to 4th element
print("prints 1st to 4th element")
print(tupSlice[:4])

# Output :
# prints 1st to 4th element
# (22, 3, 45, 4)

# prints 5th to the last element
print("prints 5th to the last element")
print(tupSlice[4:])

# Output:
# prints 5th to the last element
# (2.4, 2, 56, 890, 1)

# prints first to the last element
print("prints first to the last element")
print(tupSlice[:])

# Output:
# prints first to the last element
# (22, 3, 45, 4, 2.4, 2, 56, 890, 1)

# prints first to the last element with a step of 2 i.e. printing the alternate elements
print("prints first to the last element with a step of 2 i.e. printing the alternate elements")
print(tupSlice[::2])
# Output :
# prints first to the last element with a step of 2 i.e. printing the alternate elements
# (22, 45, 2.4, 56, 1)

# prints the fourth element from the last
print("prints the fourth element from the last")
print(tupSlice[-4])

# Output :
# prints the fourth element from the last
# 2

# prints elements from last fourth to last first
print("prints elements from last fourth to last first")
print(tupSlice[-4:-1])

# Output
# prints elements from last fourth to last first
# (2, 56, 890

print("--------------------------------------------------------------------")


