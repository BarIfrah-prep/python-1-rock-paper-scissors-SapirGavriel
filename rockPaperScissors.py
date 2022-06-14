# Rock Paper Scissors
# A code file structure:
# A line that starts with "#"  is a comment line (it will not be interpreted)
"""
If you ant to comment multiple lines, start and finish with three (3) double quotes (")
As you can see, this line is also a comment.

"""

# ----------------------------------------------------------------------------------------------------------------------
# Here you include all of your package imports (like randome and time packages wev'e discussed about) 
# ----------------------------------------------------------------------------------------------------------------------
import random

# ----------------------------------------------------------------------------------------------------------------------
# Here you will write all of the functions (for later stages of the course
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Here you write code :)
# ----------------------------------------------------------------------------------------------------------------------
"""
I'll give you the text inputs for this program, to make your lives a little easier.
In addition, and to make it simple to you, the input from the user will be an integer:
1 for ROCK
2 for PAPER
3 for SCISSORS
A text input describing the operation is unacceptable and will cost you with points.

A quick reminder of the rules:

ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins
SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win
PAPER(2) vs ROCK(1)      --> PAPER(2) wins

DO NOT ADD EXTRA OPTIONS (No lizard, no Spock.)
"""

# print the instructions for the user to see:
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")

# The game will run in a WHILE loop.
# The loop is infinite, and only the user has the power to stop it (when they say they don't want to play anymore)

while gameison:
    userChoice = input("Choose your Choice rock(1),paper(2),Scissors(3)")

    while userChoice != "1" and userChoice != "2" and userChoice != "3":
        print("invalid choice")
        userChoice = input("Choose your Choice rock(1),paper(2),Scissors(3)")
    else:
        computerChoice = random.randint(1,3)
        userChoice = int(userChoice)

        # case user choose rock
        if userChoice == 1 and computerChoice == 3:
            print("Hi, you won")
        elif userChoice == 1 and computerChoice == 2:
            print("Ho, you lose")
        elif userChoice == 1 and copmuterChoice == 1:
            print("its a draw")

        # case user choose paper
        if userChoice == 2 and computerChoice == 1:
            print("Hi, you won")
        elif userChoice == 2 and computerChoice == 3:
            print("Ho, you lose")
        elif userChoice == 2 and copmuterChoice == 2:
            print("its a draw")

        # case user choose scissors
        if userChoice == 3 and computerChoice == 2:
            print("Hi, you won")
        elif userChoice == 3 and computerChoice == 1:
            print("Ho, you lose")
        elif userChoice == 3 and copmuterChoice == 3:
            print("its a draw")


        # Asking the user if he wants to continue

        answerRequest = input("Do you want continue? y/n").lower()
        continueRequest = True

        while answerRequest != "y" and answerRequest != "n":
            print("invalid answer")
            answerRequest = input("Do you want continue? y/n").lower()

        if answerRequest == "y":
            continue
        elif answerRequest == "n":
            print("thank you for playing the game!")
            gameison = False


