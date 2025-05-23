def add_student():
    roll_no = input("Enter Your Roll No: ")
    name = input("Enter Your Name: ")
    contact_no = input("Enter Your Contact No: ")
    with open("student.txt", "a") as student:
        student.write(f"{roll_no},{name},{contact_no}\n")
    print("Student Record Added Successfully")


def view_student():
    with open("student.txt", "r") as student_data:
        students = student_data.readlines()
        for student in students:
            print(student.strip())


def update_student():
    print("You are on Update Student Function")


def delete_student():
    print("You are on Delete Student Function")


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
