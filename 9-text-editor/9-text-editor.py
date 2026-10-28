import tkinter as tk
from tkinter import messagebox, ttk

# GUI Window
root = tk.Tk()
root.title('Your Favorite Editor')
root.geometry("700x750")

# Functions 
def save_file():
    pass

def load_file():
    pass

def close_file():
    root.destroy()

# Frames
frame1 = tk.Frame(root, width=650, height=700)
frame1.pack(padx=(10), pady=(25, 15))

buttonFrame = tk.Frame(frame1, width=630, height=50)
buttonFrame.pack(fill='x', pady=10, padx=10)

editorFrame = tk.Frame(frame1, width=630, height=600)
editorFrame.pack(fill='x', pady=10, padx=10)

# Labels
titleLable = tk.Label(root, text='Your Favorite Editor ®', anchor='center', fg='yellow', font=('Courier', 12, 'bold'))
titleLable.pack()

# Menu Buttons
btn_1 = ttk.Button(buttonFrame, text='Save', width=10, command=save_file)
btn_1.pack(fill='x',side=tk.LEFT)

btn_2 = ttk.Button(buttonFrame, text='Load File', width=10, command=load_file)
btn_2.pack(fill='x', side=tk.LEFT)

btn_3 = ttk.Button(buttonFrame, text='Close', width=10, command=close_file)
btn_3.pack(fill='x', side=tk.LEFT)

# Text Box
textBox = tk.Text(editorFrame,
                  width=100,
                  height=45,
                  wrap=tk.WORD)
textBox.pack()

# Other Actions



# RUN CODE
root.mainloop()