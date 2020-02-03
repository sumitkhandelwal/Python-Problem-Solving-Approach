def Addition(n):  
  return n+n  
  
numbers = (1, 2, 3, 4, 5, 6, 7, 8)  
result = map(Addition, numbers)  
print(result)  
  
# converting map object to set  
numbersAdd = set(result)  
print(numbersAdd)  

