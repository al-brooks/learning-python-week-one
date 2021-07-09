# num1 = int(input("Enter your first number: "))
# operand = input("Enter an operand (+, -, *, /): ")
# num2 = int(input("Enter your second number: "))

# def calculator_all_operands(num1, operand, num2):
#     if operand == "+":
#         return num1 + num2
#     elif operand == "-":
#         return num1 - num2
#     elif operand == "*":
#         return num1 * num2
#     elif operand == "/":
#         return num1 / num2
#     else: 
#         print("Warning Invalid Operand Input")

# print(calculator_all_operands(num1, operand, num2))

# Hardmode - Separate Functions:

num1 = int(input("Enter your first number: "))
operand = input("Enter an operand (+, -, *, /): ")
num2 = int(input("Enter your second number: "))

def calculator_addition(num1, num2):
    return num1 + num2

def calculator_subtraction(num1, num2):
    return num1 - num2

def calculator_multiplication(num1, num2):
    return num1 * num2

def calculator_division(num1, num2):
    return num1 / num2

def calculator_all_operands(num1, operand, num2):
    if operand == "+":
        return calculator_addition(num1, num2)
    elif operand == "-":
        return calculator_subtraction(num1, num2)
    elif operand == "*":
        return calculator_multiplication(num1, num2)
    elif operand == "/":
        return calculator_division(num1, num2)
    else: 
        print("Warning Invalid Operand Input")

print(calculator_all_operands(num1, operand, num2))

 # Showing all calculations based on number inputs as well

print(calculator_addition(num1, num2))
print(calculator_subtraction(num1, num2))
print(calculator_multiplication(num1, num2))
print(calculator_division(num1, num2))
