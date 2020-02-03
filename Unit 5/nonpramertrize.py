class Person:
  def __init__(self):
    print("Output Using Non Parametrized construtor")

  def myfunction(self, name,age, salary):
    print("Hello my name is " , name ," and age is :", age)
    print ("My Salary is :", salary)
# First Person information
per_1 = Person()
per_1.myfunction("Sumit",30,23000)
