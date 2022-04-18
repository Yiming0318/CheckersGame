'''
Yiming Ge
CS 5001, Fall 2021
Final Project
Checker Game
This module contains a class representing game state.
'''
from constants import*
from movement import Movement
from utility_functions import*
import random


class GameState:
    '''
        Class -- GameState
            Represents checker game state.
        Attributes:
            square -- A nested list storing piece locations
            current_turn -- current turn (red or black)
            current_index_location -- selected piece index location
            valid_movements -- a list store valid movements of selected piece
        Methods:
            update_game_state -- update the gamestate after one movement
            click_handler -- called when a click occurs
            select_normal_piece -- determined the selected piece with normal
                                   movement and draw highlight
            select_capturing_piece -- determined the selected piece with
                                      capture movement and draw highlight
            update_king_piece -- update the king piece
            winner_update -- update the winner
            computer_player -- the computer player movement
            all_possible_movement -- calculate all possibale move
                                     for given color piece
    '''
    def __init__(self):
        '''
            Constructor -- Creates a initial GameState
            Parameters:
                self -- the current GameState object
        '''
        self.square = [[EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY,
                        BLACK],
                       [BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK,
                        EMPTY],
                       [EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY,
                        BLACK],
                       [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
                        EMPTY],
                       [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
                        EMPTY],
                       [RED, EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY],
                       [EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY, RED],
                       [RED, EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY]]
        self.current_turn = BLACK  # black goes first
        self.current_index_location = None
        self.valid_movements = []

    def update_game_state(self, move):
        '''
            Method -- update_game_state
                update the gamestate after one movement
            Parameter:
                self -- the current GameState Object
                move -- the Movement Object represents the movement of a piece
            Return:
                Nothing, draw the check board based on game state
        '''
        start_location = move.start
        end_location = move.end
        selected_piece = self.square[start_location[0]][start_location[1]]
        # update game state list -- move a piece
        # let start location be empty
        self.square[start_location[0]][start_location[1]] = EMPTY
        # determine whether capture movement
        surrounding = 4
        for direction in DIRECTIONS[RED_KING]:
            if end_location[0] != start_location[0] + direction[0] \
               and end_location[1] != start_location[1] + direction[1]:
                surrounding -= 1
        if surrounding == 0:
            self.square[end_location[0]][end_location[1]] = selected_piece
            del_r = (end_location[0] - start_location[0])/2 + start_location[0]
            del_c = (end_location[1] - start_location[1])/2 + start_location[1]
            # remove the capture piece
            self.square[int(del_r)][int(del_c)] = EMPTY
        # let the end location be the selected piece
        self.square[end_location[0]][end_location[1]] = selected_piece
        # update king piece
        self.update_king_piece()
        # draw new state
        draw_game_state(self)
        # update the winner
        self.winner_update()

    def click_handler(self, x, y):
        '''
            Method -- click_handler
                handle the click
            Parameter:
                self -- the current GameState Object
                x -- x-axis value in canvas
                y -- y-axis value in canvas
            Return:
                Nothing,
                handle the click to determine
                the user sleceted and moved location
        '''
        self.computer_player()  # AI player
        if click_not_in_the_bound(x, y) is False:
            turn = self.current_turn[:3]
            # select pice
            if self.current_index_location is None:
                if Movement.check_capture_movement(Movement, self, turn) \
                   is False:
                    self.select_normal_piece(x, y)
                else:
                    self.select_capturing_piece(x, y)
            # move the piece
            else:
                (row_index, col_index) = self.current_index_location
                (row_selected, col_selected) = \
                    cordinates_location_to_index(x, y)
                legal_click = False
                color = self.square[row_index][col_index]
                if Movement.valid_capturing_movement(Movement, self, color,
                                                     row_index, col_index) \
                        is True:  # capture movement
                    self.valid_movements = []
                    Movement.valid_capturing_movement(Movement, self, color,
                                                      row_index, col_index,
                                                      cal=True)
                    for movement in self.valid_movements:
                        if row_selected == movement.end[0] and col_selected ==\
                           movement.end[1]:
                            legal_click = True
                            break
                    if legal_click:
                        self.update_game_state(movement)
                        color = self.square[row_selected][col_selected]
                        self.current_index_location = None
                        self.valid_movements = []
                        # multi capture movements situation
                        if Movement.valid_capturing_movement(Movement, self,
                                                             color,
                                                             row_selected,
                                                             col_selected):
                            (x_selected, y_selected) = \
                                index_to_cordinates_location(row_selected,
                                                             col_selected)
                            self.select_capturing_piece(x_selected, y_selected)
                            (row_index, col_index) = \
                                self.current_index_location
                            (x, y) = (0, 0)
                            (row_selected, col_selected) = \
                                cordinates_location_to_index(x, y)
                            color = self.square[row_index][col_index]
                            legal_click = False
                            self.valid_movements = []
                            Movement.valid_capturing_movement(Movement, self,
                                                              color, row_index,
                                                              col_index,
                                                              cal=True)
                            continue_move = True
                        else:
                            continue_move = False
                        # movement finished, change the turn
                        if not continue_move:
                            if self.current_turn == BLACK:
                                self.current_turn = RED
                            else:
                                self.current_turn = BLACK
                    else:
                        print(ILLEGAL_CLICK)
                else:  # normal movement
                    for movement in self.valid_movements:
                        if row_selected == movement.end[0] and col_selected ==\
                             movement.end[1]:
                            legal_click = True
                            break
                    if legal_click:
                        self.update_game_state(movement)
                        self.current_index_location = None
                        self.valid_movements = []
                        # change the turn
                        if self.current_turn == BLACK:
                            self.current_turn = RED
                        else:
                            self.current_turn = BLACK
                    else:
                        print(ILLEGAL_CLICK)
        else:
            print(ILLEGAL_CLICK)

    def select_normal_piece(self, x, y):
        '''
            Method -- select_normal_piece
                determined the selected piece with normal movement
                and draw highlight
            Parameter:
                self -- the current GameState Object
                x -- x-axis value in canvas
                y -- y-axis value in canvas
            Return:
                Nothing, draw the highlight for seleced piece with normal move
        '''
        (row_index, col_index) = cordinates_location_to_index(x, y)
        current_piece = self.square[row_index][col_index]
        if current_piece != EMPTY and \
           current_piece[:3] == self.current_turn[:3]:
            Movement.valid_movements_cal(Movement, self, row_index, col_index)
            if self.valid_movements != []:
                self.current_index_location = (row_index, col_index)
                draw_highlight(row_index, col_index, is_selected=True)
            for movement in self.valid_movements:
                draw_highlight(movement.end[0], movement.end[1],
                               is_movement=True)
        else:
            print(ILLEGAL_CLICK)

    def select_capturing_piece(self, x, y):
        '''
            Method -- select_capturing_piece
                determined the selected piece with capture movement
                and draw highlight
            Parameter:
                self -- the current GameState Object
                x -- x-axis value in canvas
                y -- y-axis value in canvas
            Return:
                Nothing, draw the highlight for seleced piece with capture move
        '''
        (row_index, col_index) = cordinates_location_to_index(x, y)
        for legal_location \
                in Movement.check_capture_movement(Movement, self,
                                                   self.current_turn[:3],
                                                   location=True):
            legal_row = legal_location[0]
            legal_col = legal_location[1]
            legal_click = False
            if row_index == legal_row and col_index == legal_col:
                legal_click = True
                break
        if legal_click:
            Movement.valid_movements_cal(Movement, self, row_index, col_index)
            if self.valid_movements != []:
                self.current_index_location = (row_index, col_index)
                draw_highlight(row_index, col_index, is_selected=True)
            for movement in self.valid_movements:
                draw_highlight(movement.end[0], movement.end[1],
                               is_movement=True)
        else:
            print(ILLEGAL_CLICK)

    def update_king_piece(self):
        '''
            Method -- update_king_piece
                update the king piece
            Parameter:
                self -- the current GameState Object
            Return:
                Nothing, change the specific normal piece to king piece
        '''
        for col in range(NUM_SQUARES):
            if self.square[0][col] == RED:
                self.square[0][col] = RED_KING
            if self.square[7][col] == BLACK:
                self.square[7][col] = BLACK_KING

    def winner_update(self):
        '''
            Method -- winner_update
                update the winner
            Parameter:
                self -- the current GameState Object
            Return:
                Nothing, print the winner on the screen
        '''
        self.valid_movements = []
        if self.current_turn == BLACK:
            self.current_turn = RED
            if check_existence(RED, self) or check_existence(RED_KING, self):
                self.all_possible_movement(RED, RED_KING)
                if self.valid_movements == []:
                    draw_declaration('BLACK')
                self.valid_movements = []
            else:
                draw_declaration('BLACK')
            self.current_turn = BLACK
        else:
            self.current_turn = BLACK
            if check_existence(BLACK, self) or \
               check_existence(BLACK_KING, self):
                self.all_possible_movement(BLACK, BLACK_KING)
                if self.valid_movements == []:
                    draw_declaration('RED')
                self.valid_movements = []
            else:
                draw_declaration('RED')
            self.current_turn = RED

    def computer_player(self):
        '''
            Method -- computer_player
                the computer player movement
            Parameter:
                self -- the current GameState Object
            Return:
                Nothing, computer player select and move the piece
        '''
        if self.current_turn == RED:
            if check_existence(RED, self) or check_existence(RED_KING, self):
                # normal movement
                if Movement.check_capture_movement(Movement, self,
                                                   self.current_turn[:3]) \
                                                       is False:
                    # random choose one movement from
                    # all possible movements of AI
                    self.all_possible_movement(RED, RED_KING)
                    choices = self.valid_movements
                    choice = random.choice(choices)
                    self.update_game_state(choice)
                    self.valid_movements = []
                    self.current_turn = BLACK
                else:  # capture movement
                    self.valid_movements = []
                    locations = \
                        Movement.check_capture_movement(Movement, self,
                                                        self.current_turn[:3],
                                                        location=True)
                    self.valid_movements = []
                    for location in locations:
                        color = self.square[location[0]][location[1]]
                        Movement.valid_capturing_movement(Movement, self,
                                                          color,
                                                          location[0],
                                                          location[1],
                                                          cal=True)
                    choices = self.valid_movements
                    choice = random.choice(choices)
                    self.update_game_state(choice)
                    # multi capture movements situation
                    (row_selected, col_selected) = choice.end
                    color = self.square[row_selected][col_selected]
                    if Movement.valid_capturing_movement(Movement, self,
                                                         color,
                                                         row_selected,
                                                         col_selected):
                        self.valid_movements = []
                        Movement.valid_capturing_movement(Movement, self,
                                                          color, row_selected,
                                                          col_selected,
                                                          cal=True)
                        continue_move = True
                    else:
                        continue_move = False
                    # change the turn when finish the movement
                    if not continue_move:
                        self.valid_movements = []
                        self.current_turn = BLACK

    def all_possible_movement(self, color, kingcolor):
        '''
            Method -- all_possible_movement
                calculate all possibale move for given color piece
            Parameter:
                self -- the current GameState Object
                color -- the piece color
                kingcolor -- the king piece color
            Return:
                Nothing, value stored in self.valid_movements
        '''
        for row in range(NUM_SQUARES):
            for col in range(NUM_SQUARES):
                if self.square[row][col] == color:
                    Movement.valid_movements_cal(Movement, self, row, col)
                if self.square[row][col] == kingcolor:
                    Movement.valid_movements_cal(Movement, self, row, col)
