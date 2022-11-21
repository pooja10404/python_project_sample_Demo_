
# Search function with parameter list name
# and the value to be searched

def search(List, n):

	for i in range(len(List)):
		if List[i] == n:
			return True
	return False


# list which contains both string and numbers.
List = [1, 2, 'sachin', 4, 'Geeks', 6]

# Driver Code
n = 'Geeks'

if search(List, n):
	print("Found")
else:
	print("Not Found")

#remove element from the list
# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]

# remove 9 from the list
prime_numbers.remove(9)


# Updated prime_numbers List
print('Updated List: ', prime_numbers)

# Output: Updated List:  [2, 3, 5, 7, 11]

