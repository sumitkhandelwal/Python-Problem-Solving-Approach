print("Decimal to Binary Conversion :")
def convertToBinary(n):
# Function to print binary number for the input decimal using recursion
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')
# decimal number
print ("--------------------------------------------------------")
dec = int(input("Enter any Decimal Number : "))
print ("Binary Equivalent of your Number is :")
convertToBinary(dec)
print ()
print ("--------------------------------------------------------")
print("Binary to Decimal Conversion :")
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print("Decimal Equivalent of your Number is :", decimal)
binary = int(input("Enter any Binary Number : "))
binaryToDecimal(binary)

