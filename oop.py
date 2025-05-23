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
        
    def restart_game(self):
        self.logic = GameLogic()
        for i in range(4):
            for j in range(4):
                self.style.set_hidden(self.buttons[i][j])

    def show_popup(self,text):
        popup = tk.Toplevel(self.root)
        popup.title("RESULT")
        popup.geometry("300x120")
        popup.configure(bg="white")
        label = tk.Label(popup, text=text,
                         font=('Comic Sans MS', 14),
                         bg="white", fg="black")
        label.pack(pady=15)
        btn = tk.Button(popup, text="ОК", command=popup.destroy,
                        font=('Comic Sans MS', 12),
                        bg="#4CAF50", fg="white")
        btn.pack()
        
    def on_click(self, i, j):
        if self.logic.locked or self.logic.revealed[i][j]:
            return

        symbol = self.logic.symbols[i][j]
        self.style.set_revealed(self.buttons[i][j], symbol)

        if not self.logic.first:
            self.logic.first = (i, j)
        else:
            i1, j1 = self.logic.first
            if self.logic.check_match(i1, j1, i, j):
                self.logic.revealed[i][j] = True
                self.logic.revealed[i1][j1] = True
                self.logic.first = None
                if self.logic.check_win():
                    self.show_popup(" Вітаю! Ви відкрили всі пари!")
            else:
                self.logic.locked = True
                self.root.after(1000, self.hide_cards, i, j, i1, j1)
