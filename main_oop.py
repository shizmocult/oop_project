import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("MEMORY GAME")
        self.root.configure(bg="White")
        self.root.geometry("417x700")
        self.difficulty = tk.StringVar(value="4x4")
        self.logic = None
        self.style = GameStyle()
        self.buttons = []
        self.create_header()
        self.create_difficulty_selector()
        self.create_restart_button()
        self.build_grid()

    def create_header(self):
        title = tk.Label(self.root, text="GAME CHALLENGE",
                         font=('Comic Sans MS', 21, 'bold'),
                         bg='white', fg='#FF00FF')
        title.grid(row=0, column=0, columnspan=4, pady=(10, 10))

    def create_difficulty_selector(self):
        label = tk.Label(self.root, text="Choose difficulty:",
                         font=('Comic Sans MS', 12), bg="white")
        label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        options = ["2x2", "3x3", "4x4"]
        dropdown = tk.OptionMenu(self.root, self.difficulty, *options, command=self.on_difficulty_change)
        dropdown.config(font=('Comic Sans MS', 12), bg="#D1C4E9", fg="black")
        dropdown.grid(row=1, column=2, columnspan=2)

    def create_restart_button(self):
        self.restart = tk.Button(self.root, text="RESTART",
                            command=self.restart_game,
                            font=('Comic Sans MS', 20),
                            bg="#FF8A65", fg="#fff",
                            activebackground="#FFAB91",
                            padx=10, pady=5,
                            bd=0, relief=tk.FLAT)
        self.restart.grid(row=100, column=0, columnspan=4, pady=(15, 10))

    def build_grid(self):
        size = int(self.difficulty.get()[0])
        self.logic = GameLogic(size)
        self.clear_grid()
        self.buttons = [[None] * size for _ in range(size)]

        for i in range(size):
            for j in range(size):
                btn = tk.Button(self.root, command=lambda i=i, j=j: self.on_click(i, j))
                self.style.style_button(btn)
                self.style.set_hidden(btn)
                btn.grid(row=i + 2, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn

    def clear_grid(self):
        for widget in self.root.grid_slaves():
            if isinstance(widget, tk.Button) and widget != self.restart:
                widget.destroy()

    def restart_game(self):
        self.build_grid()

    def on_difficulty_change(self, _):
        self.build_grid()

    def show_popup(self, text):
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
                    self.show_popup("Вітаю! Ви відкрили всі пари!")
            else:
                self.logic.locked = True
                self.root.after(1000, self.hide_cards, i, j, i1, j1)

    def hide_cards(self, i, j, i1, j1):
        self.style.set_hidden(self.buttons[i][j])
        self.style.set_hidden(self.buttons[i1][j1])
        self.logic.first = None
        self.logic.locked = False

class GameStyle:
    def __init__(self):
        self.button_font = ('Segoe UI', 15, 'bold')

    def style_button(self, btn):
        btn.config(
            width=7, height=3,
            font=self.button_font,
            bg="#B39DDB", fg="#FFFFFF",
            activebackground="#9575CD",
            relief=tk.FLAT,
            bd=0,
            highlightthickness=3,
            highlightbackground="#D1C4E9",
            cursor="hand2"
        )

    def set_hidden(self, btn):
        btn.config(
            text="🌸",
            bg="#B39DDB",
            fg="#FFFFFF",
            font=self.button_font
        )

    def set_revealed(self, btn, symbol):
        btn.config(
            text=symbol,
            bg="#C8E6C9",
            fg="#2E7D32",
            font=self.button_font
        )

class GameLogic:
    def __init__(self, size):
        self.size = size
        total = size * size
        pair_count = total // 2
        symbols = random.sample("NRKTXYZF", pair_count) * 2
        random.shuffle(symbols)
        self.symbols = [symbols[i:i + size] for i in range(0, total, size)]
        self.revealed = [[False] * size for _ in range(size)]
        self.first = None
        self.locked = False

    def check_match(self, i1, j1, i2, j2):
        return self.symbols[i1][j1] == self.symbols[i2][j2]

    def check_win(self):
        return all(all(row) for row in self.revealed)

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryGame(root)
    root.mainloop()
