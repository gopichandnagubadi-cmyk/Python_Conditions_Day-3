number = int(input("Enter a number : "))
a= int(input("Enter first divisor : "))
b= int(input("Enter second divisor : "))
if number % a ==0 and number % b == 0:
    print(f"{number} is divisible by both {a} and {b}")
elif number % a == 0:
    print(f"{number} is only divisible by {a}")
elif number % b == 0:
    print(f"{number} is only divisible byb {b}")
else:
    print(f"{number} is not divisible by either {a} or {b}")