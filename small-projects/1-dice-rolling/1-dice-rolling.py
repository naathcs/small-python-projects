## import random generator
import random

## loop statement for endless code
while True: ## while statement is true keep running code
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        qtd = int(input('How many dices do you want to roll? ')) ## Optional enhancement of the original code to choose how many dice the user wants to roll
        if qtd == 1:
            die_roll = random.randint(1, 6)
            print(f'Roll: {die_roll}')
        elif qtd > 1: 
            roll_qtd = 1
            while roll_qtd <= qtd:
                die_roll = random.randint(1, 6)
                print(f' Roll {roll_qtd}: ({die_roll})')
                roll_qtd+=1
        else:
            print('Invalid Number. Please try again.')
    elif choice == 'n':
        print(f'Thank you for playing!')
        break
    else:
        print('Invalid choice! Please try again.')