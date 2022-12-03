# Write your solution below the starter code
# Follow the instructions in the tab to the right

#import random
import random
# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")
possible_actions = ["rock", "paper", "scissors"]

# Make a choice for the computer player
computer_action = random.choice(possible_actions)

# Get a choice from the user
user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]

# Compare the user and computer choice
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

# Print the right message, based on the choices
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a draw")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose!")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose!")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose!")