class Person:
  def __init__(self, name, age,salary):
    self.name = name
    self.age = age
    self.salary = salary

  def myfunction(self):
    print("Hello my name is " , self.name , "and age is :",self.age)
    print ("My Salary is :", self.salary)
# First Person information
per_1 = Person("Sumit", 30, 23000)
per_1. myfunction()
print(per_1.__doc__)  
print(per_1.__dict__)  
print(per_1.__module__)  
