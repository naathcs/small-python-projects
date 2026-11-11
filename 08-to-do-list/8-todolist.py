import tkinter as tk
from tkinter import ttk, messagebox

# GUI Root
root = tk.Tk()
root.title('To Do List App')
root.resizable(False, False) # Prevent manually resizing the window
root.geometry("300x450")

# Functions
def add_task():
    task = entry_task.get()
    if task != '':
        listbox_task.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title='Warning!', message='You need to enter a task.')

def remove_task():
    try:
        select_task = listbox_task.curselection()[0]
        listbox_task.delete(select_task)
    except:
        tk.messagebox.showwarning(title='Warning!', message='Please select a task to delete.')

def clear_list():
    if listbox_task.size() != 0:
        listbox_task.delete(0, tk.END)
    else:
        tk.messagebox.showinfo(title='Oops!', message='The list is empty!')

def close_app():
    root.destroy()


# GUI Frame
frame = tk.Frame(root)
frame.pack()

# Title
lbl = tk.Label(
    frame ,
    text='To Do List',
    font=('Times New Roman',27, 'bold'),
    width=15,
    height=2,
    fg='lightblue',
    padx=5,pady=5)
lbl.pack(padx=5,pady=5, fill='x')


# Box List
listbox_task = tk.Listbox(frame, height=10, width=25)
listbox_task.pack(pady=5, fill='x')

entry_task = tk.Entry(frame, width=25, relief=tk.GROOVE)
entry_task.pack(fill='x')
entry_task.bind("<Return>", lambda event: add_task())

# Buttons
btn_1 = ttk.Button(frame, text='Add Task', width=20, command=add_task)
btn_1.pack(fill='x')

btn_2 = ttk.Button(frame, text='Remove Task', width=20, command=remove_task)
btn_2.pack(fill='x')

btn_3 = ttk.Button(frame, text='Clear List', width=20, command=clear_list)
btn_3.pack(fill='x')

btn_4 = ttk.Button(frame, text='Close', width=20, command=close_app)
btn_4.pack(fill='x')

# RUN CODE
root.mainloop()