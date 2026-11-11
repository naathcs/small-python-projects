import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.filedialog import asksaveasfile, askopenfile

# GUI Window
root = tk.Tk()
root.title('Your Favorite Editor')
root.geometry("700x750")

# Functions 
def new_file():

    content = textBox.get("1.0", "end-1c") # Get content from text box
    
    if content.strip():
        response = tk.messagebox.askyesno(message='Did you save your file?')
        if response:
            textBox.delete(1.0, tk.END)
        else:
            response2 = tk.messagebox.askyesno(message='Do you want to save your file?')
            if response2:
                save_file()
            else:
                textBox.delete(1.0, tk.END)
    else:
        textBox.delete(1.0, tk.END)

def save_file():
    file = asksaveasfile(
        mode='w',
        defaultextension='.txt',
        title='Untitle File'
    )

    if file == None:
        return

    textBoxContent = textBox.get('1.0', 'end-1c') # Get content from text box

    file.write(textBoxContent)
    file.close()

    tk.messagebox.showinfo(message='Your file has been saved!')

def load_file():
    try:
        file = askopenfile(
            mode='r',
            title='Select a file...',
            filetypes=[
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*"),
            ("Document Files", "*.doc")]
        )

        if file:
            content = file.read()
            textBox.delete(1.0, tk.END)
            textBox.insert(1.0, content)
            file.close()
        else:
            tk.messagebox.showinfo(message='No file selected.')

    except Exception as e:
        tk.messagebox.showwarning(title='Error', message=f'Failed to open file {file.name}')

def close_file():

    content = textBox.get("1.0", "end-1c")# Get content from text box

    if not content.strip():
        root.destroy()
    else:
        reply = tk.messagebox.askyesno(message='Did you save your file?')
        if reply:
            root.destroy()
        else:
            reply2 = tk.messagebox.askyesno(message='Do you want to save your file?')
            if reply2:
                save_file()
            else:
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
btn_1 = ttk.Button(buttonFrame, text='New File', width=10, command=new_file)
btn_1.pack(fill='x', side=tk.LEFT)

btn_2 = ttk.Button(buttonFrame, text='Save As', width=10, command=save_file)
btn_2.pack(fill='x',side=tk.LEFT)

btn_3 = ttk.Button(buttonFrame, text='Load File', width=10, command=load_file)
btn_3.pack(fill='x', side=tk.LEFT)

btn_4 = ttk.Button(buttonFrame, text='Close', width=10, command=close_file)
btn_4.pack(fill='x', side=tk.LEFT)

# Text Box
textBox = tk.Text(editorFrame,
                width=100,
                height=45,
                wrap=tk.WORD)
textBox.pack()


# RUN CODE
root.mainloop()