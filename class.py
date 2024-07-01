class Student:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact
    
    def getdata(self):
       print('Accepting Data')
       self.name = input('Enter Name: ')
       self.contact= (input('Enter Contact: '))

    def putData(self):
       print('Name of student is ',self.name,'\n Contact info is ',self.contact)


john = Student('',0)
john.getdata()
john.putData()
