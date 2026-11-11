# Project Title
Password Generator application.


## Table of Contents
  - [Overview](#overview)
  - [Views](#views)
  - [Process Breakdown](#process-breakdown)
  - [How to Run](#how-to-run)
  - [Tutorial Source](#tutorial-source)
    - [Links](#links)
  - [Author](#author)

## Overview

The application runs for the user to generate a password that contains twelve characters, and hte characters must include upper and lower case, numbers and special characters as well. There are three buttons for the user to interact, to generate and clear the password, and to close the application.


## Views

<div align="center">
  <video width="350" height="" alt="" controls src="passwordGenerator.mp4" type="video/mp4"></video>
  <p>Password Generator Application</p>
</div>


## Process Breakdown

The libraries used in this application are the `secrets` and `string` for the password logic and `tkinter` for the visual of the application. Starting by creating the `Tk()` root, adding a title and a fixed size to prevent the user from resizing the window.

The `generate_password` function starts with the variable *alphabet* created and being assigned the three string instances merged. One for the letters, one for digits (numbers) and one for punctuation (special characters). After that, a **while loop** opens with a variable called *password*. This variable will receive a `join()` method with the `secrets` library and the `choice` function, all calling the *alphabet* variable to generate a random password with all the characters available in it. And the range set for the password is twelve characters, using a **for loop**. 

```
# Merged three modules with its constants 
alphabet = string.ascii_letters + string.digits + string.punctuation
```
```
# Generating the random password with the character in the 'alphabet' variable
password = ''.join(secrets.choice(alphabet) for i in range(12))
```

After the *password* variable is populated, an **if statement** will check the variable to make sure all the requirements are met. The statement will check for lower and upper case letters, at least two special characters and three number digits. If all those conditions are met, the **while loop** will break and content will be added to the label on screen for the user. 

The next function is called `clear_password()` and will reset the text set on the previous function, and visually cleaning the password content. And the last of three functions is the `close_app()`, that will close the window when clicked. 

The next section of the code contains the `tkinter` library items that creates the visual side of the code. The frame is the first one created to limit where all the content will be stored in, instead of scattering all over the root variable. Followed by the label that sets the title of the application using the *Label* class.

For the section where the password is shown when the user click the 'Generate Password' button, there is also a *Label* class. This particular item uses the **height** and **relief** parameters to create a visual section for the content and to avoid unnecessary resizing when an action is triggered. In this visual section, the generated password will appear when the user clicks the button, and will disappear when the user clicks the *Clear* button, and all withing the fixed area of the *Label* class.

The second to last section contains the code for the three buttons, where their `pack()` uses the same parameters for all to maintain standard sizes. All the three buttons uses the `ttk` import to visually show buttons that are close to the system being used when the application starts. And the last section contains the `mainloop()` to keep the entirety of the code open for the user to interact.


## How to Run

Download the file `passwordGenerator.py`.

Open your terminal and find the where the `passwordGenerator.py` file was downloaded, then follow the steps below.

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
python3 passwordGenerator.py
```

**NOTE:** The code will NOT run on the terminal, a window with the GUI application will open instead.


## Tutorial Source

### Links
These are the links that were used as reference and guide to adapt the original code to its current source.

- [Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html) - `secrets` and `string` libraries for the password generator.


## Author

- Developed by Nathalia Santos 🐉<br><br>
[![LinkedIn Badge](https://img.shields.io/badge/-Nathalia_Santos-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/naathcs/)](https://www.linkedin.com/in/naathcs/)