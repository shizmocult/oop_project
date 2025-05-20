import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("MEMORY GAME")
        self.root.configure(bg="White")
        self.logic = Gamelogic()
        self.style = GameStyle()
        self.buttons = [[None] * 4 for _ in range(4)]
        self.create_header()
        self.build_grid()
        self.create_restart_button()

    def create_heade(self):
        title = tk.Label(self.root, text = "GAME CHALLENGE",
                         font=('Comic Sans MS',25, 'bold'),
                         bg = '#ADD8E6', fg = '#FF00FF')
        title.grid(row=0, column=0, columnspan=4, pady=(10, 20))

