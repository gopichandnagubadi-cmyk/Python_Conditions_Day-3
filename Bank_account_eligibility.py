customer_name = input("Enter name : ").capitalize()
age  = int(input("Enter your age : "))
nationality = input("Enter your nationality : ").upper()
initial_deposit = int(input("Enter the minimum initial deposit amount : "))
id_proof = input("Has valid Id proof (yes/no) : ").lower()
if age >=18:
    if nationality == "INDIAN":
        if initial_deposit >=1000:
            if id_proof =="yes" :
                print("congratulations ",customer_name ,"!")
                print("you are eligible to open bank account .")
else:
    print("Not eligible !")
    if age< 18:
        print("Reason : Age must be greater then 18")
    if nationality != "INDIAN" :
        print("Reason :  Not an indian ")
    if initial_deposit < 1000 :
        print("Reason : Minimum deposit should be greater then thousand")
    if id_proof !="yes":
        print("Reason : No id proof")
    
    

