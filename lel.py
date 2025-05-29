class GameLogic:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        total = rows * cols
        pair_count = total // 2
        symbols = random.sample("NRKTXYZFABCD", pair_count) * 2
        random.shuffle(symbols)
        self.symbols = [symbols[i:i + cols] for i in range(0, total, cols)]
        self.revealed = [[False] * cols for _ in range(rows)]
        self.first = None
        self.locked = False

    def check_match(self, i1, j1, i2, j2):
        return self.symbols[i1][j1] == self.symbols[i2][j2]

    def check_win(self):
        return all(all(row) for row in self.revealed)
