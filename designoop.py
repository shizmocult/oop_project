# Дизайн гри
class GameStyle:
    def __init__(self):
        self.button_font = ('Segoe UI', 20, 'bold') 

    def style_button(self, btn):
        btn.config(
            width=6, height=3,
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
