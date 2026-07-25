#absolute value is nothing but the distance of a number from zero. It is always positive.
#we can also say it as mod in mathematics. It is denoted by |X|.
number = int(input("Enter a number : "))
if number <0:
    number *= -1
    print(f"the absolute value of the number is {number}")
else:
    print(f"the absolute value of the number is {number}")

# or else we can directly use the built-in function abs(number).  