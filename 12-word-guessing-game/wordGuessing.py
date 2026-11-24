import json
import random
import tkinter as tk

from tkinter import ttk

# callling function
def main():
    app = Application()
    app.mainloop()


# Logical Class
class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Guessing Game')
        self.geometry('600x600')

        # #import JSON
        with open("12-word-guessing-game/words.json", mode="r", encoding="utf-8") as file: #Using relative path to find the file and open it.
            self.words_data = json.load(file) # Access the content by the controller

        # Screens Location
        container = ttk.Frame(self) # Create frame inside the main windows
        container.pack(fill='both', expand=True) # windows in full screen

        # Store screens
        self.frames = {} # Dictionary for the screens

        # For Loop for the screens
        for Page in (startPage, categoryPage, gamePage):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky='nsew') # Make every screen is on the same position

        # Show Main Screen
        self.show_frame(startPage)

    # Switch Screens
    def show_frame(self, page):

        frame = self.frames[page]
        frame.tkraise() # Put screen in front of the others

    # Check category chosen for the game
    def start_game(self, category):

        # Check if the selection is in the JSON file
        for item in self.words_data:
            if item['category'] == category: # Check which category is selected
                selected_word = item['options']
                game_page = self.frames[gamePage]
                game_page.load_category(category, selected_word)

                # show Game Page
                self.show_frame(gamePage)
                break

# Starting Page
class startPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller # Reference to Application

        # Game Title
        self.titleLabel = tk.Label(self, text=f'Welcome Player!', font=('Helvetica', 20, 'bold'))
        self.titleLabel.pack(pady=20, fill='both', anchor='center')

        # Buttons
        self.startButton = ttk.Button(self, text='Start Game', command=lambda: controller.show_frame(categoryPage))
        self.startButton.pack(fill='x', padx=15, pady=(15,2), anchor='n')

        self.closeButton = ttk.Button(self, text='Close Game', command=controller.destroy)
        self.closeButton.pack(fill='x', padx=15, pady=(15,2), anchor='n')

# Category Page
class categoryPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller # Reference to Application

        # Game Title
        self.titleLabel = tk.Label(self, text='Choose a Category', font=('Helvetica', 20, 'bold'))
        self.titleLabel.pack(pady=20, fill='both')

        # Buttons
        self.cat1Button = ttk.Button(self, text='Countries', command=lambda: controller.start_game('Countries'))
        self.cat1Button. pack(fill='x', padx=15, pady=(15,2), anchor='n')

        self.cat2Button = ttk.Button(self, text='Car Brands', command=lambda: controller.start_game('Car Brands'))
        self.cat2Button.pack(fill='x', padx=15, pady=(2), anchor='n')

        self.cat3Button = ttk.Button(self, text='Dinosaurs', command=lambda: controller.start_game('Dinosaurs'))
        self.cat3Button.pack(fill='x', padx=15, pady=(2), anchor='n')

        self.cat4Button = ttk.Button(self, text='Back to Main', command=lambda: controller.show_frame(startPage))
        self.cat4Button.pack(fill='x', padx=15, pady=(2,15), anchor='n')

# Game Page
class gamePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.current_word = None

        # Game Title
        self.titleLabel = tk.Label(self, text="Let's Start!", font=('Helvetica', 20, 'bold'))
        self.titleLabel.pack(pady=20, fill='both')

        self.categoryLabel = tk.Label(self, text='', font=('Helvetica', 16, 'bold'))
        self.categoryLabel.pack(pady=10, fill='both')

        # Word display
        self.wordGuessing = tk.Label(self, text='', font=('Helvetica', 20, 'bold'))
        self.wordGuessing.pack(pady=10)

        # Letter input
        self.textLabel = tk.Label(self, text='Enter a Letter', font=('Helvetica',12))
        self.textLabel.pack(fill='both')

        self.letterEntry = ttk.Entry(self)
        self.letterEntry.pack(pady=10)

        # Check letter button
        self.enterLetter = ttk.Button(self, text='Enter Letter', command=self.check_letter)
        self.enterLetter.pack(fill='x', padx=15, pady=(2))

        # Feedback
        self.feedbackLabel = tk.Label(self, text='')
        self.feedbackLabel.pack(pady=10)

        # Exit button
        self.exitButton = ttk.Button(self, text='Exit Game', command=lambda: controller.show_frame(startPage))
        self.exitButton.pack(fill='x', padx=15, pady=(15, 2))

    def load_category(self, category, words):

        self.categoryLabel.config(text=category)

        # Select random word
        self.current_word = random.choice(words)

        # Word length
        self.wordLength = len(self.current_word)

        # Display lines
        self.guessedLetters = ['_' for char in self.current_word]
        self.wordGuessing.config(text='_ ' * self.wordLength)

    # Check letter in game
    def check_letter(self):
        # Get letter
        letter = self.letterEntry.get()

        if letter in self.current_word:

            self.charPosition = [i for i, char in enumerate(self.current_word) if char == letter]

            for position in self.charPosition:
                self.guessedLetters[position] = letter
        
        self.wordGuessing.config(text=' '.join(self.guessedLetters))

        # Reset input and feedback
        self.letterEntry.delete(0, tk.END)



# Results Page


# Run Application
if __name__ == '__main__':
    main()