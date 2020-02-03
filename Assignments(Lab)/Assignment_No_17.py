#Select a text file and count number of words, Lines, Characters.
num_chars = 0   # Assign Value 0 for all variable
num_words = 0
num_lines = 0
a = []
# Open file in read  mode
f = open("e:\sample.txt","r")
#Consider each line for counting the words and chars.
for line in f:     # for loop is rotate as per file object
    word = line.split()  # Seperate the word from line.
    num_words += len(word)  # update the count value of words
    num_lines += 1  # # update the count value of lines
    num_chars = len(line) # update the count value of characters
print ("Number of Characters in file is :", num_chars)  # print all values.
print ("Number of Words in file is :",num_words) 
print ("Number of Lines in file is :",num_lines)
f.close()
print ("-----------------------------------------------------------")
f = open("e:\sample.txt","r")
data = f.read()
a.append(data.split())
dict3 = {} # Create a dict.
array = a[0] # Nested list is created so consider first element
for x in array:  # Trace each and every element in list 
    if not x in dict3:   # Element found in list or not 
        dict3[x] = array.count(x)  # if found the update the count and value also
print ("Count of Repeated Word is :\n",dict3)       # print dict

