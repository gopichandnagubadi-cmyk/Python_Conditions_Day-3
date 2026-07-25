citizen=input("Are you indian citizen? (yes/no) : ").lower()
age = int(input("Enter your age : "))
voter_id = input("Do yo have voter ID ? (yes/no) : ").lower()
if citizen == "yes" and age>=18 and voter_id == "yes":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
