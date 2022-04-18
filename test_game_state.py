'''
Yiming Ge
CS5001 Fall 2021
Final Project
GameState Class unit test except anything that interacts
directly with Turtle.
'''
from constants import BLACK, BLACK_KING, RED, RED_KING
from game_state import GameState

# update_gamestate, select_normal_piece, select_capturing_piece, winner_update,
# computer_player interacts with Turtle and drawing.


def test_constructor():
    gamestate = GameState()
    assert(len(gamestate.square) == 8)
    assert(gamestate.current_index_location is None)
    assert(gamestate.current_turn == BLACK)
    assert(gamestate.valid_movements == [])


def test_update_king_piece():
    gamestate = GameState()
    gamestate.square[0][7] = RED
    gamestate.update_king_piece()
    assert(gamestate.square[0][7] == RED_KING)
    gamestate.square[0][7] = BLACK
    gamestate.update_king_piece()
    assert(gamestate.square[0][7] == BLACK)
    gamestate.square[7][0] = BLACK
    gamestate.update_king_piece()
    assert(gamestate.square[7][0] == BLACK_KING)
    gamestate.square[7][0] = RED
    gamestate.update_king_piece()
    assert(gamestate.square[7][0] == RED)


def test_all_possible_movement():
    gamestate = GameState()
    gamestate.all_possible_movement(BLACK, BLACK_KING)
    assert(len(gamestate.valid_movements) == 7)


def test_click_handler():
    gamestate = GameState()
    # Invalid click
    gamestate.click_handler(-200, -200)
    assert(len(gamestate.valid_movements) == 0)
    gamestate.click_handler(150, -200)
    assert(len(gamestate.valid_movements) == 0)
    # Valid click interact with Turtle
