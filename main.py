from student_management import (
    add_student, update_student,
    view_student, delete_student
)


def menu():
    print("Enter 1 To add student")
    print("Enter 2 To Update Student")
    print("Enter 3 To Delete Student")
    print("Enter 4 To View Student")
    print("Enter 5 To Take Attendance")
    print("Enter 6 To View Attendance")
    print("Enter 7 to Exit")


while True:
    menu()
    option = input("Enter Menu No: ")
    if option == "1":
        add_student()
    elif option == "2":
        update_student()
    elif option == "3":
        delete_student()
    elif option == "4":
        view_student()
    elif option == "7":
        print("Exit")
        break
    else:
        print("Invalid Option")
