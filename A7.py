try:
    square = lambda x: x ** 2

    numbers = range(1, 21)

    squares = list(map(square, numbers))

    print("All Squares:")
    print(squares)

    print("\nEven Squares:")

    for num in squares:
        if num % 2 == 0:
            print(num)

except Exception as e:
    print("Error:", e)