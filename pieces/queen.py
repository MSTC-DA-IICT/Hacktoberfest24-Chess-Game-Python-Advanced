# queen.py

import pygame

class Queen:
    def __init__(self, color, piece_type):
        """
        Initializes the Queen piece with a color and type.

        :param color: The color of the piece ('w' for white, 'b' for black).
        :param piece_type: The type of the piece (e.g., 'Q' for Queen).
        """
        self.color = color
        self.piece_type = piece_type
        self.image = self.load_image()  # Load the piece image

    def load_image(self):
        """
        Loads the appropriate image for the Queen based on its color.

        :return: The image for the Queen piece.
        """
        if self.color == 'w':
            return pygame.image.load('assets/pieces/Queen_White.png')  # White Queen image
        else:
            return pygame.image.load('assets/pieces/Queen_Black.png')  # Black Queen image

    def __repr__(self):
        """
        Provides a string representation of the Queen piece.

        :return: The piece type as a string, capitalized for white and lowercase for black.
        """
        return self.piece_type if self.color == 'w' else self.piece_type.lower()
