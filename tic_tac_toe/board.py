from constants import FIELD_X, FIELD_O, FIELD_EMPTY, WAYS_TO_WIN
from illegal_move import IllegalMove


class Board: 
    def __init__(self):
        """Initializes an empty board."""
        self.board = [FIELD_EMPTY] * 9
        
    def __str__(self):
        """Return a string with game board."""
        return "{}║{}║{}\n═╬═╬═\n{}║{}║{}\n═╬═╬═\n{}║{}║{}".format(*self.board)

    def check_win(self):
        """Determine if a token/player meets victory conditions."""
        for letter in (FIELD_X, FIELD_O):
            victory = [letter, letter, letter]
            if any(self.board[s] == victory for s in WAYS_TO_WIN):
                return letter
        return None

    def open_spots(self):
        """Return a list of all cell numbers/keys not occupied by any token."""
        return [i + 1 for i, cell in enumerate(self.board) if cell == FIELD_EMPTY]

    def play(self, letter, spot):
        """Attempt to place a token on a cell. Raise exception if the cell is already occupied."""
        i = spot - 1
        if self.board[i] == FIELD_EMPTY:
            self.board[i] = letter
        else:
            raise IllegalMove(f"Spot {spot} is already occupied.")
