# Smallest divisor
n=int(input("Enter an integer to find out its Smallest divisor:"))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("Smallest divisor is : ",a[0])
print("---------------------------------------------------")
# Greatest common divisor
x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
gcd = 1
if x % y == 0:
    print(y)
for k in range(int(y / 2), 0, -1):
    if x % k == 0 and y % k == 0:
        gcd = k
        break
print ("Greatest common divisor : ",gcd)
