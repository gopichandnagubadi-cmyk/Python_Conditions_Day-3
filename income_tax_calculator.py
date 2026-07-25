Annual_income=float(input("Enter your annual income : "))
if Annual_income <= 250000:
    Tax_rate   = 0
elif Annual_income <=500000:
    Tax_rate = (Annual_income-250000)*0.05
elif Annual_income <=1000000:
    Tax_rate = 12500+((Annual_income - 500000)*0.20)
else:
    Tax_rate = 112500+((Annual_income - 1000000)*0.30)
cess=0
if Tax_rate>=100000:
    cess =cess+Tax_rate*0.04    #if it is more then 100000 then we consider it as cess for health and education tax
Final_Tax = Tax_rate + cess
print(f"The amount of tax to be paid for the {Annual_income} is {Final_Tax:.2f}")


