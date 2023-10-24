#In this project you will be playing a game of rock-paper-scissors against the computer.
#The computer will randomly choose between rock, paper, and scissors. You will do the same.
#Then, the winner will be decided according to the following rules:
#Rock beats scissors
#Scissors beats paper
#Paper beats rock
#If both the computer and you make the same choice, it is a tie.
#You will be playing 5 rounds of the game. Whoever wins more rounds out of 5 is the winner of the game overall.

import random
rock = 0
paper = 0
scissors = 0

for i in range(3):
    print("Round " + str(i + 1) + ":")
    print("Rock, Paper, or Scissors?")
    choice = input()
    choice = choice.lower()
    computer = random.randint(1, 3)
    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "paper"
    else:
        computer = "scissors"
    print("Computer chooses " + computer + ".")
    if choice == "rock":
        if computer == "rock":
            print("It's a tie.")
        elif computer == "paper":
            print("Computer wins.")
            paper += 1
        else:
            print("You win.")
            rock += 1
    elif choice == "paper":
        if computer == "rock":
            print("You win.")
            paper += 1
        elif computer == "paper":
            print("It's a tie.")
        else:
            print("Computer wins.")
            scissors += 1
    elif choice == "scissors":
        if computer == "rock":
            print("Computer wins.")
            rock += 1
        elif computer == "paper":
            print("You win.")
            scissors += 1
        else:
            print("It's a tie.")
    else:
        print("Invalid input. You lose this round.")
