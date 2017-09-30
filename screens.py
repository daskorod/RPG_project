import pygame
from pygame import Surface
from pygame import image
from pygame import display
from constants import *
import fonts
import sys


if len(sys.argv)>1:
	if sys.argv[1] == 'f':
		#print ('Test mode')
		#control.auto = False
		#test_arg = True
		window = display.set_mode((860,634),pygame.FULLSCREEN)

	else:
		window = display.set_mode((860, 634))

else:
	window = display.set_mode((860, 634))	
#display.toggle_fullscreen()
#


display.set_caption('Giperborea')

text_intro_screen = Surface ((600, 150))
start_screen = Surface((840, 630))
#background = image.load ('images/back.png')
adventure_screen = Surface ((840, 420))
instrumental_screen = Surface ((880,190))
hero_screen = Surface ((180,190))
monster_screen = Surface ((190,200))
information_screen = Surface ((680,190))
roll_screen = Surface ((600, 170))
high_screen = Surface ((810, 22))
inventory_screen = Surface ((380,380))
char_screen = Surface ((380,380))
journal_screen = Surface ((380,380))
start_screen_text_surface = pygame.Surface ((300, 100))	


def main_interface (level):
	window.blit(start_screen, (10, 10))

	start_screen.fill ((black))
	start_screen.blit (high_screen, (0,2))
	high_screen.fill ((black))
	start_screen.blit (adventure_screen, (0,25))
	adventure_screen.fill ((black))
	start_screen.blit (instrumental_screen, (0,430))
	instrumental_screen.fill ((black))
	instrumental_screen.blit (hero_screen, (0,2))
	hero_screen.fill ((black))

	instrumental_screen.blit (information_screen, (180,10))
	information_screen.fill ((black))
	high_screen.blit(fonts.font5.render (level.name, True, (250,250,250)),(580,0))
