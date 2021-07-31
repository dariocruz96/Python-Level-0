import random

options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

while True:
    user_hand = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_hand == "q":
        break
    if user_hand not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_hand = options[random_number]
    print("Computer picked", computer_hand +".")

    if user_hand == "paper" and computer_hand == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_hand == "scissors" and computer_hand == "paper":
        print("You won!")
        user_wins += 1

    elif user_hand == "rock" and computer_hand == "scissors":
        print("You won!")
        user_wins += 1
    elif user_hand == computer_hand:
        print("Tie! No one wins.")
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins , "times!")
print("Computer won", computer_wins, "times!")
k=input("press close to exit") 
