import random

class Hangman:
    
    num_lives = 5

    def __init__(self, word_list, num_lives):

        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    def check_guess(self,guess):

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for position, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[position] = guess   
            print(self.word_guessed)

            self.num_letters -=1  

        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

        self.list_of_guesses.append(guess)


    def ask_for_input(self):

        allowed_characters = 'abcdefghijklmnopqrstuvwxyz'  

        while True:
            guess = input("Enter a single letter: ")
            guess = guess.lower()

            if len(guess)!=1:
                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess not in allowed_characters:
                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                self.check_guess(guess)

                break

def play_game():
    num_lives = 5
    word_list = ["apple", "banana", "pear", "grapes", "strawberry"]

    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
        
        elif game.num_letters > 0:
            game.ask_for_input()
        
        elif game.num_lives != 0 and game.num_letters <= 0:
            print("Congratulations! You won!")
            break

play_game()