#Lambda  function = annunomus function

double = lambda x : x*2
print(double(10))

sum = lambda x,y : x+y
print(sum(10,20))

def num(fx,val):
    return fx(val) + 5
print(num(double,2))