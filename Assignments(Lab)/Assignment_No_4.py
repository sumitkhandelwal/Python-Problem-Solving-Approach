a = []
n = int(input("Enter the total number subject (Ex : 5) : "))
flag = 0
for i in range(n):
    element = int(input("Enter the marks of student : "))
    a.append(element)
    if(element < 40):
        print ("Student is fail in exam")
        flag = 1
        break
sum1 = 0
if(flag == 0):
    print ("Marks of Each Subject is  :",a)
    for i in range(n):
        sum1 = sum1 + a[i]
        agg = sum1 / n
    if(agg >= 75):
        print ("Your Grade is : Distinction")
    elif(agg < 75 and agg >= 60):
        print ("Your Grade is : First Class")
    elif(agg < 60 and agg >= 50):
        print ("Your Grade is : Second Class")
    else:
        print ("Your Grade is : Third Class")

