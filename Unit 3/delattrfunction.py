class Student:  
    id = 101  
    name = "Pranshu"  
    email = "pranshu@abc.com"  
# Declaring function  
    def getinfo(self):  
        print(self.id, self.name, self.email)  
s = Student()  
s.getinfo()  
delattr(Student,name) # Removing attribute which is not available  
s.getinfo() # error: throws an error  
