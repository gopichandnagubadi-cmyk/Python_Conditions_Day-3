student_marks = int(input("Enter your marks  :  "))
if student_marks >100:
    print("Invalid marks")
if student_marks >=90 and student_marks <= 100:
    print("Grade : A+")
elif student_marks >=80 and student_marks <90:
    print("Grade : A")
elif student_marks >= 70 and student_marks <80:
    print("Grade : B")
elif student_marks >= 60 and student_marks <70:
    print("Grade : C")
elif student_marks >= 50 and student_marks <60:
    print("Grade : D")
elif student_marks <50:
    print("Grade : F")