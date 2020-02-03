class Person:
    age = 30
    name = "Sumit"  
data = Person()  
print('The age is:', getattr(data, "age"))  
print('The age is:', data.age)
print('The name is:', getattr(data, "name"))  
print('The name is:', data.name)

