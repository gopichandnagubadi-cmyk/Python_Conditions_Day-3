units = int(input("Enter the number of units consumed: "))
fixed_charge = 100

if units <= 100:
    bill = units * 1.50
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
elif units <= 300:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
else:
    bill = 100 * 1.50 + 100 * 2.50 + 100 * 4.00 + (units - 300) * 6.00

total_bill = bill + fixed_charge

if total_bill > 1000:
    total_bill = total_bill + (total_bill * 0.05)

print(f"Total electricity bill for {units} units is: {total_bill:.2f}/-")