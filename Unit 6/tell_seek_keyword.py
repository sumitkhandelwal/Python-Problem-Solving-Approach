# open the file  in read mode  
f= open("d:/sample.txt","r")  
  
#initially the filepointer is at 0   
print("The filepointer is at byte :",f.tell())  
  
#changing the file pointer location to 10.  
f.seek(10);  
  
#tell() returns the location of the fileptr.   
print("After reading, the filepointer is at:",f.tell())  
