# TODO: Develop a console-based Rock Paper Scissors Lizard Spock game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Scissors decapitate lizard
# - Scissors cuts paper
# - Paper covers rock 
# - Rock crushes lizard 
# - Lizard poisons Spock 
# - Spock smashes scissors 
# - Lizard eats paper 
# - Paper disproves Spock 
# - Spock vaporizes rock 
# - Rock crushes scissors
# Include user input for selecting options and display game results.

import random

choices = ["rock", "paper", "scissors", "lizard", "spock"]
computer_choice = random.choice(choices)

user_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ")

if user_choice not in choices:
    print("Invalid choice. Please select from rock, paper, scissors, lizard, or spock.")
else:
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or \
         (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or \
            (user_choice == "rock" and (computer_choice == "lizard" or computer_choice == "scissors")) or \
            (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or \
            (user_choice == "spock" and (computer_choice == "scissors" or computer_choice == "rock")):
        print("You win!")
    else:
        print("Computer wins!")

        
    
