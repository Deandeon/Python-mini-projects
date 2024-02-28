# Ludo Game Version 1 by Group 8
# Members:
# Shadrack Agyei Nti
# David Kweku Amissah Orhin
# Boss Baeta
# Edudzi Ama Nyaho
# Jessica Doesi Tetteh-Yumu


import random
from List_of_piece_spaces import*
import turtle
from board import *
yp = turtle.Turtle()
rp = turtle.Turtle()
from Main_ludo import *



game_logic = SimpleLudoGame()

# Initialize the game interface and start the game:
game_interface = LudoGameInterface()
game_interface.play_game(game_logic)


