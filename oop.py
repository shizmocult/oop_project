import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("MEMORY GAME")
        self.root.configure(bg="White")
        self.logic = GameLogic()
        self.style = GameStyle()
        self.buttons = [[None] * 4 for _ in range(4)]
        self.create_header()
        self.build_grid()
        self.create_restart_button()

    def create_header(self):
        title = tk.Label(self.root, text="GAME CHALLENGE",
                         font=('Comic Sans MS', 25, 'bold'),
                         bg='white', fg='#FF00FF')
        title.grid(row=0, column=0, columnspan=4, pady=(10, 20))

    def build_grid(self):
        for i in range(4):
            for j in range(4):
                btn = tk.Button(self.root, command=lambda i=i, j=j: self.on_click(i, j))
                self.style.style_button(btn)
                self.style.set_hidden(btn)
                btn.grid(row=i + 1, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn

    def create_restart_button(self):
        restart = tk.Button(self.root, text="RESTART",
                            font=('Comic Sans MS',25),
                            bg="#FF8A65", fg="#fff",
                            activebackground="#FFAB91",
                            padx=10, pady=5,
                            bd=0, relief=tk.FLAT)
        restart.grid(row=6, column=0, columnspan=4, pady=(15, 10))


