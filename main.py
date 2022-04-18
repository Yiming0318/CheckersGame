'''
Yiming Ge
CS 5001, Fall 2021
Final Project
Checker Game

Run this file to start the game
Follow Basic Checker Game Rule
!!!!!!Notices!!!!!:
Black is your piece, and Red is AI piece.
***Click empty board to let AI move after you finish your turn.***
After you choose your piece, you are not allowed to switch your choice.
Force movement rule applied wich means
only capture movement can be made when there's a capture movement exists.
'''
import turtle
from constants import*
from utility_functions import the_starting_ui
from game_state import*


def main():
    # Create the starting checkerboard user interface
    the_starting_ui()
    # get Class GameState
    game_state = GameState()
    screen = turtle.Screen()
    # This will call the click_handler function when a click occurs
    screen.onclick(game_state.click_handler)
    turtle.done()  # Stops the window from closing.


if __name__ == "__main__":
    main()
