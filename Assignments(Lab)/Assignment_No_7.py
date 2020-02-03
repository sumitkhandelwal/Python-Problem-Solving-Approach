import math
n = int(input("Enter any number : "))
print("Sqaure Root of Number is : ",math.sqrt(n))
print("Sqaure of Number is : ",math.pow(n,2))
print("Cube of Number is : ",math.pow(n,3))
# Check Given No is Prime or Not Prime Number
flag = 0 # Prime
for i in range(2,n//2):
    if(n%i == 0):
        flag = 1 # not Prime
        break
if(flag == 0):
    print("Given Number is Prime")
else:
    print("Given Number is Not Prime")
# Factorial of a number 
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("Factorial of Given Number is :", fact)
# Prime Factor
print("Prime Factor of a Given Number is : ")
while n % 2 == 0:
    print (2) 
    n = n / 2
for i in range(3,int(math.sqrt(n))+1,2): 
    while n % i== 0:
        print (i) 
        n = n / i 
if n > 2: 
    print (n) 
