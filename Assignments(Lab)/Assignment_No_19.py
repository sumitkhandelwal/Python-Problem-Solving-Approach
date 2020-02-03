class Person(object):
    """__init__() functions as the class constructor"""
    def __init__(self, name=None, job=None, quote=None):
        self.name = name
        self.job = job
        self.quote = quote
# make a list of class Person(s)
personList = []
personList.append(Person("Payne N. Diaz", "coach", "Without exception, there is no rule!"))
personList.append(Person("Mia Serts", "bicyclist", "If the world didn't suck, we'd all fall off!"))
personList.append(Person("Don B. Sanosi", "teacher", "Work real hard while you wait and good things will come to you!"))
personList.append(Person("Hugh Jorgan", "organist", "Age is a very high price to pay for maturity."))
personList.append(Person("Herasmus B. Dragon", "dentist", "Enough people can't find work in America!"))
personList.append(Person("Adolph Koors", "master-brewer", "Wish you were beer!"))
personList.append(Person("Zucker Zahn", "dentist", "If you drink from the fountain of knowledge, quench your thirst slowly."))
print ("Show one particular item:")
for i in range(len(personList)):
    print ("Name :", personList[i].name)
    print ("Job :", personList[i].job)
    print ("Quote :", personList[i].quote)
    print ("----------------------------------------------------------")
def compute():
    count = len(personList)
    print (count)
print ("Total Number of Employee in an organization :",)
compute()

print ("Sort the personList in place by job ...")
import operator
print (personList.sort(key=operator.attrgetter('job')))
#https://www.daniweb.com/programming/software-development/code/216631/a-list-of-class-objects-python#
