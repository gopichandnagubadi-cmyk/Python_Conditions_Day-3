weight = float(input("Enter your weight in (Kg's) : "))
height = float(input("Enter your height in (meters) : "))
Bmi = weight/(height**2)
if Bmi< 18.5:
    print(f"the {Bmi:.2f} shows category Underweight")
elif Bmi< 25:
    print(f"the {Bmi:.2f} shows category Normal weight")
elif Bmi< 30 :
    print(f"the {Bmi:.2f} shows category Over weight")
else:
    print(f"the {Bmi:.2f} shows category Obese")
