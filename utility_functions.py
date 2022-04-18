'''
Yiming Ge
CS 5001, Fall 2021
Final Project
Checker Game
This module contains all utility functions in this program.
'''
import turtle
from constants import*


def draw_square(a_turtle, size, color=None):
    '''
        Function -- draw_square
            Draw a square of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    RIGHT_ANGLE = 90
    a_turtle.color(SQUARE_COLORS[0], color)
    a_turtle.begin_fill()
    a_turtle.pendown()
    for i in range(4):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.end_fill()
    a_turtle.penup()


def draw_circle(a_turtle, size, color):
    '''
        Function -- draw_circle
            Draw a circle with a given radius.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the radius of the circle
        Returns:
            Nothing. Draws a circle in the graphics windo.
    '''
    a_turtle.color(color, color)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.circle(size)
    a_turtle.end_fill()
    a_turtle.penup()


def draw_ring(a_turtle, size):
    '''
        Function -- draw_circle
            Draw a circle with a given radius.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the radius of the circle
        Returns:
            Nothing. Draws a circle in the graphics windo.
    '''
    a_turtle.color(SQUARE_COLORS[1])
    a_turtle.pendown()
    a_turtle.circle(size)
    a_turtle.penup()


def draw_hollow_square(a_turtle, size):
    '''
        Function -- draw_hollow_square
            Draw a hollow square of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    RIGHT_ANGLE = 90
    a_turtle.pendown()
    for i in range(4):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.penup()


def the_starting_ui():  # milestone 1
    '''
        Function -- draw_starting_ui
            Create the initial UI.
        Parameters:
            None.
        Returns:
            Nothing. Draws all the pieces in their correct starting positions
            in 8 * 8 board with a checkerboard pattern.
    '''
    # Create the UI window. This should be the width of the board plus a
    # little margin
    turtle.setup(WINDOW_SIZE, WINDOW_SIZE)

    # Set the drawing canvas size. The should be actual board size
    turtle.screensize(BOARD_SIZE, BOARD_SIZE)
    turtle.bgcolor("white")  # The window's background color
    turtle.tracer(0, 0)  # makes the drawing appear immediately

    pen = turtle.Turtle()  # This variable does the drawing.
    pen.penup()  # This allows the pen to be moved.
    pen.hideturtle()  # This gets rid of the triangle cursor.

    # The first parameter is the outline color, the second is the filler
    pen.color("black", "white")

    # YOUR CODE HERE
    # Step 1 - the board outline
    pen.setposition(CORNER, CORNER)

    draw_square(pen, BOARD_SIZE, SQUARE_COLORS[1])

    # Step 2 & 3 - the checkerboard squares and pieces
    radius = SQUARE / 2
    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            pen.setposition(CORNER + SQUARE * col, CORNER + SQUARE * row)
            if col % 2 != row % 2:
                draw_square(pen, SQUARE, SQUARE_COLORS[0])
                pen.setposition(CORNER + SQUARE * col + radius,
                                CORNER + SQUARE * row)
                if row < 3:
                    # pen.color(PIECE_COLORS[1], PIECE_COLORS[1])
                    draw_circle(pen, radius, PIECE_COLORS[1])
                if row > 4:
                    draw_circle(pen, radius, PIECE_COLORS[0])


def index_to_cordinates_location(row_index, col_index):
    '''
        Function -- index_to_cordinates_location
            Convert index location to cordinates location
        Parameters:
            row_index -- row location, integer from 0 to 7
            col_index -- column location, integer from 0 to 7
        Returns:
            Return x and y cordinates, tuple, float
    '''
    y = (row_index * SQUARE) - (SQUARE * NUM_SQUARES) / 2
    x = (col_index * SQUARE) - (SQUARE * NUM_SQUARES) / 2
    return (x, y)


def cordinates_location_to_index(x, y):
    '''
        Function -- cordinates_to_index_location
            Convert cordinates location to index location
        Parameters:
            x -- x cordinates float
            y -- y cordinates float
        Returns:
            Return row and column index location, tuple, integer
    '''
    row_index = (y + (SQUARE * NUM_SQUARES) / 2) // SQUARE
    col_index = (x + (SQUARE * NUM_SQUARES) / 2) // SQUARE
    return(int(row_index), int(col_index))


def click_not_in_the_bound(x, y):
    '''
        Function -- click_not_in_the_bound
            Check whether the click in the bound based on cordinates
        Parameters:
            x -- x cordinates float
            y -- y cordinates float
        Returns:
            Return True if click out of the bound, otherwise return False
    '''
    bound_axis = NUM_SQUARES * SQUARE / 2
    if x < - bound_axis or x > bound_axis or \
       y < - bound_axis or y > bound_axis:
        return True
    return False


def index_not_in_the_bound(row_i, col_i):
    '''
        Function -- index_not_in_the_bound
            Check whether the index in the nested list
        Parameters:
            row_i -- row location, integer from 0 to 7
            col_i -- column location, integer from 0 to 7
        Returns:
            Return True if click out of the list, otherwise return False
    '''
    if row_i < 0 or row_i >= NUM_SQUARES or \
       col_i < 0 or col_i >= NUM_SQUARES:
        return True
    return False


def draw_highlight(row_i, col_i, is_selected=False, is_movement=False):
    '''
        Function -- draw_highlight
            draw the higlight based on given location
        Parameters:
            row_i -- row location, integer from 0 to 7
            col_i -- column location, integer from 0 to 7
            is_selected -- selecting highlight (blue)
            is_movement -- movement highlight (red)
        Returns:
            Nothing. Draw highlight.
    '''
    (x, y) = index_to_cordinates_location(row_i, col_i)
    pen = turtle.Turtle()  # This variable does the drawing.
    pen.penup()  # This allows the pen to be moved.
    pen.hideturtle()  # This gets rid of the triangle cursor.
    if is_selected is True:
        pen.color(HIGHLIGHT_COLORS[0])
    elif is_movement is True:
        pen.color(HIGHLIGHT_COLORS[1])
    pen.setposition(x, y)
    draw_hollow_square(pen, SQUARE)


def draw_game_state(gamestate):
    '''
        Function -- draw_game_state
            draw the ui based on the gamestate
        Parameters:
            gamestate - class GameState
        Returns:
            Nothing. Draws all the pieces in their correct positions
            in 8 * 8 board with a checkerboard pattern based on gamestate
    '''
    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    for row in range(NUM_SQUARES):
        for col in range(NUM_SQUARES):
            if col % 2 != row % 2:
                (x, y) = index_to_cordinates_location(row, col)
                pen.setposition(x, y)
                draw_square(pen, SQUARE, SQUARE_COLORS[0])
            if gamestate.square[row][col] != EMPTY:
                (x, y) = index_to_cordinates_location(row, col)
                radius = SQUARE / 2
                circle_x = x + radius
                king_y = y + radius/2
                if gamestate.square[row][col] == BLACK:
                    pen.setposition(circle_x, y)
                    draw_circle(pen, radius, PIECE_COLORS[1])
                elif gamestate.square[row][col] == RED:
                    pen.setposition(circle_x, y)
                    draw_circle(pen, radius, PIECE_COLORS[0])
                elif gamestate.square[row][col] == BLACK_KING:
                    pen.setposition(circle_x, y)
                    draw_circle(pen, radius, PIECE_COLORS[1])
                    pen.setposition(circle_x, king_y)
                    draw_ring(pen, radius/2)
                else:
                    pen.setposition(circle_x, y)
                    draw_circle(pen, radius, PIECE_COLORS[0])
                    pen.setposition(circle_x, king_y)
                    draw_ring(pen, radius/2)


def draw_declaration(winner):
    '''
        Function -- draw_declaration
            draw who win the game on the screen
        Parameters:
            winner -- the winner, string
        Returns:
            Nothing. Draw who win the game on the screen
    '''
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("green")
    pen.write("GAME OVER! " + winner + " WINS!", align="center",
              font=("Arial", 25, "normal"))


def check_existence(color, gamestate):
    '''
        Function -- check_existence
            check the given color piece existence on the board
        Parameters:
            color -- the color of piece
            gamestate -- GameState class
        Returns:
            Return Ture if the given color piece exist
            Otherwise return False
    '''
    for row in gamestate.square:
        if color in row:
            return True
    return False
