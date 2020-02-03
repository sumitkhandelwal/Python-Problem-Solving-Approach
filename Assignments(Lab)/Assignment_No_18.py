# class definition
class Employee(object):
     """__init__() functions as the class constructor"""
     def __init__(self, name=None, dest=None, gender=None, date=None,salary=None):
         self.name = name
         self.dest = dest
         self.gender = gender
         self.date = date
         self.salary = salary
empList = []
empList.append(Employee('Sumit','Asst_Manager','M','28/08','50000'))
empList.append(Employee('Ashwini','CLO','F','28/08','50000'))
empList.append(Employee('Vinod','Developer','M','28/08','5000'))
empList.append(Employee('Kalyan','Tester','F','28/08','5000'))
empList.append(Employee('Pratik','Programmer','M','28/08','50000'))

'''
User Define Code (Optional)
n = int(input("Enter the count of an employee :"))
for i in range(n):
  
    name = str(input("Enter Name of Employee :"))
    dest = str(input("Enter Destination of Employee :"))
    gender = str(input("Enter Gender of Employee(M/F):"))
    date = str(input("Enter DOJ of Employee :"))
    salary = str(input("Enter Salary of Employee :"))
   
    empList.append(Employee(name,dest,gender,date,salary))
'''

print ("Show one particular item:")
for i in range(len(empList)):
    print ("Name :", empList[i].name)
    print ("Dest :", empList[i].dest)
    print ("Gender :", empList[i].gender)
    print ("DOJ :", empList[i].date)
    print ("Salary :", empList[i].salary )
    print ("----------------------------------------------------------")
#total number of employees in an organization
def compute():
    count = len(empList)
    print ("Total Number of Employee in an organization :",count)

compute()
#count of male and female employee 
male = []
female = []
for i in range(len(empList)):
    if(empList[i].gender == 'M'):
        male.append(empList[i].name)
    else:
        female.append(empList[i].name)
def count_gender():
    print ("Total Number of Male Employee is :", len(male))
    print ("Total Number of Male Employee is :",len(female))
print ("----------------------------------------------------------")
count_gender()
print ("----------------------------------------------------------")
#Employee with salary more than 10,000
def salary_more_than_10k():
    count = 0
    for i in range(len(empList)):
        if(int(empList[i].salary) > 10000):
            count = count + 1
    print ("Employee with salary more than 10,000:",count)
salary_more_than_10k()
# Employee with designation "Asst Manager" 
asst_manager = []
n = len(empList)
def Asst_Manager():
    count = 0
    for i in range(n):
        if((empList[i].dest) == "Asst_Manager"):
            asst_manager.append(empList[i].name)
    print ("Employee with designation Asst Managers are :")
    print (asst_manager) 
Asst_Manager()
