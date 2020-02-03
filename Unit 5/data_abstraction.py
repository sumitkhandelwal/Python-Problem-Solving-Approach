class Person:  
    count = 0;  
    def __init__(self):  
        Person.count = Person.count+1  
    def display(self):  
        print("The number of Person",Person.count)  
p1 = Person()  
p2 = Person()
# Display the data using one object
p1.display()  
