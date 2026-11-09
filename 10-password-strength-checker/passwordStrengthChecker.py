# libraries
import tkinter as tk
from tkinter import ttk, messagebox

from password_strength import PasswordPolicy, PasswordStats

# GUI Run
root = tk.Tk()
root.title('Password Strength Check')
root.geometry('400x500')

# Functions
def password_check():
    policy = PasswordPolicy.from_names(
        length=12,  # min length: 12
        uppercase=1,  # need min. 1 uppercase letters
        numbers=2,  # need min. 2 digits
        special=1  # need min. 1 special characters
    )

    content = passwordText.get()

    stats = PasswordStats(content)

    try:
        if stats.strength() <= 0.333:
            passwordStatus.config(text='The password is weak! 😭')
        
        elif stats.strength() > 0.333 and stats.strength() <= 0.666:
            passwordStatus.config(text='The password needs improvement. 😐')
        else:
            passwordStatus.config(text='The password is STRONG! 😊')
    except Exception:
        passwordStatus.config(text=f'-- Strength Meter --')
        messagebox.showerror(title='Ops!', message='Something does not look right.')

def password_requirements():
    messagebox.showinfo(title='You Need', message='Minimum Length: 12 characters\nUpper Case: 1\nNumbers: 2\nSpecial Characters: 1', icon='info')

def clear_password():
    content = passwordText.get()
    
    if content.strip():
        passwordText.delete(0, tk.END)
        passwordStatus.config(text=f'-- Strength Meter --')
    else:
        messagebox.showinfo(title='All Clear', message='Nothing to delete')

def close_app():
    root.destroy()

# Frames
frame = tk.Frame(root, width=350, height=450)
frame.pack(padx=(10), pady=(25, 15))

# Label

lblTitle = tk.Label(frame, text='Password Strength \nChecker', font=('Arial', 30, 'bold'), fg='dark green')
lblTitle.pack(fill='x', padx=(10), pady=(10, 25))

passwordStatus = tk.Label(frame, text='-- Strength Meter --', anchor='n', relief='flat', bd=1)
passwordStatus.pack(fill='x', side='top', ipady=5, padx=(10), pady=(10))

lblText = tk.Label(frame, text='Enter your password below:', font=('Arial', 12))
lblText.pack(padx=(10), pady=(10))


# Text Box
passwordText = tk.Entry(frame, justify='center', )
passwordText.pack(fill='x', padx=(10), pady=(10))


# Buttons
btn_1 = ttk.Button(frame, text='Check Password', command=password_check)
btn_1.pack(fill='x', padx=(10), pady=(10, 0))

btn_2 = ttk.Button(frame, text='Requirements', command=password_requirements)
btn_2.pack(fill='x', padx=(10), pady=(2))

btn_3 = ttk.Button(frame, text='Clear', command=clear_password)
btn_3.pack(fill='x', padx=(10), pady=(2))

btn_4 = ttk.Button(frame, text='Close', command=close_app)
btn_4.pack(fill='x', padx=(10), pady=(0, 10))


#RUN CODE
root.mainloop()