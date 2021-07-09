num = int(input("Enter a number: "))

def fizz_buzz(num):
    if (num % 3) == 0 and (num % 5) == 0:
        print("Fizz Buzz")
    elif (num % 5) == 0:
        print("Buzz")
    elif (num % 3) == 0:
        print("Fizz")
    else:
        print("Value is not divisble by 3 or 5")

fizz_buzz(num)