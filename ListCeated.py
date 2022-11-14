#creating a list in that
employee=["shubham",1,"India"]
department=["Mca",1,"India"]
print("employee data are:")
print("name is %s,ID :%d,Country is %s"%(employee[0],employee[1],employee[2]))
print("department are %s,dep:%d,country:%s"%(department[0],department[1],department[2]))


listcollect=[1,2,3,4,5,6]
print(listcollect[0])
print(listcollect[1])
print(listcollect[2])
print(listcollect[3])

#slicing the elements its print the element from the 0 to the fixed value ex-(0:6)
print(listcollect[0:6])

# By default the index value is 0 so its starts from the 0th element and go for index -1.
print(listcollect[:])
print(listcollect[2:5])
print(listcollect[1:6:2])

#list indexing in forward or backward indexing
listdefault=[0,1,92,3,4,5,6]
print(listdefault[1])
print(listdefault[-1])
print(listdefault[-3:-1])

#list where we update the list on the
listupdate=[1,2,3,4,5,6]
print(listupdate)
# It will assign value to the value to second index
listupdate[2]=10
print(listupdate)
#adding mutliple element
listupdate[1:3]=[89,87]
print(listupdate)
# It will add value at the end of the list
listupdate[-1]=25
print(listupdate)

#concatenation and repitation
listconcatL1=[1,2,3,4]
listconconcatL2=[6,7,8,9]
#on the listconcatL1 (*) star here we used for repitation for our list
print(listconcatL1*2)
#here (+) plus sign used for concatenation for our list
listconcatL1+listconconcatL2
print(listconcatL1+listconconcatL2)
# membership chek the element present in the list our not It returns true if a particular item exists in a particular list otherwise false.
print(2 in listconcatL1)
# Iteration the list The for loop is used to iterate over the list elements.
for i in listconcatL1:
    print(i)
#length of your list
len(listconcatL1)

#print the max element
print(max(listconcatL1))


#there is a list of names
namelist=["john","davic","james","jonathan"]

for i in namelist:
    print(i)

#append() the append() function can only add value to the end of the list.
#Declaring the empty list
l=[]
#Number of elements will be entered by the user
n = int(input("Enter the number of elements in the list:"))
# for loop to take the input
for i in range(0,n):
    # The input is taken from the user and added to the list as the item
    l.append(input("Enter the item:"))
print("printing the list items..")
# traversal loop to print the list items
for i in l:
    print(i, end = "  ")


#Removing elements from the list
#the remove() function which is used to remove the element from the list.
listrem = [0,1,2,3,4]
print("printing original list: ");
for i in listrem:
    print(i)
listrem.remove(2)
print("\nprinting the list after the removal of first element...")
for i in listrem:
    print(i)