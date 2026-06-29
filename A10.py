import math
import random
from datetime import datetime

history = {}


def basic_calculator():
    try:
        a = float(input("Enter First Number : "))
        b = float(input("Enter Second Number : "))

        op = input("Enter (+,-,*,/) : ")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        else:
            print("Invalid Operator")
            return

        print("Result :", result)

        history[str(datetime.now())] = result

    except Exception as e:
        print(e)


def scientific():
    try:
        num = float(input("Enter Number : "))

        print("Square Root :", math.sqrt(num))
        print("Power :", math.pow(num, 2))
        print("Factorial :", math.factorial(int(num)))

    except Exception as e:
        print(e)


def random_number():
    number = random.randint(1, 100)

    print("Random Number :", number)

    history[str(datetime.now())] = number


def view_history():
    if not history:
        print("No History Available")

    else:
        for time, value in history.items():
            print(time, ":", value)


while True:

    print("\n===== Smart Calculator =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculator")
    print("3. Generate Random Number")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        basic_calculator()

    elif choice == "2":
        scientific()

    elif choice == "3":
        random_number()

    elif choice == "4":
        view_history()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")