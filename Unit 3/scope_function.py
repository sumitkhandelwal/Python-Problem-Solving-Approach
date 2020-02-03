def addition(*args):
    sum1=0
    for arg in args:
        sum1 = sum1 +arg
    print("Value After Addition is (Inside the function) : ",sum1)
sum1 = 0  
addition(20,40,60) #60 will be printed as the sum  
print("Value After Addition is (outside the function):",sum1) 
