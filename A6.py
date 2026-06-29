import random
import math

try:
    numbers = set()

    while len(numbers) < 10:
        num = int(input("Enter Number: "))
        numbers.add(num)

    number_tuple = tuple(numbers)

    print("\nUnique Numbers:", number_tuple)

    print("Random Numbers:",
          random.sample(number_tuple, 3))

    total = sum(number_tuple)

    print("Square Root of Sum:",
          math.sqrt(total))

except ValueError:
    print("Please Enter Integer Values.")

except Exception as e:
    print("Error:", e)