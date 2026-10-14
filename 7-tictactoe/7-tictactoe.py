import os

# Location Dictionary
spots = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

playing = True
complete = False
turn = 0
prev_turn = -1

# Draw Board
def board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

# Check turns
def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'

# Check Wins
def check_for_win(spots):
    if (spots[1] == spots[2] == spots[3]) \
        or (spots[4] == spots[5] == spots[6]) \
        or (spots[7] == spots[8] == spots[9]):
        return True
    elif (spots[1] == spots[4] == spots[7]) \
        or (spots[2] == spots[5] == spots[8]) \
        or (spots[3] == spots[6] == spots[9]):
        return True
    elif (spots[1] == spots[5] == spots[9]) \
        or (spots[3] == spots[5] == spots[7]):
        return True
    else:
        return False


# Call Game
while playing:
    # Reset screen (not repeat the board)
    os.system('cls' if os.name == 'nt' else 'clear')
    board(spots)

    # Check invalid entry
    if prev_turn == turn:
        prev_turn('Invalid spot selected, please pick another')
    prev_turn = turn
    # Print Player's turn
    print('Player ' + str((turn % 2) + 1) + "'s turn: Pick your spot or press Q to quit.")

    # Get input from player
    choice = input()

    #stop game at any time
    if choice == 'q':
        playing = False
    # Check if the user adds a valid input
    elif str.isdigit(choice) and int(choice) in spots:
        # Check if the spot is taken
        if not spots[int(choice)] in {'X','O'}:
            # Update board if input is valid
            turn+=1
            spots[int(choice)] = check_turn(turn)

    # Check if the game ended
    if check_for_win(spots): 
        playing, complete = False, True
    if turn > 8:
        playing = False

# Out of Loop
# Print Games Results
os.system('cls' if os.name == 'nt' else 'clear')
board(spots)

# Check Winner
if complete:
    if check_turn(turn) == 'X':
        print('Player 1 Wins!')
    else:
        print('Player 2 Wins!')
else:
    print("No Winner. It's a tie!")

print('Thank you for playing!')
