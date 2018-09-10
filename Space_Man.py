import random
import os
import json


class SpaceMan:

    def __init__(self):
        self.man_art = ["        0",
                        '      /-+-/',
                        '        |',
                        '        |',
                        "       / \ ",
                        ]
        self.rocket_art = ["        |",
                           "       / \ ",
                           "      / _ \ ",
                           "     |.o '.| ",
                           "     |'._.'| ",
                           "     |     | ",
                           "   ,'|  |  |`.",
                           "  /  |  |  |  \ ",
                           "  |,-'--|--'-.| "
                           ]
        self.fire_art = ['     #######',
                         "    #########",
                         "     ####### ",
                         "      #####  ",
                         "      #####  ",
                         "       ###   ",
                         "       ###   ",
                         "       ###   ",
                         "       ###   "
                         ]
        self.categories = ["STATES", "COUNTRIES"]
        self.game_word = []  # reference list of characters
        self.secret_word = []  # List contains the amount of characters as the reference list but with underscores
        self.wrong_guesses = 0  # Wrong guesses counter
        self.user_word = ""  # It'll be what the user sees instead of a list of character
        self.guess_list = []  # Record the unique letters that the user guessed

    # Draw function for wrong guesses
    def draw(self):
        if self.wrong_guesses <= 5:
            for i in range(self.wrong_guesses):
                print(self.man_art[i])

        elif self.wrong_guesses == 6:
            for i in self.rocket_art:
                print(i)

        else:
            for i in self.rocket_art:
                print(i)
            for i in self.fire_art:
                print(i)

    # Generate random word from the library and create a list with the characters
    def word_choice(self):

        f = open("words.json", 'r')
        word_list = json.load(f)

        # Show the index and categories' names for the user to choose
        for index, title in enumerate(word_list):
            print(index, title)

        choice = input("Please input the number associated with the categories: ")

        # Test if the user try to chose a out of index categories or inputted a character that is not a number
        try:
            var = random.choice(word_list[self.categories[int(choice)]])

            for character in var.upper():
                self.game_word.append(character)
                self.secret_word.append('_')

            for i in self.secret_word:
                self.user_word += i + " "

            print(self.game_word)
            print(self.user_word)

        except ValueError:
            os.system("clear")
            print("What you input wasn't a number!")
            self.word_choice()

        except IndexError:
            os.system("clear")
            print("You tried to select a categories that doesn't exist: ")
            self.word_choice()

    # Game functions method
    def game_function(self):

        # User input
        guess = input("Guess a letter: ")

        # Check whether the user inputted a alphabetical
        if guess.isalpha() and len(guess) == 1:

            # Check if the guess is correct and if the user guess the same letter
            if guess.upper() in self.game_word and guess.upper() not in self.guess_list:

                # loop for the indexes and values in the reference list of characters
                for index, value in enumerate(self.game_word):

                    # Checking if the user's guess is identical to the item in the reference list
                    # If pass, the item in the secret list will change according to the index
                    if guess.upper() == value:
                        self.secret_word[index] = value
                        self.user_word = ''         # Reset the word

                        # Checking if the correct guess is not in the guess list
                        if value not in self.guess_list:
                            self.guess_list.append(value)

                        # Concatenate characters plus spaces
                        for i in self.secret_word:
                            self.user_word += i + " "

                        os.system('clear')
                        self.draw()
                        print(self.user_word)
                        print(self.guess_list)

            # Catch if the user's guess the same letter
            elif guess.upper() in self.guess_list:
                os.system("clear")
                self.draw()
                print(self.user_word)
                print(self.guess_list)
                print("You've already guessed this letter")

            # Record and notify the wrong guesses
            else:
                os.system('clear')
                self.guess_list.append(guess.upper())
                self.wrong_guesses += 1
                self.draw()
                print(self.user_word)
                print("You have " + str(self.wrong_guesses) + " wrong guesses")
                print(self.guess_list)

        # Catch the ill inputs
        else:
            print("You've either inputted nothing, not a alphabetical character, or multiple letters!\n" +
                  "Please try again")
            self.game_function()

    # Run the program
    def run(self):
        self.word_choice()
        while "_" in self.secret_word:
            self.game_function()
            if self.wrong_guesses == 7:
                print("You lose")
                break
        if "_" not in self.secret_word:
            print("Congratulation\nYOU WON!")


new = SpaceMan()

new.run()