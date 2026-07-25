num1,num2 = map(int,input("Enter two numbers : ").split())
operator = input("Enter the operator : ")
if operator not in "*%//+-/**":
    print("Invalid operator!")
if operator =="*":
    print(num1 * num2)
elif operator =="%":
    print(num1%num2)
elif operator =="//":
    print(num1 // num2)
elif operator =="+":
    print(num1 + num2)
elif operator =="-":
    print(num1-num2)
elif operator =="/":
    print(num1 /num2)
elif operator =="**":
    print(num1**num2)

