# Create a file and write a file
f = open ("d:\sample.txt","w")
f.write("Python is best programming language")
f.close()

# Chech the content of a file
f = open ("d:\sample.txt","r")
print ("Contents of a open file is :", f.read())
f.close()
