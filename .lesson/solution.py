import random

print("Welcome to rock, paper, scissors. Good luck!")

random_value = random.randint(1,3)
if random_value == 1:
  computer_choice = "Rock"
elif random_value == 2:
  computer_choice = "Paper"
elif random_value == 3:
  computer_choice = "Scissors"
else:
  print("Something went wrong with RANDOM")

choice = input("Rock, Paper, or Scissors? ")
print("The computer chooses " + computer_choice)

if choice == "Rock":
  if computer_choice == "Scissors":
    print("Rock smashes Scissors. You win!")
  elif computer_choice == "Paper":
    print("Paper covers Rock. You lose!")
  else:
    print("Rock and Rock. It's a draw.")
elif choice == "Paper":
  if computer_choice == "Scissors":
    print("Scissors cut Paper. You lose!")
  elif computer_choice == "Paper":
    print("Paper and Paper. It's a draw.")
  else:
    print("Paper covers Rock. You win!")
elif choice == "Scissors":
  if computer_choice == "Scissors":
    print("Scissors and Scissors. It's a draw.")
  elif computer_choice == "Paper":
    print("Scissors cuts Paper. You win!")
  else:
    print("Rock smashes Scissors. You lose!")
else:
  print("You have to enter Rock, Paper, or Scissors")