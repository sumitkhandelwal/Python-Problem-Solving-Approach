#opens the file file.txt in read mode and extract the contents  
f = open("d:/file_sample.txt","r")  
str1 = f.read()
print ("File open sucessfully and contents in file is :",str1)
f.close()  # Close the file
if f :
    str2 = f.read()
    print ("File open sucessfully and contents in file is :",str2)
else:
    print ("File is not open now.")

