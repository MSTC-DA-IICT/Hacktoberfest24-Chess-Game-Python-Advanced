# knight.py

import pygame

class Knight:
    def __init__(self, color, piece_type):
        """
        Initializes the Knight piece with a color and type.

        :param color: The color of the piece ('w' for white, 'b' for black).
        :param piece_type: The type of the piece (e.g., 'N' for Knight).
        """
        self.color = color
        self.piece_type = piece_type
        self.image = self.load_image()  # Load the piece image

    def load_image(self):
        """
        Loads the appropriate image for the Knight based on its color.

        :return: The image for the Knight piece.
        """
        if self.color == 'w':
            return pygame.image.load('assets/pieces/Knight_White.png')  # White Knight image
        else:
            return pygame.image.load('assets/pieces/Knight_Black.png')  # Black Knight image

    def __repr__(self):
        """
        Provides a string representation of the Knight piece.

        :return: The piece type as a string, capitalized for white and lowercase for black.
        """
        return self.piece_type if self.color == 'w' else self.piece_type.lower()
