number = int(input("Enter a number : "))
a= int(input("Enter first divisor : "))
b= int(input("Enter second divisor : "))
if number % a ==0 and number % b == 0:
    print(f"{number} is multiple of both {a} and {b}")
elif number % a == 0:
    print(f"{number} is only multiple of  {a}")
elif number % b == 0:
    print(f"{number} is only multiple of {b}")
else:
    print(f"{number} is not multiple of either {a} or {b}")