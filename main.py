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

pygame.key.set_repeat(100,100)
pygame.key.get_repeat ()


class main ():
	def __init__ (self, stage1, stage2, control, hero):
		self.stage1 = stage1
		self.stage2 = stage2
		self.control = control
		self.hero = hero
		self.current_location = stage1
		
	def main_loop (self):
		while True:

			self.control.control ()
			self.hero.transcendental_apperception ()
			pygame.display.update()
			

son = functions.Son ()
control = controller.Holy_Spirit () 
battle = functions.Battle (control)
compose_text = functions.Compose_dialog_tree (control,son)
stage1 = levels.Level1(control, lev1, battle, son)
stage2 = levels.Level2(control, lev2, battle, son)
levels_list = [stage1, stage2]
hero = character.Hero (2,2, battle, control, compose_text, 6,6,6,1, son, levels_list)
game = main (stage1, stage2, control, hero)
game.main_loop ()



