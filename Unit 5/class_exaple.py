class Person:
  def __init__(self, name, age,salary):
    self.name = name
    self.age = age
    self.salary = salary

  def myfunction(self):
    print("Hello my name is " , self.name , "and age is :",self.age)
    print ("My Salary is :", self.salary)

p = Person("Sumit", 30, 23000)
p. myfunction()
