class student:     #This is how class created
    name = 'Tazbin'
    age = 16

s1 = student()     #This is how object created
# print(s1.age)      #access age using object


               #----------Constructor (workflow)------------#


class Student:

    print("hello")

#self = reference of current instant(object)
#creating constructor

    def __init__(self,fullname,age):    
        self.name = fullname
        self.age = age
        print("Contructor Created")

# Constructor  methods => function in class 
    def hello(self):
        print("hello jonogon",self.name)

#when object is created __init__ function invoke automatically
s2 = Student("karim",16) 
s2.hello()            
print(s2.name,s2.age)


s3 = Student('jamal',18)


             #-------------Attributes---------------#

# obj attributes > class attributes
# if any information is common do it to the class attributes otherwise object attributes 


