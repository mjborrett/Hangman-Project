import random

word_list = ["apple", "banana", "pear", "grapes", "strawberry"]
word = random.choice(word_list)
print(word)
guess = None

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    allowed_characters = 'abcdefghijklmnopqrstuvwxyz'  
    while True:
        guess = input("Enter a single letter: ")
        guess = guess.lower()
        if len(guess)!=1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess not in allowed_characters:
            print("Invalid letter. Please, enter a single alphabetical character.")
        else:
            break
        check_guess(guess)

ask_for_input()