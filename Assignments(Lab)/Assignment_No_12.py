a = []
n = int(input("Enter the count of elements in a list : "))
for i in range(n):
    element = int(input("Enter an element in a list : "))
    a.append(element)
print ("Your Given list is : ", a)
even = []
odd = []
for i in range(len(a)):
    if(a[i]%2 == 0):
        even.append(a[i])
    else:
        odd.append(a[i])
print ("Even number list is :", even)
print ("Odd number list is :", odd)
