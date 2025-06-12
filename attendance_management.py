def take_attendance():
    with open("student.txt", "r") as file:
        students_data = file.readlines()
        for student in students_data:
            student = student.strip()
            roll = student.split(",")[0]
            name = student.split(",")[1]
            while True:
                print(f"Roll: {roll}, Name: {name}")
                attendace = input("Present (y/n)").lower()
                if attendace == "y" or attendace == "n":
                    break
                else:
                    print("Enter Valid Input")
