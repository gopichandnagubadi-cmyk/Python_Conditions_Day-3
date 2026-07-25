age = int(input("Enter the age of the person : "))
day = input("Enter the day ticket booked : ").lower()
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
Ticket_price = 0
if age<=0 :
      print("invalid age!")
elif day not in days:
    print("invalid day!")
else:      
    if day !="wednesday":
        if age <5:
            Ticket_price =0
        elif age <=12:
            Ticket_price = 100
        elif age <=59:
            Ticket_price = 200
        else:
            Ticket_price = 150
    else:
        if age <5:
            Ticket_price =0
        elif age <=12:
            Ticket_price = 100-100*0.1
        elif age <=59:
            Ticket_price = 200-200*0.1
        else:
            Ticket_price = 150-150*0.1
    print(f"the cost is {Ticket_price:.2f} for your age {age} on the day {day}")
    
