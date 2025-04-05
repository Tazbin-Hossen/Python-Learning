       #-----------------polymorphysom-----------------#
# when same operator have different meaning accourding to the context
class complexNumber :

    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def mainForm(self):
        print(self.real,"i + ",self.img,"j")

    def __add__(self,cmp2):       # __add__ (dunder function)
        newX = self.real + cmp2.real
        newY = self.img + cmp2.img
        return complexNumber(newX,newY)

cmp = complexNumber(3,4)
cmp.mainForm()

cmp2 = complexNumber(5,6)
cmp2.mainForm()

cmp3 = cmp + cmp2
cmp3.mainForm()
        

