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


