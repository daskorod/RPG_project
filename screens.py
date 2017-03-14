from pygame import Surface
from pygame import image
from pygame import display
from constants import *

window = display.set_mode((834, 634))
display.set_caption('Svinotest')

start_screen = Surface((814, 614))
background = image.load ('images/back.png')
adventure_screen = Surface ((810, 420))
instrumental_screen = Surface ((818,178))
hero_screen = Surface ((70,170))
monster_screen = Surface ((130,158))
information_screen = Surface ((736,170))
roll_screen = Surface ((600, 170))



def main_interface ():
	window.blit(start_screen, (10, 10))
	start_screen.fill ((black))
	start_screen.blit (adventure_screen, (0,0))
	adventure_screen.fill ((black))
	start_screen.blit (instrumental_screen, (0,430))
	instrumental_screen.fill ((red))
	instrumental_screen.blit (hero_screen, (4,4))
	#hero_screen.fill ((cool_orange))
	instrumental_screen.blit (information_screen, (74,4))
	information_screen.fill ((black))
