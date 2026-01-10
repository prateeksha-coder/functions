
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Please choose an option:")
print("a. Addition")
print("b. Subtraction")
print("c. Product")
print("d. Divide")

choice=input("Enter your choice a/b/c/d: ")

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

if choice=='a':
    print("Sum :", add(num1, num2))
elif choice=='b':
    print("Difference :", subtract(num1, num2))
elif choice=='c':
    print("Product :", multiply(num1, num2))
elif choice=='d':
    print("Quotient :", divide(num1, num2))
else:
    print("Invalid Input Choice!!")