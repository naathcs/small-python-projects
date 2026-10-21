# Project Title
A simple tic tac toe game.

## Table of Contents
  - [Overview](#overview)
  - [About](#about)
  - [Process Breakdown](#process-breakdown)
  - [How to Run](#how-to-run)
  - [Tutorial Source](#tutorial-source)
    - [Links](#links)
  - [Author](#author)

## Overview

A simple tic tac toe game where the games starts with player 1 being the `X` and the player 2 being the `O`. On the terminal each player will type the location where they would like to add they tag on the board from 1 through 9 and the number will be replaced by either an `X` or an `O`. The players will add tag until one of them wins or the game is tied. The game is also designed to not let the user replace its opponent tag.


## Process Breakdown

The process was followed by the tutorial available in the [Links](#links) section. The games is created following the tutorial from beginning to end, with the only difference from the original video being that only one file is created for the entire code, while in the video, two different files are created, so one can be imported to the main one.

Following the process was easy and comprehensible, maintaing its beginner level status.

A couple things that I notice that could be improved to level up the skill of the exercise is the fact that there is a lot of writing for the board location and to check the win of a player, which makes the code extensive to read. Also, the several `if statements` in the code, if not correctly added, could generate an error. 

One other thing to notice is that the `os import` that is used to clean the screen and avoid the repetition of the board while playing, shows as *soft deprecated* in some locations, but it is not officially deprecated.

```
os.system('cls' if os.name == 'nt' else 'clear')
```

The game will terminate once there is a winner or a tie and do not offer the option to start again, neither the option for the user to choose with tag to use 'X' or 'O'. And the user will always play with somebody, there is not an option to play alone, making the second player code written to be automatically inputted.

I chose to follow the tutorial instead of adapting ot my personal style, to practice my ability to understand a code that is already complete and what each part is able to do without any adaptions form its original source.


## How to Run

Download the file `7-tictactoe.py`.

Open your terminal and find the where the `7-tictactoe` folder was downloaded, then follow the steps below.

```
# (Optional)Create a Virtual Environment
python3 -m venv venv
```
```
# (Optional)Active Virtual Environment
source .venv/bin/activate
```
```
# Run the Code
python3 7-tictactoe.py
```


### Links
This is the link that was used as reference and guide to adapt the original code to its current source.

- [Beginner Python Project From Scratch: Tic Tac Toe](https://www.youtube.com/watch?v=Q6CCdCBVypg&t=14s) - Video used as reference to create the game.


## Author

- Developed by Nathalia Santos 🐉<br><br>
[![LinkedIn Badge](https://img.shields.io/badge/-Nathalia_Santos-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/naathcs/)](https://www.linkedin.com/in/naathcs/)