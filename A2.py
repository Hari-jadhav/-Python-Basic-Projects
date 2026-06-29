def analyze_string(s):
    # Check for empty string
    if len(s) == 0:
        print("String is empty.")
        return

    # Length
    print("Length:", len(s))

    # Reverse
    print("Reverse String:", s[::-1])

    # Count vowels
    vowels = "aeiou"
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1

    print("Total Vowels:", count)

    # Print characters with positive and negative index
    print("\nCharacter\tPositive Index\tNegative Index")

    for i in range(len(s)):
        print(s[i], "\t\t", i, "\t\t", i - len(s))


# User Input
text = input("Enter a string: ")

analyze_string(text)