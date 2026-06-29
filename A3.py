def manage_marks():
    marks = []

    print("Enter marks of 5 subjects:")

    while len(marks) < 5:
        try:
            mark = float(input(f"Subject {len(marks)+1}: "))

            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100.")
                continue

            marks.append(mark)

        except ValueError:
            print("Please enter numeric values only.")

    average = sum(marks) / len(marks)

    print("\nMarks List:", marks)
    print("Average Marks:", average)
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))

    marks.sort(reverse=True)

    print("Marks in Descending Order:", marks)


manage_marks()