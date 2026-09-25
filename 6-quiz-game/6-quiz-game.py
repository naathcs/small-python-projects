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

# Ask user name
def user_info():
    userName = input('Please enter your name: ')
    print(f'Welcome {userName}!\n')


# Quiz Logic
def quiz_questions():
    questionNumber = 1

    # get questions to randomize 
    question_list = [
        item for item in quiz_data if item.get('question')
    ]

    # Print questions from JSON file
    for q in question_list[:5]: # limit the amount of prints to 5
        
        global random_question
        random_question =  random.choice(question_list) # randomize question list
        print(f'\n{questionNumber}. {random_question['question']}')
        questionNumber += 1
        loc=0
        for option in random_question['options']:
            print(f'{opts[loc]} - {option}')
            loc+=1

        check_answers()
        

# User Answer
def user_input():
    user_guess = input('\nEnter (A, B, C, D): ').strip().upper()[:1] # limit character to one
    print(f'Choice Confirmed: {user_guess}')
    print('-' * 30)

    user_guesses.append(user_guess) # store user guesses

    return user_guess


# Correct Answer
def check_answers():

    user_guess = user_input()
    
    correct_answer = random_question['correctAnswer'] # get the correct answer to verify the user's answer
    answer_index = random_question['options'].index(correct_answer) # Find the location of the answer in the array
    correct_letter = opts[answer_index].strip().rstrip('.') # clean variable

    correct_answers.append(answer_index) # Store correct answers

    global score # get score variable

    if user_guess == correct_letter:
        print("Correct!")
        print('-' * 30)
        score += 1
        
    else:
        print(f'Incorrect.')
        print('-' * 30)

    return score
        
# User Score
def user_score():

    score

    print('\n\n')
    print('-' * 30)
    print('-- RESULTS --')
    print('-' * 30)

    print(f'Guesses: {user_guesses}')
    print(f'Correct Answers: {c}')

    # reasign score to a percentage value
    finalScore = int(score / len(questionNumber) * 100)
    print(f'Your score is: {finalScore}%')


# Run program
def run_all(): 
    user_info()
    quiz_questions()
    user_score()

run_all()