def student_database():
    students = {}

    while True:
        print("\n----- Student Database -----")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                roll = input("Enter Roll Number: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

                print("Student Added Successfully.")

            except ValueError:
                print("Invalid Age!")

        elif choice == "2":
            roll = input("Enter Roll Number: ")
            student = students.get(roll)

            if student:
                print(student)
            else:
                print("Student Not Found.")

        elif choice == "3":
            if not students:
                print("No Records Found.")
            else:
                for roll, details in students.items():
                    print("\nRoll No:", roll)
                    print(details)

        elif choice == "4":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


student_database()