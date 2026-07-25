num1,num2,num3 = map(int,input("Enter three numbers : ").split())
if num1>num2 and num1 > num3:
    print(f"{num1} is largest")
elif num2> num1 and num2 > num3:
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")