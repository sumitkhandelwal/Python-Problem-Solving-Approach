'''Write a python program that accepts a string from user and perform following string operations-
i. Calculate length of string
ii. String reversal
iii. Equality check of two strings
iii. Check palindrome
ii. Check substring
'''
str1 = raw_input("Enter any string : ")
# Calculate the length of a string is
length = len(str1)
print ("Length of Given String is :", length)
# String Reverse
rev = ""
for i in range(length-1,-1,-1):
    rev = rev + str1[i]
print ("Reverse String of a given string is : ", rev)
# Check Equality
str2 = raw_input("Enter another string : ")
if(str1 == str2):
    print ("Both string is same.")
else:
    print ("Both string is not same.")
# Check Palindrome
if(str1 == rev):
    print ("Your First String is Palindrome.")
else:
    print ("Your First String is not Palindrome.")
# Substring
sub_str1 = raw_input("Enter the substring of first string :")
s = (str1.find(sub_str1))
if(s == -1):
    print (sub_str1, "String is not a part of your first String.")
else:
    print (sub_str1, "String is a part of your first String.")
    

