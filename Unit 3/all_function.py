# all values true  
a = [1, 3, 4, 6]  
print(all(a))  
  
# all values false  
a = [0, False]  
print(all(a))  
  
# one false value  
a = [1, 3, 7, 0]  
print(all(a))  
  
# one true value  
a = [0, False, 5]  
print(all(a))  
  
# empty iterable  
a = []  
print(all(a))  


