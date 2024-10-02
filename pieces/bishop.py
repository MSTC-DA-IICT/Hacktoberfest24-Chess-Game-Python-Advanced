# bishop.py

import pygame

class Bishop:
    def __init__(self, color, piece_type):
        """
        Initializes the Bishop piece with a color and type.

        :param color: The color of the piece ('w' for white, 'b' for black).
        :param piece_type: The type of the piece (e.g., 'B' for Bishop).
        """
        self.color = color
        self.piece_type = piece_type
        self.image = self.load_image()  # Load the piece image

    def load_image(self):
        """
        Loads the appropriate image for the Bishop based on its color.

        :return: The image for the Bishop piece.
        """
        if self.color == 'w':
            return pygame.image.load('assets/pieces/Bishop_White.png')  # White Bishop image
        else:
            return pygame.image.load('assets/pieces/Bishop_Black.png')  # Black Bishop image

    def __repr__(self):
        """
        Provides a string representation of the Bishop piece.

        :return: The piece type as a string, capitalized for white and lowercase for black.
        """
        return self.piece_type if self.color == 'w' else self.piece_type.lower()
