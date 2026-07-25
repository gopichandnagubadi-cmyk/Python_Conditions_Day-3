User_name = 'admin'
Password = 'admin123'
attempts = 3
while attempts>0:
    user_name = input("Enter valid user Id : ")
    password = input("Enter valid password : ")
    if User_name == user_name and Password == password:
        print("Login successful!")
        print("Welcome, admin")
        attempts =0
    else:
        if User_name != user_name and User_name != user_name :
            print("Both of them are invalid")
        elif User_name != user_name :
            print("Invalid username.")
        elif User_name != user_name :
            print("Incorrect Password.")
    attempts -=1
print("Account Locked permanently")
    