import random
from List_of_piece_spaces import*
import turtle
from board import *
yp = turtle.Turtle()
rp = turtle.Turtle()

bulidBoard()
rp.up()
rp.goto(boardBox["RH"])
rp.down()
rp.color("purple")
rp.dot(20)

yp.up()
yp.goto(boardBox["YH"])
yp.down()
yp.color("gold")
yp.dot(20)


class SimpleLudoGame:
    def __init__(self):
        self.positions = {'Player 1': -1, 'Player 2': -1}  # Start outside the board (-1)
        self.turn = 'Player 1'  # Player 1 starts
        self.game_over = False

    def roll_dice(self):
        # Simulate a dice roll
        return random.randint(1, 6)

    def move_piece(self, roll, player):
        # Check if the player can start
        if self.positions[player] == -1 and roll == 6:
            self.positions[player] = 0  # Start on the board
            if self.turn == "Player 1":
             rp.clear()
             rp.up()
             rp.goto(boardBox[boardBoxLR[0]])
             rp.down()
             rp.color("purple")
             rp.dot(20)
             return f"{player} starts their piece on the board!", True
            elif self.turn == "Player 2" :
             yp.clear()
             yp.up()
             yp.goto(boardBox[boardBoxLY[0]])
             yp.down()
             yp.color("gold")
             yp.dot(20)
             return f"{player} starts their piece on the board!", True
        elif self.positions[player] >= 0:
            # Check if the player can move
            if self.positions[player] + roll <= 56:  # The total track is 57 spaces including home
                Newroll = roll
                self.positions[player] += roll
                if self.turn == "Player 1":
                    rp.clear()
                    rp.up()
                    rp.goto(boardBox[boardBoxLR[self.positions[player]]])
                    rp.down()
                    rp.color("purple")
                    rp.dot(20)
                    return f"{player} moves their piece to space {self.positions[player]}.", roll == 6
                elif self.turn == "Player 2":
                    yp.clear()
                    yp.up()
                    yp.goto(boardBox[boardBoxLY[self.positions[player]]])
                    yp.down()
                    yp.color("gold")
                    yp.dot(20)
                    return f"{player} moves their piece to space {self.positions[player]}.", roll == 6        
            else:
            # Cannot move as the roll was too high to reach home
                return f"{player} cannot move, roll was too high!", False
        else:
            # Cannot start as the roll was not a 6
            return f"{player} cannot start, they did not roll a 6.", False

    def game_interaction(self, player_input):
        # Check if it's the correct player's turn based on the input
        if (self.turn == 'Player 1' and player_input.upper() == 'R1') or (self.turn == 'Player 2' and player_input.upper() == 'R2'):
            roll = self.roll_dice()
            move_message, is_six = self.move_piece(roll, self.turn)

            # Check for a win condition
            if self.positions[self.turn] == 56:
                self.game_over = True
                return f"{move_message}\n{self.turn} has won the game!"
            
            if roll != 6:
              print(f"{self.turn} rolled a {roll}")  

            # If the player rolled a six, they may roll again unless they just started
            if is_six:
                return f"{move_message}\n{self.turn} rolled a 6 and may roll again!"
            else:
                # Switch turns if the player did not roll a six
                self.turn = 'Player 2' if self.turn == 'Player 1' else 'Player 1'
                return move_message
        else:
            # It's not the player's turn
            return f"It's not your turn, {self.turn}."


# This class represents the core game logic for the simplified Ludo game.


class LudoGameInterface:
    def __init__(self):
        self.player_turn = 1  # Start with player 1

    def display_message(self, message):
        print(message)

    def get_player_input(self):
        if self.player_turn == 1:
            return input("Player 1, please roll by typing 'R1': ")
        else:
            return input("Player 2, please roll by typing 'R2': ")

    def validate_input(self, input_str):
        if (self.player_turn == 1 and input_str.upper() == 'R1') or \
            (self.player_turn == 2 and input_str.upper() == 'R2'):
            return True
        else:
            self.display_message("Invalid input. Please try again.")
            return False

    def update_turn(self):
        # Switch turns between 1 and 2
        self.player_turn = 1 if self.player_turn == 2 else 2

    def play_game(self, game_logic):
        self.display_message("Welcome to Team 1 Ludo Game Version 1.")
        while not game_logic.game_over:
            player_input = self.get_player_input()
            if self.validate_input(player_input):
                response = game_logic.game_interaction(player_input)
                self.display_message(response)
                if "won" in response:
                    break
                if "roll again" not in response.lower():
                    self.update_turn()
        self.display_message("Game Over. Thank you for playing!")





