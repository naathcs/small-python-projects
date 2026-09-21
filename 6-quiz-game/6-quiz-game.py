import tkinter as tk
from tkinter import ttk

import json
import random

# root
# root = tk.Tk()
# root.title('QUIZ GAME')

# Visual Frame
# frame = ttk.Frame(root, padding=5)
# frame.grid(row=0, column=0, sticky="nsew")

# json file import
with open("6-quiz-game/questions.json", mode="r", encoding="utf-8") as file:
    quiz_data = json.load(file)

# variables

score = 0
opts = ['A. ','B. ','C. ','D. ']


# Initial User page ttk

# Ask user name
def user_info():
    userName = input('Please enter your name: ')
    print(f'Welcome {userName}!\n')
# Ask quiz subject
# startGame = input('Would you like to start?')

# Quiz Logic
def quiz_questions():
    questionNumber = 0
    questionNumber += 1
    
    for q in quiz_data: 
            print(f'\n{questionNumber}. {q['question']}')
            questionNumber += 1
            loc=0
            for option in q['options']:
                print(f'{opts[loc]} - {option}')
                loc+=1



# User Answer
def user_input():

    userGuess = input('Your Answer: ').strip().upper()[0]
    

    

# Correct Answer
def check_answers():
    print()

# User Score
def count_score():
    print()

# Ask if user wants to play again (return to the quiz subject part of the code)

user_info()
quiz_questions()

# answer = input('Do You want to play again? (Y/N): ').strip().upper()[0]
# if answer == 'N':

# else:
#     print('Invalid Input! Please Try again.')

# TTK 
# title_label = ttk.Label(frame, text="Quiz Game", font=("Arial", 16))
# title_label.grid(row=0, column=0, pady=10)


# Run program