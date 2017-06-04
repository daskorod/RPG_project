#! /usr/bin/env python3
import pygame
import levels
import classes
import controller
import character
from level_data import *
from constants import *
import camera
import functions

#settings
pygame.key.set_repeat(100,100)
pygame.key.get_repeat ()

#main

class main ():
	def __init__ (self, control, hero):
		self.control = control
		self.hero = hero
		
	def main_loop (self):
		while True:

			self.control.control ()
			self.hero.transcendental_apperception ()
			pygame.display.update()
			
#create objects (cosmic forces)

son = functions.Son ()
control = controller.Holy_Spirit () 
battle = functions.Battle () #delet
compose_text = functions.Compose_dialog_tree (control,son)

#locations
stage1 = levels.Level1(control, lev1, battle, son)
stage2 = levels.Level2(control, lev2, battle, son)
mainplatz = levels.Platz (control, platz, battle, son)
tavern_loc = levels.Tavern (control, tavern, battle, son)
temple_loc = levels.Temple (control, temple, battle, son)

levels_list = [stage1,temple_loc, stage2, mainplatz]
levels_dict = {'1':stage1, 'end':stage2, 'temple':temple_loc, "tavern":tavern_loc, "platz":mainplatz}
#hero
hero = character.Hero (2,2, battle, control, compose_text, 6,6,6,1, son, levels_list, levels_dict)


#game
game = main (control, hero)
game.main_loop ()



