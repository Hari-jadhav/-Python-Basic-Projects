import math

try:
    sentence = input("Enter a Sentence : ")

    words = sentence.split()

    unique_words = set(words)

    sorted_words = sorted(unique_words)

    print("\nUnique Words in Sorted Order")

    for word in sorted_words:
        print(word)

    total = len(unique_words)

    print("\nSquare of Total Unique Words :", math.pow(total, 2))

except Exception as e:
    print("Error :", e)