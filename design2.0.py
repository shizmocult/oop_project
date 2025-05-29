class GameStyle:
    def __init__(self):
        self.button_font = ('Arial', 15, 'bold')
        self.width = 7
        self.height = 3

    def update_size(self, rows, cols):
        total = rows * cols
        if total == 4:
            self.button_font = ('Arial', 24, 'bold')
            self.width = 8
            self.height = 4
        elif total == 8:
            self.button_font = ('Arial', 20, 'bold')
            self.width = 8
            self.height = 4
        else:
            self.button_font = ('Arial', 15, 'bold')
            self.width = 7
            self.height = 3

    def style_button(self, btn):
        btn.config(
            width=self.width, height=self.height,
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
