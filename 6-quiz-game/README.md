# Quiz Game
A small pop quiz gamewith multiple choice answers and score counting.

## Table of Content 
- [Overview](#overview)
- [View](#view)
- [Process Breakdown](#process-breakdown)
  - [How to Run](#how-to-run)
- [Links](#links)
- [Author](#author)

## Overview

The games is designed to be visually simple and intuitive for any user. There are 5 questions and 4 options of answer for each question. 
The goalof the quiz is that, each time the program runs, five random questions will show up to the user, one at a time, and the options to answer will also be shown in a random position to avoid the user from memorizing the answers. At the end the score will be shown and a question to wheather the user would like to play again, and the answer will either run the program again or terminate it.

## View

<div align="center">
  <img width="550" height="300" alt="" src=""/>
</div>

## Process Breakdown

Starting by creating a `JSON` file with the questions that will be used in the quiz game. Once all the questions are in the file, the same is loaded into the program.
The program will start by asking the user's name and welcoming it to the game along with a button to start the game or terminate it.



Once the game is complete the user's score will show up on screen. A question will alos show up asking if the user would like to play it again, if the answer is yes, the program will run again from the beginning, and if the answer is no, the program terminates.


#### How to Run

Follow this steps if you do not have a virtual envrionment or the necessary libraries to run the code.

Open your terminal and find the folder where the Python file was downloaded, then follow the steps below.

```
# Create a Virtual Environment
python3 -m venv venv
```
```
# Active Virtual Environment
source .venv/bin/activate
```

```
# Run the Code
python3 6-quiz-game.py
```

## Links

- [Tkinter Usage](https://www.youtube.com/watch?v=epDKamC-V-8&t=1114s) - Understanding how to use the tkinter library.
- [JSON Files](https://www.youtube.com/watch?v=iiADhChRriM&t=170s) - Creating a JSON file.
- [Generate Randoms](https://docs.python.org/3/library/random.html) - Generate pseudo-random number for various distributions.
- [Fixinf JSON Call Error](https://stackoverflow.com/questions/22282760/filenotfounderror-errno-2-no-such-file-or-directory) - Understanding what triggered the error when trying to call the JSON file into the code.

## Author 

- Developed by Nathalia Santos 🐉<br><br>
[![LinkedIn Badge](https://img.shields.io/badge/-Nathalia_Santos-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/naathcs/)](https://www.linkedin.com/in/naathcs/)