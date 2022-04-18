'''
Yiming Ge
CS5001 Fall 2021
Final Project
Movement Class unit test except anything that interacts
directly with Turtle.
'''
from movement import *
from game_state import GameState


def test_constructor():
    movement = Movement(3, 4)
    assert(movement.start == 3)
    assert(movement.end == 4)


def test_valid_click():
    gamestate = GameState()
    assert(Movement.valid_click(gamestate, 0, 0) is False)
    assert(Movement.valid_click(gamestate, 0, 1) is True)


def test_valid_normal_movements():
    gamestate = GameState()
    Movement.valid_normal_movements(Movement, gamestate, BLACK, 0, 1)
    assert(gamestate.valid_movements == [])
    Movement.valid_normal_movements(Movement, gamestate, BLACK, 2, 1)
    assert(len(gamestate.valid_movements) == 2)


def test_valid_capturing_movement():
    gamestate = GameState()
    assert(Movement.valid_capturing_movement(Movement, gamestate, RED, 2, 1,
                                             cal=True) is False)
    assert(gamestate.valid_movements == [])
    gamestate.square[5][2] = EMPTY
    gamestate.square[3][4] = RED
    assert(Movement.valid_capturing_movement(Movement, gamestate, BLACK, 2, 3,
                                             cal=True) is True)


def test_check_capture_movement():
    gamestate = GameState()
    assert(Movement.check_capture_movement(Movement, gamestate, BLACK,
                                           location=False) is False)
    assert(Movement.check_capture_movement(Movement, gamestate, BLACK,
                                           location=True) == [])
    assert(Movement.check_capture_movement(Movement, gamestate, RED,
                                           location=False) is False)
    assert(Movement.check_capture_movement(Movement, gamestate, RED,
                                           location=True) == [])


def test_valid_movements_cal():
    gamestate = GameState()
    Movement.valid_movements_cal(Movement, gamestate, 0, 1)
    assert(len(gamestate.valid_movements) == 0)
    Movement.valid_movements_cal(Movement, gamestate, 2, 1)
    assert(len(gamestate.valid_movements) == 2)
