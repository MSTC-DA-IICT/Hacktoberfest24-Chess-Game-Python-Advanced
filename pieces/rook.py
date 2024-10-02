# rook.py

import pygame

class Rook:
    def __init__(self, color, piece_type):
        """
        Initializes the Rook piece with a color and type.

        :param color: The color of the piece ('w' for white, 'b' for black).
        :param piece_type: The type of the piece (e.g., 'R' for Rook).
        """
        self.color = color
        self.piece_type = piece_type
        self.image = self.load_image()  # Load the piece image

    def load_image(self):
        """
        Loads the appropriate image for the Rook based on its color.

        :return: The image for the Rook piece.
        """
        if self.color == 'w':
            return pygame.image.load('assets/pieces/Rook_White.png')  # White Rook image
        else:
            return pygame.image.load('assets/pieces/Rook_Black.png')  # Black Rook image

    def __repr__(self):
        """
        Provides a string representation of the Rook piece.

        :return: The piece type as a string, capitalized for white and lowercase for black.
        """
        return self.piece_type if self.color == 'w' else self.piece_type.lower()
