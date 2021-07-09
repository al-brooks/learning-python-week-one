# Assignment 1: Factorial
def calculate_factorial(number):
    number_range = []
    factorial = 1

    while number > 0:
        number_range.append(number)
        number -= 1

    for index in range(0, len(number_range)):
        factorial *= number_range[index]
        # First Loop: Factorial = 1(original value) * 4
        # Second Loop: Factorial = 4(new value) * 3
        # etc.

    return factorial

number = int(input("Enter a number: "))

print(calculate_factorial(number))
