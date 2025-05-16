import random
import json
import os

class GameLogic:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[0]*self.size for _ in range(self.size)]
        self.score = 0
        self.best_score = self.load_best_score()
        self.reset()

    def load_best_score(self):
        try:
            if os.path.exists('scores.json'):
                with open('scores.json', 'r') as f:
                    data = json.load(f)
                    return data.get('best_score', 0)
        except:
            return 0
        return 0

    def save_best_score(self):
        try:
            with open('scores.json', 'w') as f:
                json.dump({'best_score': self.best_score}, f)
        except:
            pass

    def reset(self):
        self.grid = [[0]*self.size for _ in range(self.size)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def compress(self, row):
        new_row = [num for num in row if num != 0]
        new_row += [0] * (self.size - len(new_row))
        return new_row

    def merge(self, row):
        for i in range(self.size - 1):
            if row[i] != 0 and row[i] == row[i+1]:
                row[i] *= 2
                self.score += row[i]
                if self.score > self.best_score:
                    self.best_score = self.score
                    self.save_best_score()
                row[i+1] = 0
        return self.compress(row)

    def move_left(self):
        moved = False
        for i in range(self.size):
            compressed = self.compress(self.grid[i])
            merged = self.merge(compressed)
            if merged != self.grid[i]:
                self.grid[i] = merged
                moved = True
        return moved

    def move_right(self):
        moved = False
        for i in range(self.size):
            reversed_row = self.grid[i][::-1]
            compressed = self.compress(reversed_row)
            merged = self.merge(compressed)
            merged = merged[::-1]
            if merged != self.grid[i]:
                self.grid[i] = merged
                moved = True
        return moved

    def move_up(self):
        moved = False
        for j in range(self.size):
            col = [self.grid[i][j] for i in range(self.size)]
            compressed = self.compress(col)
            merged = self.merge(compressed)
            if merged != col:
                for i in range(self.size):
                    self.grid[i][j] = merged[i]
                moved = True
        return moved

    def move_down(self):
        moved = False
        for j in range(self.size):
            col = [self.grid[i][j] for i in range(self.size)][::-1]
            compressed = self.compress(col)
            merged = self.merge(compressed)
            merged = merged[::-1]
            if merged != [self.grid[i][j] for i in range(self.size)]:
                for i in range(self.size):
                    self.grid[i][j] = merged[i]
                moved = True
        return moved

    def add_random_tile(self):
        empty = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] == 0]
        if empty:
            i, j = random.choice(empty)
            self.grid[i][j] = random.choice([2, 4]) 