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
print("------------------------------------------------")
# Second Person information
per_2 = Person("Ashwini", 29, 20000)
per_2. myfunction()
