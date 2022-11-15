# Creating a Dictionary
# with Integer Keys
from filecmp import cmp

Dict1 = {1: 'Geeks', 2: 'for', 3: 'Geeks'}
print(Dict1)
# output :- {1: 'Geeks', 2: 'for', 3: 'Geeks'}
print("-------------------------------------")
# Creating a Dictionary
# with Mixed keys
Dict2 = {'Name': 'Geeks', 1: [1, 2, 3, 4, 5]}
print(Dict2)
# output :- {'Name': 'Geeks', 1: [1, 2, 3, 4, 5]}
print("----------------------------------------")
# Creating a Dictionary
# with each item as a Pair
Dict4 = dict([(1, 'Geeks'), (2, 'For')])
print(Dict4)
# output :- {1: 'Geeks', 2: 'For'}
print("----------------------------------------")
# Creating a Dictionary
# with dict() method
Dict5 = dict({1: 'Geeks', 2: 'for', 3: 'Geeks'})
print(Dict5)
# output :- {1: 'Geeks', 2: 'for', 3: 'Geeks'}
print("--------------------------------------")
# Creating a Nested Dictionary
# as shown in the below image
Dict6 = {1: 'shivam', 2: 'rohit', 3: 'shubham', 4: {'A': 'To', 'B': 'The', 'C': 'New'}}
print(Dict6)
# output :- {1: 'shivam', 2: 'rohit', 3: 'shubham', 4: {'A': 'To', 'B': 'The', 'C': 'New'}}
print("--------------------------------------")
# accessing a element using key
print("Accessing a element using key:")
print(Dict6[1])
# output :- Accessing a element using key:
# shivam
print("--------------------------------------")
# accessing a element using get() method
# method
print("Accessing a element using get:")
print(Dict6.get(3))
# output:- Accessing a element using get:
# shubham
print("--------------------------------------")
# The clear() method removes all items from the dictionary
D = {7: 'name', 8: 'is', 9: 'shivam'}
D.clear()
print(D)
# output:- {}
print("--------------------------------------")
# copy() method
original = {1: 'move', 2: 'To', 3: 'element'}
new = original.copy()
print(new)
# output :- {1: 'move', 2: 'To', 3: 'element'}
print("--------------------------------------")
# items() method
# Dictionary with three items
Dictionary1 = {'A': 'Geeks', 'B': 4, 'C': 'Geeks'}

print("Dictionary items:")

# Printing all the items of the Dictionary
print(Dictionary1.items())
# output :- Dictionary items:
# dict_items([('A', 'Geeks'), ('B', 4), ('C', 'Geeks')])
print("--------------------------------------")
# keys() method
Dictionary2 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
# Printing keys of dictionary
print(Dictionary2.keys())
# output:- dict_keys(['A', 'B', 'C'])
print("--------------------------------------")
# pop() method
# working of pop()
# initializing dictionary
test_dict = {"Nikhil": 7, "Akshat": 1, "Akash": 2}

# Printing initial dict
print("The dictionary before deletion : " + str(test_dict))

# using pop to return and remove key-value pair.
pop_ele = test_dict.pop('Akash')

# Printing the value associated to popped key
print("Value associated to popped key is : " + str(pop_ele))

# Printing dictionary after deletion
print("Dictionary after deletion is : " + str(test_dict))
# output :- The dictionary before deletion : {'Nikhil': 7, 'Akshat': 1, 'Akash': 2}
# Value associated to popped key is : 2
# Dictionary after deletion is : {'Nikhil': 7, 'Akshat': 1}
print("--------------------------------------")
# popitem() Method
d = {1: '001', 2: '010', 3: '011'}
print(d.popitem())
# output :- (3, '011')
print("--------------------------------------")
# update() method
# Dictionary with three items
Dictionary4 = {'A': 'Geeks', 'B': 'For', }
Dictionary5 = {'B': 'Geeks'}

# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary4)

# update the value of key 'B'
Dictionary4.update(Dictionary5)
print("Dictionary after updation:")
print(Dictionary4)
# output :- Original Dictionary:
# {'A': 'Geeks', 'B': 'For'}
# Dictionary after updation:
# {'A': 'Geeks', 'B': 'Geeks'}
print("--------------------------------------")
# values() method
dictionary3 = {"raj": 2, "striver": 3, "vikram": 4}
print(dictionary3.values())

# string values
dictionary6 = {"geeks": "5", "for": "3", "Geeks": "5"}
print(dictionary6.values())
# output:- dict_values([2, 3, 4])
# dict_values(['5', '3', '5'])
print("--------------------------------------")

