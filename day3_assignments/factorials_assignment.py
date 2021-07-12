# Assignment 1: Factorial
def calculate_factorial(number):
    factorial = 1

    for number in range(1, number + 1): # up to but not including (end number) - add 1
        print(f"{factorial} is the factorial and will be multiplied by: {number}") # list out each loop iteration
        factorial *= number
    
    print(f"The factorial value of {number} is: {factorial}")
    return factorial
# --------------------------------------------------------------
    # Alternate method - using While loop and array

    # number_range = []

    # while number > 0:
    #     number_range.append(number)
    #     number -= 1

    # for index in range(0, len(number_range)):
    #     factorial *= number_range[index]
    #     # First Loop: Factorial = 1(original value) * 4
        # Second Loop: Factorial = 4(new value) * 3
        # etc.
# --------------------------------------------------------------
    

number = int(input("Enter a number: "))

calculate_factorial(number)