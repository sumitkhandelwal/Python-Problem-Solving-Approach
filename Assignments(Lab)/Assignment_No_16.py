'''To copy contents of one file to other. While copying
a) all full stops are to be replaced with commas
b) lower case are to be replaced with upper case
c) upper case are to be replaced with lower case'''

# Open a exiting file
f = open("e:\sample.txt","r")
data = f.read()
print ("Content of a file is :", data)
f.close()
# all full stops are to be replaced with commas
data = data.replace(".",",")
print ("------------------------------------------------------")
print ("All full stops are to be replaced with commas :")
print (data)
#lower case are to be replaced with upper case
#upper case are to be replaced with lower case
print ("------------------------------------------------------")
print ("Swapcase of data :")
data = data.swapcase()
print (data)
# Load the data in new file
f = open("e:\sample_new.txt","w")
f.write(data)
print("Data loaded into new file.")
f.close()
