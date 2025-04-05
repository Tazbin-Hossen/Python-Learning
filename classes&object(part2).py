# Abstraction => hide unneccesary information from the user
# encapsulation => wrapping data and related function in single unit 

class account():
    def __init__(self,accNo,balance):
        self.accNo = accNo
        self.balance = balance

    def debit(self,deb):
        self.balance = self.balance - deb
        print('your amount is right now ',self.balance)

    def credit(self,cre):
        self.balance = self.balance + cre
        print('your amount is roght now ',self.balance)

    def get_balance(self):
        print('your total amount of balance is ',self.balance)
        

acc = account(1122334455,1000)
acc.debit(500)
acc.credit(1000)
acc.get_balance()


        