import random
import string

word_list = ["apple", "banana", "pear", "grapes", "strawberry"]
word = random.choice(word_list)

guess = input("Enter a single letter")
guess = guess.upper()

allowed_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if len(guess)!=1:
    print("Oops! That is not a valid input.") 
elif guess not in allowed_characters:
    print("Oops! That is not a valid input.") 
else:
    print("Good guess!")