def add(a,b):
    c= a+b
    return c
def subtract(a,b):
    c= a-b
    return c
def multiply (a,b):
    c= a*b
    return c
def divide(a,b):
    c= a/b
    return c







print("enter the first number" )
n1 = float(input())
print("enter the second number")
n2 = float(input())

print("enter + FOR addition,- for subtraction, * for multiplication ,/ for division")

sym =input()


if sym == "+":
    number = add(n1,n2)
    print(number)

if sym == "-":
    number = subtract(n1,n2)
    print(number)
if sym == "*":
    number = multiply(n1,n2)
    print(number)
if sym == "/":
    number = divide(n1,n2)
    print(number)



