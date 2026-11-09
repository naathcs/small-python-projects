# Project Title

Password strength checker application.


## Table of Contents
  - [Overview](#overview)
  - [Views](#views)
  - [Process Breakdown](#process-breakdown)
  - [How to Run](#how-to-run)
  - [Tutorial Source](#tutorial-source)
    - [Links](#links)
  - [Author](#author)

## Overview

The application is designed for the user to add a password, and check the strength. Having a requirements options for them to also check what is advised to add to the password for it to be strong. The user is also able to clean the input and reset it to add a new password to check it. 


## Views

<div align="center">
  <video width="350" height="" alt="" controls src="password-check.mp4" type="video/mp4"></video>
  <p>Password Strength Checker application working</p>
</div>


## Process Breakdown

This project started by getting the libraries imports `tkinter` for the visual side and the `password_strength` for the logical check of the application. For the `tkinter`, the *ttk* was imported for the buttons visual according to each OS system that the application is running, and the *message box* for the action of one of the buttons and to alert the user in case something goes wrong. And from the `password_strength` library, both *PasswordPolicy*, for the password requirements, and the *PasswordStats*, that checks the password statistically and its complexicity by returning a value between 0.00 and 0.99, where the higher the number, the stronger the password. 

Starting with the GUI root and the title of the window and a set size to prevent the user from resizing the window. The next section is for the functions that are going the be used as the actions of the buttons. The first function is the `password_check()`, where the requirements for the function are added with the *PasswordPolicy* class, allowing requirements such as: **length**, **special characters**, **numbers** and the minimum amount for each requirement in the password.

```
def password_check():
    policy = PasswordPolicy.from_names(
        length=12,  # min length: 12
        uppercase=1,  # need min. 1 uppercase letters
        numbers=2,  # need min. 2 digits
        special=1  # need min. 1 special characters
    )
```

After that, the password is stored in a variable called `content`, then this variable is used to check the `PasswordStats()` and this statistic value, that is a number between **0.00** and **0.99** where the higher the number, the stronger the password, is stored in another variable called `stats`. Thi variable is used in an **if statement** inside a **try except** statement. The **if statement** checks if the stats number is below, between or above a certain value, if so, the label `-- Strength Meter --` that is on the window will be replaced by a message letting the user know wether their password is weak, needs improvement or if it is a good an secure one.

The next function is the `password_requirements()`, that when clicked by the user, a pop-up window created with the `tkinter messagebox` appears with all the suggestions for a strong password. Even thought the button and the funtion have *requirements* in its name, they suggestions for the user since nothing in the code prevents the password from containg or not what is specified in the list. 

The function `clear_password()` will get the content from the Entry box, store it in a variable and analyze it with an **if statement**, where it is using the `strip()` to identify if there is anything in the box, if there is, the content is deleted and the label showing the `-- Strength Meter --` is reseted to its original state. If there is nothing in the box, a pop-up message appears letting the user know that the box is empty. And the last function is the `close_app()` function that closes the application.

The next section contains the `tkinter` library usage where the frame is created to populate the root window, containing padding vertically and horizontally. Inside the frame, three labels are created, one containing the title of the program, one named `passwordStatus` which is the variable used inside both `password_chech()` and `clear_password()` functions to either print an information to the user or to reset its content on screen. The third labels is the a fixed text to guide the user inside the window.

Below the labels is the Entry box for the user to type in their password. The password is stored in the `passwordText` variable that is used in the `password_chech()` to check the policies on the password and how strong it is, and the  `clear_password()` to verify if the box is empty before running an action.

The last section of the code contains the buttons that follows the same order of the functions in the beginning of the code, from checking the password to closing the application. All the four buttons have a few standard `pack()` arguments to avoid visual mismatches, with buttons two and three having the vertical padding different from the buttons one and four. And lastly, the `mainloop()` argument at the end of the code. 


## How to Run

Download the file `passwordStrengthChecker.py`.

Open your terminal and find the where the `passwordStrengthChecker.py` file was downloaded, then follow the steps below.

```
# Create a Virtual Environment
python3 -m venv venv
```
```
# Active Virtual Environment
source .venv/bin/activate
```
```
# Install the library used in this application in your virtual machine
pip install password-strength
```
```
# Run the Code
python3 passwordStrengthChecker.py
```

**NOTE:** The code will NOT run on the terminal, a window with the GUI application will open instead.


## Tutorial Source

### Links
These are the links that were used as reference and guide to adapt the original code to its current source.

- [Password Strength Library](https://pypi.org/project/password-strength/) - Password Strength library that is used in the application.
- [Status Bar](https://www.youtube.com/watch?v=Qlg6ZHG7rxI&t=484s) - Applying a manual status bar in the GUI with `tkinter`
- [Tkinter messagebox prompts](https://docs.python.org/3/library/tkinter.messagebox.html) - `messagebox` paramenters for the code.

## Author

- Developed by Nathalia Santos 🐉<br><br>
[![LinkedIn Badge](https://img.shields.io/badge/-Nathalia_Santos-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/naathcs/)](https://www.linkedin.com/in/naathcs/)