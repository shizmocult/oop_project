class GameLogic:
    def __init__(self):
        symbols = list("NRKTXYZF") * 2
        random.shuffle(symbols)
        self.symbols = [symbols[i:i + 4] for i in range(0, 16, 4)]
        self.revealed = [[False] * 4 for _ in range(4)]
        self.first = None
        self.locked = False


    def check_match(self, i1, j1, i2, j2):
        return self.symbols[i1][j1] == self.symbols[i2][j2]

    def check_win(self):
        return all(all(row) for row in self.revealed)


