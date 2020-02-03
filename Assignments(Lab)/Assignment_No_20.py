# Class Defination
class Product(object):
     """__init__() functions as the class constructor"""
     def __init__(self, code=None, name=None, price=None):
         self.code = code
         self.name = name
         self.price = price
         
prodList = []
prodList.append(Product('101','Milk','20'))
prodList.append(Product('102','Curd','25'))
prodList.append(Product('103','CMilk','23'))
prodList.append(Product('104','Toste','26'))
prodList.append(Product('105','Bread','28'))
prodList.append(Product('106','Buter','30'))
prodList.append(Product('107','Suger','20'))
prodList.append(Product('108','Tea','40'))
prodList.append(Product('109','Cofee','45'))
prodList.append(Product('110','Ceame','10'))
print (" Menu Card of Restonant is :")
print ("Product Code \t\t Name of Product \t\t\t Price") 
for i in range(len(prodList)):
    print (prodList[i].code,"\t\t\t\t",prodList[i].name,"\t\t\t\t",prodList[i].price)
bill = 0
for j in range(len(prodList)):
    ch= str(input ("Do You want to Purchase any product :(Y/N)"))
    if(ch == 'Y'):
        code_p = str(input("Enter the product code here :"))
        for i in range(len(prodList)):
            if(prodList[i].code == code_p):
                bill = bill + int(prodList[i].price)
    elif(ch == 'N'):
        break
    else:
        print ("Invalid Choice:")
        break      
print ("Bill Amount is :", bill)
