# Assignment 1: Factorial
def calculate_factorial(number):
    # number_range = [] # Method 2
    factorial = 1

    # while number > 0: # Method 2
    #     number_range.append(number)
    #     number -= 1


    for number in range(1, number + 1): # up to but not including (end number) - add 1
        print(f"{factorial} is the factorial and is being multiplied by: {number}") # list out each loop iteration
        factorial *= number
    
    # for index in range(0, len(number_range)): # Method 2
    #     factorial *= number_range[index]
    #     # First Loop: Factorial = 1(original value) * 4
        # Second Loop: Factorial = 4(new value) * 3
        # etc.

    return factorial

number = int(input("Enter a number: "))

print(calculate_factorial(number))
