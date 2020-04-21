import random

print('Hello! What is your name? ')
myName = input()
print("Welcome " + str(myName) + "!" + " Let's play a guessing game.")


def guessing_game():

    play = True
    while play:

        easy = random.randint(1, 10)
        medium = random.randint(1, 20)
        hard = random.randint(1, 50)
        
        print("Would you like to play on easy, medium, or hard?"
              "\nType 'e' for easy, 'm' for medium, or 'h' for hard!")

        level_selection = True
        while level_selection:
            level = input()
            if level == "e":
                print("\nAwesome! We'll begin with easy!")
                level_selection = not True
                break
            if level == "m":
                print("\nAwesome! We'll begin with medium!")
                level_selection = not True
                break
            if level == "h":
                print("\nAwesome! We'll begin with hard!")
                level_selection = not True
                break
            else:
                print("Invalid input!\nPlease enter either e, m, or h. ")


        if level == 'e':
            print("Level = Easy You have 6 guesses \nGuess a number between 1-10.")
            guesses_left = 6
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == easy:
                    print("You got it right")
                    break
                else:
                    print("Thats wrong")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                if guesses_left == 0:
                    print("Game Over")

        if level == 'm':
            print("Level = Medium You have 4 guesses \nGuess a number between 1-20. ")
            guesses_left = 4
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == medium:
                    print("You got it right")
                    break
                else:
                    print("Thats wrong")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                if guesses_left == 0:
                    print('Game over')

        if level == 'h':
            print("Level = Hard You have 3 guesses \nGuess a number between 1-50.")
            guesses_left = 3
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == hard:
                    print("You got it right")
                    break
                else:
                     print("That's wrong")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                if guesses_left == 0:
                    print('Game Over')

        maybe_play = True
        while maybe_play:
            again = input("\nWould you like to play again?\nYes or No\n ")
            if again == 'No' or again == 'no':
                print('\nThank you for playing.\n Do come back again')
                maybe_play = not True
                play = not True
            elif again == 'yes' or again == 'Yes':
                print("\nNice, let's play\n")
                maybe_play = not True
                play = True
            else:
                print('Please enter either yes or no.')
                input()
                maybe_play = not True
                play = not True


guessing_game()
