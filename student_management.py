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
