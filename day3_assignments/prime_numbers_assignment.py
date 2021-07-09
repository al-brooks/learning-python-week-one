# Assignment 3 - Prime or Not

def is_prime(number):
    test_number = 2 # Skipping 1: All numbers are divisible by 1
    if number < 2: # 2 is the first Prime Number so any numbers entered before 2 are false.
        return False
    while number > test_number: # Only need to compare to lower numbers
        if number % test_number == 0:
            return False
            break
        test_number += 1
    
    return True # Once while loop is complete, if it was not broken assign value of True.

number = int(input("Enter a number: "))

if is_prime(number):
    print("This is a Prime Number")
else:
    print("This is not a Prime Number")

# Test range of Prime Numbers
for number in range(2,100):
    if is_prime(number):
        print(f"{number} is a Prime Number")
