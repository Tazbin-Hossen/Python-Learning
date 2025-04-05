           #--------------------delete attributes--------------------#

class student():
    def __init__(self,name):
        self.name = name
s1 = student("mahadi")
print(s1.name)
del s1.name        #delete name attributes
#print(s1.name)


         #--------------private attributes and methods------------------#

class Account():
    def __init__(self,accNo,accPass):
        self.accNo = accNo
        # __accPass means it cannot access out of the class  
        self.__accPass = accPass

    def acceess(self):
        print(self.__accPass) 

acc = Account(112233,"12avcduhehf")
#print(acc.__accPass)
acc.acceess()

                #----------------Inheritance------------------#

#single inheritance

class car:

    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped.....")

class toyotaCar(car):
    def __init__(self,name,model):
        self.name = name
        self.model = model

toyota = toyotaCar("fortuner","a75")

# print(toyota.name)
# print(toyota.model)
# print(toyota.start())

# multi level inheritance 

class car:

    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped.....")

class toyotaCar(car):
    def __init__(self,name,model):
        self.name = name
        self.model = model

class fortuner(toyotaCar):
    def __init__(self, type):
        self.type = type

car1 = fortuner("diesel")
print(car1.start())

#multiple inheritance

class A:
    varA = 'variable A'

class B:
    varB = 'variable B'

class C:
    varC = 'variable C'

class D(A,B,C):
    varD = 'variable D'

ans = D()
print(ans.varA)
print(ans.varB)
print(ans.varC)
print(ans.varD)

   
        #---------super method--------------#
#it mainly use call a method from parent class in a chlid class

class car:
    
    def __init__(self,type):
        self.type = type
        print(type)
        
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped.....")

class toyotaCar(car):
    def __init__(self,name,model,type):
        self.name = name
        self.model = model
        super().__init__(type)

car2 = toyotaCar('axio',2016,'electric')
print(car2.name)
print(car2.model)
print(car2.type)

              #------------class methods----------------#

class person:
    name = 'annonymous'

    # def changeName(self,name):
    #     self.__class__.name = name

    @classmethod
    def changeName(cls,name):
        cls.name = name

s1 = person()
s1.changeName("mahadi")
print(s1.name)
print(person.name)

              #-----------property method----------------#
# it used for change the class property and always this property return the updated value

class subjects:
    phy = 98
    chem = 98
    math = 98
    
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property 
    def calculate(self):
        calc = str((self.phy + self.chem + self.math) / 3)
        print(calc)

s1 = subjects(60,60,60)
s1.calculate 
s1.phy = 100
s1.calculate
s1.calculate