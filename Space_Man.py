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
        self.game_word = []     # reference list of characters
        self.secret_word = []   # List contains underscores
        self.wrong_guesses = 0  # Wrong guesses counter
        self.user_word = ""     # It'll be what the user sees instead of a list of character
        self.guess = ""
        self.guess_list = []    # Record the unique letters that the user guessed

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

    # Ask user for category selection
    def word_choice(self):

        f = open("words.json")
        word_list = json.load(f)

        # Show keys parse from a JSON file
        for key in word_list.keys():
            print(key)

        selection = input("Please type the category you want to play: ")

        selection = selection.strip().upper()

        var = random.choice(word_list[selection])

        for character in var.upper():
            self.game_word.append(character)
            self.secret_word.append('_')

        for i in self.secret_word:
            self.user_word += i + " "

    # Function that will handle errors for first function
    def verify_first_choice(self):
        try:

            self.word_choice()

        except KeyboardInterrupt:
            print("You try to interrupt the keyboard!")
            self.verify_first_choice()

        except EOFError:
            print("You entered a END OF FILE input!")
            self.verify_first_choice()

        except KeyError:
            print("You might have misspelled, entered a number, or entered nothing for your input ")
            self.verify_first_choice()

    # Game functions method
    def game_function(self):

        # print(self.game_word)
        self.draw()
        print(self.user_word)
        print("Guess list: ")
        print(self.guess_list)

        guess = input("Guess a letter: ")
        guess = guess.upper()

        if guess.isalpha() and len(guess) == 1:
            if guess in self.game_word and guess:
                if guess not in self.guess_list:
                    os.system('clear')
                    self.user_word = ''
                    self.guess_list.append(guess)
                    for index, value in enumerate(self.game_word):
                        if guess == value:
                            self.secret_word[index] = value
                    for value in self.secret_word:
                        self.user_word += value + ' '

                else:
                    os.system("clear")
                    print("You've already guess this letter")
            else:
                os.system("clear")
                print("Wrong")
                self.wrong_guesses += 1
                print("You have " + str(self.wrong_guesses) + " wrong guess")
                self.guess_list.append(guess)
        else:
            os.system("clear")
            print("What you entered wasn't a alphabetical letter, not ONE letter, or nothing")

    # Check for ill inputs from user guesses
    def verify_user_guesses(self):
        try:
            self.game_function()

        except EOFError:
            os.system('clear')
            print("You entered an END OF FILE input")
            self.verify_user_guesses()

        except KeyboardInterrupt:
            os.system('clear')
            print("You try to Interrupt your keyboard")
            self.verify_user_guesses()

    # Run the program
    def run(self):
        self.verify_first_choice()
        while "_" in self.secret_word:
            self.verify_user_guesses()
            if self.wrong_guesses == 7:
                self.draw()
                print("You lose")
                break
        if "_" not in self.secret_word:
            print(self.user_word)
            print("Congratulation\nYOU WON!")


new = SpaceMan()

new.run()