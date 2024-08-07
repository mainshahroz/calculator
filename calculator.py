
print("enter the first number" )
n1 = float(input())
print("enter the second number")
n2 = float(input())

print("enter + FOR addition,- for subtraction, * for multiplication ,/ for division")

sym =input()


if sym == "+":
    print(f"{n1}{sym}{n2}={n1+n2}")

if sym == "-":
    print(f"{n1}{sym}{n2}={n1-n2}")
if sym == "*":
     print(f"{n1}{sym}{n2}={n1*n2}")
if sym == "/":
    print(f"{n1}{sym}{n2}={n1/n2}")



