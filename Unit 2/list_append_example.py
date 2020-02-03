# Use of append() method
n = int(input("Enter the size of a list :"))
a = []
for i in range(n):
    element = int(input("Enter the values :"))
    a.append(element)
print ("Array is :")
for i in a: # traversal loop to print the list items
    print(i, end = "  ");   

