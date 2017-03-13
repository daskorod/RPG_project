from pygame import Surface
from pygame import image
from pygame import display
from constants import *

window = display.set_mode((830, 620))
display.set_caption('Svinotest')

start_screen = Surface((810, 600))
background = image.load ('images/back.png')
adventure_screen = Surface ((810, 420))
instrumental_screen = Surface ((810,170))
hero_screen = Surface ((60,170))
monster_screen = Surface ((150,150))
information_screen = Surface ((740,170))

def main_interface ():
	window.blit(start_screen, (10, 10))
	start_screen.fill ((black))
	start_screen.blit (adventure_screen, (0,0))
	adventure_screen.fill ((black))
	start_screen.blit (instrumental_screen, (0,430))
	instrumental_screen.fill ((black))
	instrumental_screen.blit (hero_screen, (0,0))
	#hero_screen.fill ((cool_orange))
	instrumental_screen.blit (information_screen, (70,0))
	information_screen.fill ((black))
	instrumental_screen.blit (monster_screen, (650,0))
	monster_screen.fill ((sea_color))