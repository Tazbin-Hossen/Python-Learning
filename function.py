#sum of expenses using function
rahim_expenses = [100,200,300]
def calculate_expenses (exp):    #decalre a function
    total = 0
    for item in exp :
        total = total + item
    return total
total_expenses  = calculate_expenses(rahim_expenses)  #function call
print(total_expenses)

#sum of two number using function
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
def sum(a,b):
    return a+b
ans = sum(num1,num2)
print(ans)