class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
   

  def myfunction(self):
    print("Hello my name is " , self.name , "and age is :",self.age)
 

p = Person("Sumit", 30)
p. myfunction()
