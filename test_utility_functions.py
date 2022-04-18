'''
Yiming Ge
CS5001 Fall 2021
Final Project
Utility functions module test
'''
from utility_functions import *
from game_state import GameState

# draw_square, draw_circle, draw_ring, draw_hollow_square, the_starting_ui,
# draw_highlight, draw_game_state, draw_declaration interacts with Turtle
# and drawing.


def test_index_to_cordinates_location():
    assert(index_to_cordinates_location(0, 0) == (-200, -200))
    assert(index_to_cordinates_location(7, 7) == (150, 150))
    assert(index_to_cordinates_location(0, 7) == (150, -200))


def test_cordinates_location_to_index():
    assert(cordinates_location_to_index(-200, -200) == (0, 0))
    assert(cordinates_location_to_index(150, 150) == (7, 7))
    assert(cordinates_location_to_index(150, -200) == (0, 7))


def test_click_not_in_the_bound():
    assert(click_not_in_the_bound(0, 0) is False)
    assert(click_not_in_the_bound(200, -200) is False)
    assert(click_not_in_the_bound(999, 999) is True)


def test_index_not_in_the_bound():
    assert(index_not_in_the_bound(7, 7) is False)
    assert(index_not_in_the_bound(5, 7) is False)
    assert(index_not_in_the_bound(-7, 1) is True)
    assert(index_not_in_the_bound(-7, 9) is True)


def test_check_existence():
    gamestate = GameState()
    assert(check_existence(RED, gamestate) is True)
