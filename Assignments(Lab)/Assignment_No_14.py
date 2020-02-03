n  = int(input("How many values in series do you want to print : "))
x0 = 0 
x1 = 1 
counter = 2  
if (n ==1): 
    print "My Fibbonacci Series is :\n", x0
if (n ==2): 
    print "My Fibbonacci Series is :\n", x0,"\n",x1
if (n > 2): 
    print "My Fibbonacci Series is : \n", x0,"\n",x1
while(counter < n): 
    xth = x0 + x1 
    print xth 
    x0 = x1 
    x1 = xth 
    counter = counter + 1 

# Output

#How many values in series do you want to print : 5
#My Fibbonacci Series is : 
#0 
#1
#1
#2
#3
5
