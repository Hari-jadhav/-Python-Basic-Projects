class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    def add_mark(self, mark):
        try:
            mark = float(mark)

            if mark < 0 or mark > 100:
                print("Invalid Marks")
            else:
                self.marks_list.append(mark)

        except ValueError:
            print("Enter numeric marks only.")

    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    def display_info(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks :", self.marks_list)
        print("Average :", self.get_average())


name = input("Enter Name: ")
roll = input("Enter Roll Number: ")

student = Student(name, roll)

for i in range(5):
    mark = input(f"Enter Mark {i+1}: ")
    student.add_mark(mark)

student.display_info()