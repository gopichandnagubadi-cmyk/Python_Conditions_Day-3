Student_name = input("Enter the name of the student : ")
Roll_no = input("Enter your roll no. : ")

Marks = list(map(int, input("Enter five subject marks : ").split()))

if len(Marks) != 5:
    print("Please enter exactly 5 subject marks.")
else:
    Total_marks = 0
    valid = True

    # Validate marks and calculate total
    for i in Marks:
        if i < 0 or i > 100:
            print("Invalid marks!")
            valid = False
            break
        else:
            Total_marks += i

    if valid:
        Average = Total_marks / len(Marks)

        # Calculate Grade
        if Average >= 90:
            Grade = "A+"
        elif Average >= 80:
            Grade = "A"
        elif Average >= 70:
            Grade = "B"
        elif Average >= 60:
            Grade = "C"
        elif Average >= 50:
            Grade = "D"
        else:
            Grade = "F"

        # Calculate Result
        Result = "Pass"
        for i in Marks:
            if i < 35:
                Result = "Fail"
                break

        # Display Result
        print("\n----------- Student Result -----------")
        print(f"Student Name : {Student_name}")
        print(f"Roll No      : {Roll_no}")
        print(f"Marks        : {Marks}")
        print(f"Total Marks  : {Total_marks}")
        print(f"Average      : {Average:.2f}")
        print(f"Grade        : {Grade}")
        print(f"Result       : {Result}")