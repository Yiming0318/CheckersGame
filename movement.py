'''
Yiming Ge
CS 5001, Fall 2021
Final Project
Checker Game
This module contains a class representing movement.
'''
from constants import*
from utility_functions import index_not_in_the_bound


class Movement:
    '''
        Class -- Movement
            Represents the movement of a piece
        Attributes:
            start -- start location of this movement
            end -- end location of this movement
        Methods:
            valid_click -- check whether the clicked piece is valid
                           in current turn
            valid_normal_movements -- calculate the valid normal movement
                                      based on piece location
            valid_capturing_movements -- determin whether a valid capture move
                                         exists based on piece location
                                         calculate the valid capture movement
            check_capture_movement -- determin whether a capture move exists
                                      on the board based on turn color
                                      get the locations of these capture
                                      movements
            valid_movements_cal -- calculate the valid movements based on
                                   piece location
    '''
    def __init__(self, start_location, end_location):
        '''
            Constructor -- Creates a initial Movement
            Parameters:
                self -- the current Movement object
                start_location -- start location of this movement
                end_location -- end location of this movement
        '''
        self.start = start_location
        self.end = end_location

    def valid_click(gamestate, row_i, col_i):
        '''
            Method -- valid_click
                check whether the clicked piece is valid in current turn
            Parameter:
                gamestate -- GameState class
                row_i -- row location, integer from 0 to 7
                col_i -- column location, integer from 0 to 7
            Return:
                Return True if click a valid color piece in current turn
                Otherwise return False
        '''
        if gamestate.square[row_i][col_i] != EMPTY:
            current_piece = gamestate.square[row_i][col_i]
            if current_piece[:3] == gamestate.current_turn[:3]:
                return True
        return False

    def valid_normal_movements(self, gamestate, color, row_i, col_i):
        '''
            Method -- valid_normal_movements
                calculate the valid normal movement based on piece location
            Parameter:
                self -- the current Movement object
                gamestate -- GameState class
                color -- piece color
                row_i -- row location, integer from 0 to 7
                col_i -- column location, integer from 0 to 7
            Return:
                Nothing, append valid normal move to the
                GameState.valid_movement
        '''
        if Movement.valid_click(gamestate, row_i, col_i) is True:
            for direction in DIRECTIONS[color]:
                moved_row = row_i + direction[0]
                moved_col = col_i + direction[1]
                if index_not_in_the_bound(moved_row, moved_col) \
                   is False and \
                   gamestate.square[moved_row][moved_col] == EMPTY:
                    valid_movement = self([row_i, col_i],
                                          [moved_row, moved_col])
                    gamestate.valid_movements.append(valid_movement)

    def valid_capturing_movement(self, gamestate, color, row_i, col_i,
                                 cal=False):
        '''
            Method -- valid_capturing_movements
                determin whether a valid capture move exists
                based on piece location
                calculate the valid capture movement
            Parameter:
                self -- the current Movement object
                gamestate -- GameState class
                color -- piece color
                row_i -- row location, integer from 0 to 7
                col_i -- column location, integer from 0 to 7
                cal -- if need to calculate let cal equal to True
            Return:
                Return true if there's a capture move, otherwise return False
                If parameter cal = True, append valid capturing move to the
                GameState.valid_movement.
        '''
        got_valid_capturing_move = False
        if Movement.valid_click(gamestate, row_i, col_i) is True:
            if color[:3] == 'red':
                enemy_color = (BLACK, BLACK_KING)
            if color[:3] == 'bla':
                enemy_color = (RED, RED_KING)
            for direction in DIRECTIONS[color]:
                moved_row = row_i + direction[0]
                moved_col = col_i + direction[1]
                if index_not_in_the_bound(moved_row, moved_col) is False and \
                   gamestate.square[moved_row][moved_col] in enemy_color:
                    jumped_row = 2 * direction[0] + row_i
                    jumped_col = 2 * direction[1] + col_i
                    if index_not_in_the_bound(jumped_row, jumped_col) is False\
                       and gamestate.square[jumped_row][jumped_col] == EMPTY:
                        got_valid_capturing_move = True
                        if cal is True:
                            valid_movement = self([row_i, col_i],
                                                  [jumped_row, jumped_col])
                            gamestate.valid_movements.append(valid_movement)
        return got_valid_capturing_move

    def check_capture_movement(self, gamestate, turn, location=False):
        '''
            Method -- check_capture_movement
                determin whether a capture move exists on the board
                based on turn color
                get the locations of these capture movements
            Parameter:
                self -- the current Movement object
                gamestate -- GameState class
                turn -- the turn color
                location -- if need the locations let location equal to True
            Return:
                Return true if there's a capture move, otherwise return False
                If parameter location = True, append valid capturing move
                to the locations list and return locations
        '''
        locations = []
        for row in range(NUM_SQUARES):
            for col in range(NUM_SQUARES):
                color = gamestate.square[row][col]
                if turn == color[:3]:
                    if Movement.valid_capturing_movement(self, gamestate,
                                                         color, row, col)\
                       is True:
                        locations.append((row, col))
        if location is True:
            return locations
        if locations != []:
            return True
        return False

    def valid_movements_cal(self, gamestate, row_i, col_i):
        '''
            Method -- valid_movements_cal
                calculate the valid movements based on piece location
            Parameter:
                self -- the current Movement object
                gamestate -- GameState class
                row_i -- row location, integer from 0 to 7
                col_i -- column location, integer from 0 to 7
            Return:
                Nothing, append valid movements to the
                GameState.valid_movement
        '''
        current_piece = gamestate.square[row_i][col_i]
        if current_piece == RED:
            Movement.valid_normal_movements(self, gamestate, RED, row_i, col_i)
            Movement.valid_capturing_movement(self, gamestate, RED, row_i,
                                              col_i, cal=True)
        elif current_piece == BLACK:
            Movement.valid_normal_movements(self, gamestate, BLACK, row_i,
                                            col_i)
            Movement.valid_capturing_movement(self, gamestate, BLACK, row_i,
                                              col_i, cal=True)
        elif current_piece == BLACK_KING:
            Movement.valid_normal_movements(self, gamestate, BLACK_KING, row_i,
                                            col_i)
            Movement.valid_capturing_movement(self, gamestate, BLACK_KING,
                                              row_i, col_i, cal=True)
        elif current_piece == RED_KING:
            Movement.valid_normal_movements(self, gamestate, RED_KING, row_i,
                                            col_i)
            Movement.valid_capturing_movement(self, gamestate, RED_KING,
                                              row_i, col_i, cal=True)
