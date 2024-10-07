# Class representing a king piece
class King:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type
        self.is_untouched = True

    # Representation for printing the piece
    def __repr__(self):
        return self.piece_type if self.color == 'w' else self.piece_type.lower()

    # Placeholder for validating king movement
    def is_valid_move(self, board, start, end):

        start_x, start_y = start
        end_x, end_y = end

        # If the end position have a piece then that piece color should not be same as currunt piece color
        if board[end_x][end_y] and board[end_x][end_y].color == self.color:
            return False

        is_valid_hr_move =  self.is_horizontal_move(start, end)
        is_valid_dia_move = self.is_diagonal_move(start, end)
        is_valid_vr_move = self.is_vertical_move(start, end)

        return is_valid_hr_move or is_valid_dia_move or is_valid_vr_move

    # Placeholder for horizontal move validation
    def is_horizontal_move(self, start, end):

        start_x, start_y = start
        end_x, end_y = end

        is_hr_move = (start_x == end_x and abs(start_y-end_y) == 1)

        return is_hr_move

    # Placeholder for diagonal move validation
    def is_diagonal_move(self, start, end):

        start_x, start_y = start
        end_x, end_y = end

        delta = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        is_dia_move = ((end_x-start_x, end_y-start_y) in delta)

        return is_dia_move

    # Placeholder for diagonal move validation
    def is_valid_king_castle_move(self, board, start, end):
        
        start_x, start_y = start
        end_x, end_y = end

        # Four possible castles
        # To castle king and rook should be at their original location
        # There should not a any piece between rook and king

        rook_is_present = False
        no_piece_in_bw = True
        is_untouched = False

        if start_x == 7 and start_y == 4 and end_x == 7 and end_y == 6:
            # White-King Kingside Castle
            # King's Position should be (7,4) and Rook's Position should be (7,7) and there should not be any piece between them
            # Also the end position should be (7, 6)
            
            rook_is_present = (board[7][7].__repr__() in ('r', 'R'))
            no_piece_in_bw = True
            for k in range(5, 7):
                no_piece_in_bw = no_piece_in_bw and (not board[7][k])
            is_untouched = self.is_untouched and (rook_is_present and board[7][7].is_untouched)

        elif start_x == 7 and start_y == 4 and end_x == 7 and end_y == 2:
            # White-King Queenside Castle
            # King's Position should be (7,4) and Rook's Position should be (7,0) and there should not be any piece between them
            # Also the end position should be (7,2)

            rook_is_present = (board[7][0].__repr__() in ('r', 'R'))
            no_piece_in_bw = True
            for k in range(1, 4):
                no_piece_in_bw = no_piece_in_bw and (not board[7][k])
            is_untouched = self.is_untouched and (rook_is_present and board[7][0].is_untouched)

        elif start_x == 0 and start_y == 4 and end_x == 0 and end_y == 6:
            # Black-King Kingside Castle
            # King's Position should be (0,4) and Rook's Position should be (0,7) and there should not be any piece between them
            # Also the end position should be (0, 6)
            
            rook_is_present = (board[0][7].__repr__() in ('r', 'R'))
            no_piece_in_bw = True
            for k in range(5, 7):
                no_piece_in_bw = no_piece_in_bw and (not board[0][k])
            is_untouched = self.is_untouched and (rook_is_present and board[0][7].is_untouched)

        elif start_x == 0 and start_y == 4 and end_x == 0 and end_y == 2:
            # Black-King Queenside Castle
            # King's Position should be (0,4) and Rook's Position should be (0,0) and there should not be any piece between them
            # Also the end position should be (0, 2)

            rook_is_present = (board[0][0].__repr__() in ('r', 'R'))
            no_piece_in_bw = True
            for k in range(1, 4):
                no_piece_in_bw = no_piece_in_bw and (not board[0][k])
            is_untouched = self.is_untouched and (rook_is_present and board[0][0].is_untouched)

        else:
            return False
        
        return rook_is_present and no_piece_in_bw and is_untouched

    # Placeholder for vertical move validation
    def is_vertical_move(self, start, end):

        start_x, start_y = start
        end_x, end_y = end

        is_vr_move = (start_y == end_y and abs(start_x-end_x) == 1)

        return is_vr_move
