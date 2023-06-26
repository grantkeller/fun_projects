import random

# Define options and rules
options = ["rock", "paper", "scissors"]
rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

# Get player's choice
print("Let's play Rock-Paper-Scissors!")
player_choice = input("Choose your weapon (rock, paper, or scissors): ").lower()

# Generate computer's choice
computer_choice = random.choice(options)

# Print choices
print(f"You chose {player_choice} and the computer chose {computer_choice}.")

# Determine winner
if player_choice == computer_choice:
    print("It's a tie!")
elif rules[player_choice] == computer_choice:
    print("You win!")
else:
    print("The computer wins!")