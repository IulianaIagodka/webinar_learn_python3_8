def opposite_char(char):
    return '0' if char == 'X' else 'X'
class Bot:
    def __init__(self, char):
        self.char = char

    def move (self):
        free_cells = [(x, y) for x in range (3) for y in range (3) if field[x, y] == ' ']
        for x, y in free_cells:
            field[x, y] = self.char
            if field.is_win(self.char):
                return  x, y

