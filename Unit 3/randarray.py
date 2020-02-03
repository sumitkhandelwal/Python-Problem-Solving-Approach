#A random bytearray  
randarray = bytearray('ABC', 'utf-8')  
  
mv = memoryview(randarray)  
  
# access the memory view's zeroth index  
print(mv[0])  
  
# It create byte from memory view  
print(bytes(mv[0:2]))  
  
# It create list from memory view  
print(list(mv[0:3]))  

