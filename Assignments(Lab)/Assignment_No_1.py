'''To calculate salary of an employee given his basic pay (take as input from user).
Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of basic pay.
Let employee pay professional tax as 2% of total salary. Calculate net salary payable after deductions.
'''
basicpay = float(input("Enter the basic pay of an employee : "))
hra = (basicpay * 10)/ 100
ta = (basicpay * 5)/ 100
pt =(basicpay * 2)/ 100

grosssalary = basicpay + hra + ta + pt

print ("Gross Salary of an Employee is : ", grosssalary)
