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
#prints the attribute name of the object s  
print(getattr(per_1,'name'))  
# reset the value of attribute age to 23  
setattr(per_1,"age",23)  
# prints the modified value of age  
print(getattr(per_1,'age'))  
# prints true if the Person contains the attribute with salary 
print(hasattr(per_1,'salary'))  
# deletes the attribute age  
delattr(per_1,'age')  
	  
