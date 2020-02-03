a = []
n = int(input("Enter the total number of elements in a series : "))
for i in range(n):
    element = int(input("Enter the elements : "))
    a.append(element)
print ("Elements in a series is :",a)
# Maximum Number
print ("Maximum number in a list is :",max(a))
# Minimum Number
print ("Maximum number in a list is :",min(a))
# Sum of a number in a list is
sum1 = 0
for i in range(len(a)):
    sum1 = sum1 + a[i]
print ("Sum of all number in a list is : ", sum1)
# Average of a number in a list
average = sum1 / len(a)
print ("Average of all; Number in a list is :", average)
