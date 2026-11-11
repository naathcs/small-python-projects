import json
import random


# json file import
with open("6-quiz-game/questions.json", mode="r", encoding="utf-8") as file: #Using relative path to find the file and open it.
    quiz_data = json.load(file)

# variables
score = 0
opts = ['A. ','B. ','C. ','D. ']
user_guesses = []
correct_answers = []

# tracking active questions
current_question = None


# Ask user name
def user_info():
    global userName 
    userName = input('Please enter your name: ')
    print(f'Welcome {userName}!\n')

# User Answer
def user_input():

     # Loop to limit the allowed typed characters
    while True:
        user_guess = input('\nEnter (A, B, C, D): ').strip().upper()[:1] # limit character to one

        if user_guess in ('A','B','C','D'):
            print(f'Choice Confirmed: {user_guess}')
            print('-' * 30)
            user_guesses.append(user_guess) # store user guesses
            return user_guess # Return the user guess to be used if valid
        else:
            print('\nInvalid Entry. Please try again.')

# Correct Answer
def check_answers():
    global score # get score variable

    user_guess = user_input()
    
    correct_answer = current_question['correctAnswer'] # get the correct answer to verify the user's answer
    answer_index = current_question['options'].index(correct_answer) # Find the location of the answer in the array
    correct_letter = opts[answer_index].strip().rstrip('.') # clean variable

    correct_answers.append(correct_letter) # Store correct answers

    if user_guess == correct_letter:
        print("Correct!")
        print('-' * 30)
        score += 1
        
    else:
        print(f'Incorrect. The correct answer was {correct_letter}.')
        print('-' * 30)


# Quiz Logic
def quiz_questions():
    global current_question
    questionNumber = 1

    # Getting a limit of 5 random questions from the json file
    selected_questions = random.sample(quiz_data, min(5, len(quiz_data)))
    # Print Questions
    for q in selected_questions:
        current_question = q
        print(f'\n{questionNumber}. {q['question']}')
        questionNumber += 1

        # Print Question 
        loc = 0
        for option in q['options']:
            print(f'{opts[loc]} - {option}')
            loc += 1

        check_answers()

        
# User Score
def user_score():

    print('\n\n')
    print('-' * 30)
    print('-- RESULTS --')
    print('-' * 30)

    print(f"{userName}'s Guesses: {user_guesses}")
    print(f'Correct Answers: {correct_answers}')

    # Calculate user score
    total_questions = len(user_guesses)
    if total_questions > 0:
        finalScore = int((score / total_questions) * 100)
    else:
        finalScore = 0

    print(f'Your final score is: {finalScore}% ({score}/{total_questions})')



# Run program
def run_all(): 
    while True:
        user_info()
        quiz_questions()
        user_score()

        print(f'{userName}, would you like to play again? (Y/N): ')
        answer = input().strip().upper()[:1]

        while answer not in ('Y','N'):
                print('\nInvalid Entry. Please try again.')             
                print('\nWould you like to play again? (Y/N):')
                answer = input().strip().upper()[:1]
        
        if answer == 'N':
                break

# Run the program
run_all()