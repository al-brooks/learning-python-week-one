# Assignment 2: Palindrome

def is_Palindrome(word):
    reversed_word = ""

    for index in range(len(word)-1, -1, -1):
        reversed_word += word[index]

    if word == reversed_word:
        return True
    else:
        return False

word = input("Enter a word: ")

if is_Palindrome(word):
    print("Yes, word is a Palindrome")
else:
    print("Word is not a Palindrome")
