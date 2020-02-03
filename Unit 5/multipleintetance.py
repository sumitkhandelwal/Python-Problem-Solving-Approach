class Per_Details1:  
    def __init__(self):  
        self.name = 'Sumit'  
        self.age = 23 
  
    def getName(self):  
        return self.name  
  
  
class Per_Details2:  
    def __init__(self):  
        self.name = 'Ashwini'  
        self.id = '30'  
  
    def getName(self):  
        return self.name  
  
  
class Person(Per_Details1, Per_Details2):  
    def __init__(self):  
        Per_Details1.__init__(self)  
        Per_Details2.__init__(self)  
  
    def getName(self):  
        return self.name  
  
per_info = Person()  
print(per_info.getName())  
