from chess_piece import ChessPiece
from move import Move


class Queen(ChessPiece):
    def __str__(self) -> str:
        return 'Queen'

    def type(self) -> str:
        return 'Queen'

    # FIX ME
    def is_valid_move(self, move: Move, board) -> bool:
        if not super().is_valid_move(move, board):
            return False
        if not isinstance(self, Queen):
            return False

        # King movements
        # if (abs(move.from_col - move.to_col) == 1) or (abs(move.from_row - move.to_row) == 1):
        #     return True
        # # Checks if the difference of starting position of col and row to where you are trying to move is equal to one
        # elif (abs(move.from_col - move.to_col) == 1) and (abs(move.from_row - move.to_row) == 1):
        #     return True
        # End of King Movements
        # Start of Bishop Movement

        if abs(move.from_col - move.to_col) == abs(move.from_row - move.to_row):
            if move.to_row > move.from_row:
                row = 1
            else:
                row = -1

            if move.to_col > move.from_col:
                col = 1
            else:
                col = -1

            x = move.from_row + row
            y = move.from_col + col
            while (x, y) != (move.to_row, move.to_col):
                if board[x][y] is not None:
                    return False
                x += row
                y += col

            return True
            #End of Bishop Movement
        #Start of Rook movement
        else:
            x = move.from_row
            y = move.from_col

            if move.from_row == move.to_row:
                while (x, y) != (move.to_row, move.to_col):
                    if move.to_col > move.from_col:
                        y += 1
                    else:
                        y -= 1
                    if board[x][y] is not None and (x, y) != (move.to_row, move.to_col):
                        return False

                return True
            if move.from_col == move.to_col:
                while (x, y) != (move.to_row, move.to_col):
                    if move.to_row > move.from_row:
                        x += 1
                    else:
                        x -= 1
                    if board[x][y] is not None and (x, y) != (move.to_row, move.to_col):
                        return False

                return True
            # End of Rook Movements




