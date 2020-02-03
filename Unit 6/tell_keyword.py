# open the in read mode  
f = open("d:/sample.txt","r")  
  
#initially the filepointer is at 0   
print("The filepointer is at byte :",f.tell())  
  
#reading the content of the file  
data = f.read();  
  
#after the read operation file pointer modifies. 
print("After reading, the filepointer is at:",f.tell())  
