a,b,c=map(int,input("Enter three sides of the triangle : ").split())
if a+b <= c or a+c <=b or b+c<=a:
    print("Invalid Triangle!")
else:
    if a==b and a==c:
        print("Equilateral Triangle")
    elif (a==b and a!=c) or (b==c and b!=a) or (a==c and a!=b):
        print("Isosceles Triangle!")
    elif (a!= c and a!=b and c!=b):
        print("Scalene Triangle!")