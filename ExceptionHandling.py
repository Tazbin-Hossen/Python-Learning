a = 10
b = 2

try:
    print("Resource open: ")
    print(a/0)
except Exception:
    print("You cannot devide a a number by zero.")
finally:
    print("Resource close.")

print("Thank you.")
