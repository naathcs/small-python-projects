import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
emojis = {ROCK:'🪨', PAPER:'📃', SCISSOR:'✂️'}
choices = tuple(emojis.keys()) ## Using tuples to avoid repetition in the code

## Using Modularization 
# No Enhancements were added in this code.

def get_user_choice():
    while True: 
        user_choice = input('What is your choice (r/p/s)? ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid Commmand. Please try again!')

def print_result(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSOR) or
        (user_choice == SCISSOR and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print('You win!')
    else:
        print('You lose!')

def play_games():
    while True:
        
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        print_result(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)
        
        continue_game = input('Do you want to continue the game? (y/n): ').lower()
        if continue_game == 'n':
            break

play_games()