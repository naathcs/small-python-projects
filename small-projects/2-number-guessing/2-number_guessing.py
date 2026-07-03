## import random library
import random

## Guessing Number Code

# Enhancement 1 - allow the user to choose the range of the number for the guessing game
print(' ** Choose a range ** ')
first_number = int(input('Add the First Number: '))
second_number = int(input('Add the Second Number: '))
number_to_guess = random.randint(first_number, second_number)

# Enhancement 2 - limit the number of guesses
number_of_guesses = int(input('Choose a number between 1 and 9: '))
print(f'You have {number_of_guesses} to find the correct value. Good Luck! \n')
guess_count = 0

## original code
while True:
    try:
        if number_of_guesses > guess_count: # Enhancement 2
            guess = int(input(f'Guess the number (between {first_number} and {second_number}): '))
            if guess > second_number:
                print('Number out of range. Please try again.')
            elif guess < number_to_guess:
                print('Too Low!')
            elif guess > number_to_guess:
                print('Too High!')
            else:
                print(f'Congratulations! You guessed the number. \n It took you {guess_count+1} attemps')
                break
            guess_count+=1
        else:
            print(f'You ran out of guesses. The correct number was {number_to_guess}')
            break
    except ValueError:
        print('Please enter a valid number')
