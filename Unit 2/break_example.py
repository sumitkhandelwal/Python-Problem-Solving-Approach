list1 =[1,2,3,4,5,6,7,8,9,10]  
item = int(input("Enter the item do you want to find its position :"))
for i in range(len(list1)):
    if list1[i] == item :
        print("Item matched")
        break  
print("found at", i, "location") 
