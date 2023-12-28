import random

def rock_paper_scissors(user_choice):
    valid_choices = ["rock", "paper","scissors"]
    computer_choice = random.choice(valid_choices)

    if user_choice not in valid_choices:
       return f"Invalid Choice, please input: 'Rock', 'Paper' or 'Scissors'"
    if computer_choice == user_choice:
        return f"I Pick, {computer_choice} \n It's a tie!!"
    elif (computer_choice == "rock" and user_choice == "paper") or \
        (computer_choice == "scissors" and user_choice == "rock") or \
        (computer_choice == "paper" and user_choice =="scissors"):
        return f"I Pick, {computer_choice} \n You Win!"
    else:
        return f"I Pick, {computer_choice} \n You Lose!"
    
user_input = rock_paper_scissors(input("Rock, Paper or scissors? ").lower())
print(user_input)
