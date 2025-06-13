import os
from datetime import date


def take_attendance():
    with open("student.txt", "r") as file:
        students_data = file.readlines()
        student_attendance = []
        for student in students_data:
            student = student.strip()
            roll = student.split(",")[0]
            name = student.split(",")[1]
            while True:
                print(f"Roll: {roll}, Name: {name}")
                attendace = input("Present (y/n)").lower()
                if attendace == "y" or attendace == "n":
                    student_attendance.append(f"{roll},{name},{attendace}\n")
                    break
                else:
                    print("Enter Valid Input")
        with open(f"attendance/{date.today()}.txt", "w") as file:
            file.writelines(student_attendance)


def view_attendance():
    date_input = input("Enter date(yyyy-dd-mm) to view student")
    if os.path.exists(f"attendance/{date_input}.txt"):
        with open(f"attendance/{date_input}.txt", "r") as file:
            attendance_data = file.readlines()
            for attendance in attendance_data:
                print(attendance.strip())
    else:
        print("File Does not Exist")
