'''
Yiming Ge
CS 5001, Fall 2021
Final Project
Checker Game

This module contains all the constants in this program.
'''
# UI
NUM_SQUARES = 8  # The number of squares on each row.
SQUARE = 50  # The size of each square in the checkerboard.
BOARD_SIZE = NUM_SQUARES * SQUARE
WINDOW_SIZE = BOARD_SIZE + SQUARE  # The extra + SQUARE is the margin
CORNER = -BOARD_SIZE / 2
# colors
SQUARE_COLORS = ("light gray", "white")
PIECE_COLORS = ("crimson", "black")
HIGHLIGHT_COLORS = ("blue", "red")
# pieces
BLACK_KING = 'black_king'
BLACK = 'black'
RED_KING = 'red_king'
RED = 'red'
EMPTY = 'empty'
# directions
NORTH_WEST = (1, -1)
NORTH_EAST = (1, 1)
SOUTH_WEST = (-1, -1)
SOUTH_EAST = (-1, 1)
DIRECTIONS = {RED: [SOUTH_EAST, SOUTH_WEST],
              BLACK: [NORTH_EAST, NORTH_WEST],
              BLACK_KING: [NORTH_EAST, NORTH_WEST, SOUTH_WEST, SOUTH_EAST],
              RED_KING: [NORTH_EAST, NORTH_WEST, SOUTH_WEST, SOUTH_EAST]}
ILLEGAL_CLICK = 'Either an illegal click or a click to let AI move!'
