import secrets
import string

import tkinter as tk
from tkinter import ttk

#GUI
root = tk.Tk()
root.title('Password Generator')
root.geometry('400x500')

# Functions
def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation # Merged three categories


    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(12))
        if (any(c.islower() for c in password) # Check for lower case
            and any(c.isupper() for c in password) # Check for upper case
            and sum(c.isalnum() for c in password) >= 2 # Check for special characters
            and sum(c.isdigit() for c in password) >= 3): # Check for numbers
            break

    passwordText.config(text=f'Your Password is: \n\n {password} ')

def clear_password():
    passwordText.config(text='Generate you password\n\n')

def close_app():
    root.destroy()

# Frames
frame = tk.Frame(root, width=350, height=400)
frame.pack(padx=(10), pady=(25,15))

# Labels
lblTitle = tk.Label(frame, text='Password Generator', font=('Arial', 22, 'bold'))
lblTitle.pack(fill='x', padx=(5), pady=(15, 5), anchor='n')

# Password Box
passwordText = tk.Label(frame, text='Generate you password\n\n', justify='center', fg='yellow', height=5, relief='raised')
passwordText.pack(fill='x', anchor='center', padx=(5), pady=(5))

# Buttons
btn_1 = ttk.Button(frame, text='Generate Password', compound='center', command=generate_password)
btn_1.pack(fill='x', padx=(2), pady=(2,0), anchor='s')

btn_2 = ttk.Button(frame, text='Clear', compound='center', command=clear_password)
btn_2.pack(fill='x', padx=(2), pady=(2), anchor='s')

btn_3 = ttk.Button(frame, text='Close', compound='center', command=close_app)
btn_3.pack(fill='x', padx=(2), pady=(0,2), anchor='s')


# RUN CODE
root.mainloop()