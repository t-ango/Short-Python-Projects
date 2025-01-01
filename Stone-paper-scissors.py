'''
This program simulates a game of Rock-Paper-Scissors between the user and the computer.

- **Game Rules**:
  - Rock (stone) beats Scissors.
  - Scissors beats Paper.
  - Paper beats Rock.

- **Process**:
  1. The computer randomly selects its choice (0 for Paper, 1 for Scissors, 2 for Stone).
  2. The user is prompted to input their choice (0 for Paper, 1 for Scissors, 2 for Stone).
  3. The computer's choice is revealed to the user.

- **Outcome Determination**:
  - If both the user and the computer make the same choice, it's a tie.
  - If the computer's choice beats the user's choice (as per the game rules), the user loses.
  - If the user's choice beats the computer's choice, the user wins.
  - If the user inputs an invalid choice, the program warns against cheating.

- **Output**:
  - The program announces the computer's choice.
  - It declares the outcome as "It's a tie!", "You won!", or "You lost!" depending on the result.
'''
import random
computerGuess = random.randint (0,2)
stone = 2
scissors = 1
paper = 0

userGuess= eval(input("You turn! Enter 0 for paper, 1 for scissors, 2 for stone:"))

if computerGuess == stone:
    print ("Computer got stone!")
elif (computerGuess == scissors):
    print ("Computer got scissors!")
else:
    print ("Computer got paper!")

if computerGuess == userGuess:
    print ("Its a tie!")
elif (computerGuess == stone and userGuess == scissors
      or computerGuess == scissors and userGuess == paper
      or computerGuess == paper and userGuess == stone):
    print ("You lost!")
elif (computerGuess == stone and userGuess == paper
      or computerGuess == scissors and userGuess == stone
      or computerGuess == paper and userGuess == scissors):
    print ("You won!")
else:
    print ("No cheating! Enter correct nummber")